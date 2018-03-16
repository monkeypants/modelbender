#!/bin/bash
cd ../examples/gosource

# equate pwd to /work/, because indir/outdir are relative to that
#docker run -v `pwd`:/work/ model-bender validate --indir=metamodel
docker run -v `pwd`:/work/ model-bender enterprise --indir=metamodel

# this is a horrible kluidge
# FIXME: container generates files owned by root
sudo chown chtis:chtis _tmp/*
sudo chown chtis:chtis _tmp/*/*
#sudo chown chtis:chtis _tmp/*/*/*

../../scripts/mk_diagrams.sh
cd _tmp
./venv.sh make html
#make latexpdf
