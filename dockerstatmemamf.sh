#!/bin/bash

rm statsmemamf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-amf --no-stream | awk '{ print $4 }' | awk '{if(NR>1) print $NF}' | tee --append statsmemamf.txt;
    i=$(( $i + 1 ))

done

