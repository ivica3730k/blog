#!/bin/bash

# remove dir html if it exists
if [ -d html ]; then
    rm -rf html
fi
find . -name 'README.md' -execdir sh -c 'mv "$1" "index.md"' _ {} \;
mkdir html
rsync -av --exclude='html/' . html
markdown-folder-to-html ./html
rm -rf html
mv _html html
find . -name 'index.md' -execdir sh -c 'mv "$1" "README.md"' _ {} \;
