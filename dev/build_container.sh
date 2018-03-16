#!/bin/bash
echo "cleanup"
docker ps --filter status=dead --filter status=exited -aq | xargs docker rm -v
docker images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs -r docker rmi

echo "building container..."
ORIG_DIR=`pwd`
cd ..
docker build -t model-bender .
cd $ORIG_DIR

# now run it
./build_examples.sh
