#!/bin/bash

rm statsmemudr.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-udr --no-stream | awk '{ print $4 }' | awk '{if(NR>1) print $NF}' | tee --append statsmemudr.txt;
    i=$(( $i + 1 ))

done

