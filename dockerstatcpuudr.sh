#!/bin/bash

rm statscpuudr.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-udr --no-stream | awk '{ print $3 }' | awk '{if(NR>1) print $NF}' | tee --append statscpuudr.txt;
    i=$(( $i + 1 ))

done

