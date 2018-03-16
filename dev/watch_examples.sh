#!/bin/bash
#
# if an example metamodel changes, rebuild the generated docs
#
# note, only one example for now
# FIXME: build_examples.sh should iterate over multiple examples
# or even better, only the one that changed

./venv.sh react.py ../examples -r "^.*\.yaml$" ./build_examples.sh
#./venv.sh react.py ../examples ./build_examples.sh

