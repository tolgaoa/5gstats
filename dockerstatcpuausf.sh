#!/bin/bash

rm statscpuausf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-ausf --no-stream | awk '{ print $3 }' | awk '{if(NR>1) print $NF}' | tee --append statscpuausf.txt;
    i=$(( $i + 1 ))

done

