#!/bin/bash

rm statscpusmf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-smf --no-stream | awk '{ print $3 }' | awk '{if(NR>1) print $NF}' | tee --append statscpusmf.txt;
    i=$(( $i + 1 ))

done

