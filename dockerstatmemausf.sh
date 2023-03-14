#!/bin/bash

rm statsmemausf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-ausf --no-stream | awk '{ print $4 }' | awk '{if(NR>1) print $NF}' | tee --append statsmemausf.txt;
    i=$(( $i + 1 ))

done

