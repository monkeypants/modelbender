#!/bin/bash
# assumes you have graphviz installed
# and that dot files don't have more than one '.' in their names
# and that you have blockdiag, seqdiag, actdiag and nwdiag installed
# and that your .diag files are named *_block.diag, *_seq.diag,
# *_act.diag and *_nw.diag

origdir=`pwd`
for dir in _tmp/domains/*/
do
    cd $dir
    
    # graphviz
    for dotfile in $(ls | grep '^[^\.]*\.dot$')
    do
	prefix=$(echo $dotfile | cut -d. -f1)
	dot -Tpng $prefix.dot -o $prefix.png
    done
    # blockdiag
    for fname in $(ls | grep '^[^\.]*\_block.diag$')
    do
	prefix=$(echo $fname | cut -d. -f1)
	blockdiag -Tsvg $prefix.diag
	blockdiag $prefix.diag
    done
    # seqdiag
    for fname in $(ls | grep '^[^\.]*\_seq.diag$')
    do
	prefix=$(echo $fname | cut -d. -f1)
	seqdiag -Tsvg $prefix.diag
	seqdiag $prefix.diag
    done
    # actdiag
    for fname in $(ls | grep '^[^\.]*\_act.diag$')
    do
	prefix=$(echo $fname | cut -d. -f1)
	actdiag -Tsvg $prefix.diag
	actdiag $prefix.diag
    done
    # nwdiag
    for fname in $(ls | grep '^[^\.]*\_nw.diag$')
    do
	prefix=$(echo $fname | cut -d. -f1)
	nwdiag -Tsvg $prefix.diag
	nwdiag $prefix.diag
    done
    cd $origdir
done
