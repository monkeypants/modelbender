#!/bin/bash
#
# if the modelbender source code changes,
# rebuild the container and test it

./venv.sh react.py ../modelbender ./build_container.sh

