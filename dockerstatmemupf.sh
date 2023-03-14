#!/bin/bash

rm statsmemupf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-spgwu --no-stream | awk '{ print $4 }' | awk '{if(NR>1) print $NF}' | tee --append statsmemupf.txt;
    i=$(( $i + 1 ))

done

