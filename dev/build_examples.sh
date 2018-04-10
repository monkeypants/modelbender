#!/bin/bash
cd ../examples/gosource

# equate pwd to /work/, because indir/outdir are relative to that
#docker run -v `pwd`:/work/ model-bender validate --indir=metamodel
docker run -v `pwd`:/work/ model-bender enterprise --indir=metamodel
docker run -v `pwd`:/work/ model-bender render


# TODO: push this into another command, like render
#cd _tmp
#./venv.sh make html
#make latexpdf
