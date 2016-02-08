# A sample Guardfile
# More info at https://github.com/guard/guard#readme

## Uncomment and set this to only include directories you want to watch

directories %w(static_dir_dev tengApp/templates) \
 .select{|d| Dir.exists?(d) ? d : UI.warning("Directory #{d} does not exist")}

guard 'livereload' do
  extensions = {
    css: :css,
    scss: :css,
    sass: :css,
    js: :js,
    coffee: :js,
    html: :html,
    png: :png,
    gif: :gif,
    jpg: :jpg,
    jpeg: :jpeg,
    # less: :less, # uncomment if you want LESS stylesheets done in browser
  }
  compiled_exts = extensions.values.uniq
  watch(%r{.+\.(#{compiled_exts * '|'})})
end

