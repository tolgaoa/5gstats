#!/bin/bash

rm statscpuudm.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-udm --no-stream | awk '{ print $3 }' | awk '{if(NR>1) print $NF}' | tee --append statscpuudm.txt;
    i=$(( $i + 1 ))

done

