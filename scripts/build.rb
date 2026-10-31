# Use after bundle install; avoids Windows bundle-exec path quoting issues.
require 'bundler/setup'
require 'jekyll'
ENV['JEKYLL_ENV'] ||= 'production'
Dir.chdir(File.expand_path('..', __dir__)) do
  Jekyll::Commands::Build.process({ 'trace' => true })
end
