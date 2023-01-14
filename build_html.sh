mkdir html
cp -r . ./html || true
markdown-folder-to-html ./html
rm -rf ./html
mv _html html
