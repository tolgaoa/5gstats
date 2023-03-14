#!/bin/bash

rm statscpuupf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-spgwu --no-stream | awk '{ print $3 }' | awk '{if(NR>1) print $NF}' | tee --append statscpuupf.txt;
    i=$(( $i + 1 ))

done

