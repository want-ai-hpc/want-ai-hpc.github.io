#! /bin/bash

# Delete previously installed gem plugins 
rm Gemfile.lock 

# Delete folder with previously generated site (if exists) 
[ -d  "_site" ] && rm -r _site

# Install gem plugins defined in Gemfile, _config.yml, _plugins
bundle install
# => File Gemfile.lock will be generated

# Build the site and make it available at the local server
bundle exec jekyll serve 
# => Folder _site will be generated (if does not exist) 

# Browse to http://localhost:4000