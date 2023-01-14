#!/bin/bash

# remove dir html if it exists
if [ -d html ]; then
    rm -rf html
fi
mkdir html
rsync -av --exclude='html/' . html
markdown-folder-to-html ./html
rm -rf html
mv _html html

