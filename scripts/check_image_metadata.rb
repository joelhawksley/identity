#!/usr/bin/env ruby
# frozen_string_literal: true

# Checks that image files have no metadata (EXIF, IPTC, XMP, ICC profiles).
# Intended to be run as a pre-commit hook via overcommit.
#
# When run with arguments, checks only those files.
# When run without arguments, checks all images in the repo.
#
# Requires ImageMagick (`identify` command).

require "open3"

IMAGE_EXTENSIONS = %w[.jpg .jpeg .png .gif .webp .tiff .tif .bmp].freeze
REPO_ROOT = File.expand_path("..", __dir__)

def image_files
  Dir.glob(File.join(REPO_ROOT, "**", "*")).select do |file|
    File.file?(file) && IMAGE_EXTENSIONS.include?(File.extname(file).downcase)
  end.reject { |file| file.include?("_site/") }
end

def has_metadata?(file)
  output, _ = Open3.capture2("identify", "-format", '%[exif:*]%[iptc:*]%[xmp:*]%[icc:*]%[profile:*]', file)
  !output.strip.empty?
rescue StandardError => e
  warn "Warning: could not check #{file}: #{e.message}"
  false
end

# Check only provided files (from overcommit) or all images
files = if ARGV.any?
  ARGV.select { |f| IMAGE_EXTENSIONS.include?(File.extname(f).downcase) }
       .map { |f| File.expand_path(f, REPO_ROOT) }
else
  image_files
end

failures = []

files.each do |file|
  next unless File.file?(file)

  if has_metadata?(file)
    relative = file.sub("#{REPO_ROOT}/", "")
    failures << relative
  end
end

if failures.any?
  warn "The following images contain metadata:"
  failures.each { |f| warn "  #{f}" }
  warn ""
  warn "Run `ruby scripts/strip_image_metadata.rb` to strip metadata."
  exit 1
else
  puts "All images are clean (no metadata)."
  exit 0
end
