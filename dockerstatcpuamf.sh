#!/bin/bash

rm statscpuamf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-amf --no-stream | awk '{ print $3 }' | awk '{if(NR>1) print $NF}' | tee --append statscpuamf.txt;
    i=$(( $i + 1 ))

done

