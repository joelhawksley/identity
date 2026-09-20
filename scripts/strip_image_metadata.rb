#!/usr/bin/env ruby
# frozen_string_literal: true

# Strips all metadata (EXIF, IPTC, XMP, ICC profiles) from images in the repo.
# Requires ImageMagick (`mogrify` command).

require "open3"

IMAGE_EXTENSIONS = %w[.jpg .jpeg .png .gif .webp .tiff .tif .bmp].freeze
REPO_ROOT = File.expand_path("..", __dir__)

module ImageMetadata
  module_function

  def image_files
    Dir.glob(File.join(REPO_ROOT, "**", "*")).select do |file|
      File.file?(file) && IMAGE_EXTENSIONS.include?(File.extname(file).downcase)
    end.reject { |file| file.include?("_site/") }
  end

  def has_metadata?(file)
    output, status = Open3.capture2("identify", "-format", '%[exif:*]%[iptc:*]%[xmp:*]%[icc:*]%[profile:*]', file)
    raise "ImageMagick could not inspect #{file}" unless status.success?

    !output.strip.empty?
  end

  def strip
    stripped = 0
    skipped = 0
    errored = 0
    files = image_files

    puts "Scanning #{files.length} images..."

    files.each do |file|
      relative = file.sub("#{REPO_ROOT}/", "")

      unless has_metadata?(file)
        skipped += 1
        next
      end

      print "Stripping metadata from #{relative}... "
      _, status = Open3.capture2("mogrify", "-strip", file)

      if status.success?
        puts "done"
        stripped += 1
      else
        puts "FAILED"
        errored += 1
      end
    rescue StandardError => e
      warn "FAILED: #{e.message}"
      errored += 1
    end

    puts
    puts "Results: #{stripped} stripped, #{skipped} already clean, #{errored} errors"
    errored.zero?
  end
end

exit(ImageMetadata.strip ? 0 : 1) if $PROGRAM_NAME == __FILE__
