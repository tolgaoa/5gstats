#!/bin/bash

rm statsmemsmf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-smf --no-stream | awk '{ print $4 }' | awk '{if(NR>1) print $NF}' | tee --append statsmemsmf.txt;
    i=$(( $i + 1 ))

done

