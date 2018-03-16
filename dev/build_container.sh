#!/bin/bash
echo "building container..."
ORIG_DIR=`pwd`
cd ..
docker build -t model-bender .
cd $ORIG_DIR

# now run it
./build_examples.sh
