#!/bin/bash

GITHUB_PAGES_DIR=$TRAVIS_BUILD_DIR/tests/gh-pages

MONOLITH_DOWNLOAD_URL=https://github.com/Y2Z/monolith/releases/download/v2.3.1/monolith-gnu-linux-x86_64
MONOLITH_DOWNLOAD_DIR=/tmp/monolith
MONOLITH_PATH=$MONOLITH_DOWNLOAD_DIR/monolith

# Make the script verbose

set -x

# Enter the conda environment

source $TRAVIS_BUILD_DIR/env/conda/bin/activate sphinxcontrib-verilog-diagrams

# Update the machine and install prerequisites

sudo apt update
sudo apt install -y wget libssl-dev

# Download monolith and add it to the PATH

mkdir -p $MONOLITH_DOWNLOAD_DIR
wget $MONOLITH_DOWNLOAD_URL -O $MONOLITH_PATH
sudo chmod u+rwx $MONOLITH_PATH

# Create directory for GitHub Pages

mkdir -p $GITHUB_PAGES_DIR

# Generate test HTMLs

cd $TRAVIS_BUILD_DIR/tests && make test

# Open HTTP server

cd $TRAVIS_BUILD_DIR/tests/build
python3 -m http.server 8000 &
sleep 1

# Convert test HTMLs and create the index for GitHub Pages

echo "<html><body><ul>" > $GITHUB_PAGES_DIR/index.html
echo "<h1> Verilog Diagrams Tests </h1>" >> $GITHUB_PAGES_DIR/index.html
HTML_FILES=$(find -name "test_*.html")
for file in $HTML_FILES
do
    FILE_NAME=$(basename $file)
    FILE_NO_EXT_NAME=$(basename $file .html)
    echo "<li><a href=\"$FILE_NAME\">$FILE_NO_EXT_NAME</a></li>" >> $GITHUB_PAGES_DIR/index.html
    $MONOLITH_PATH http://127.0.0.1:8000/$file -o $GITHUB_PAGES_DIR/$FILE_NAME
done
echo "</ul></body></html>" >> $GITHUB_PAGES_DIR/index.html
