# frozen_string_literal: true

require_relative "../scripts/strip_image_metadata"

Jekyll::Hooks.register :site, :after_init do
  raise "Could not strip image metadata" unless ImageMetadata.strip
end