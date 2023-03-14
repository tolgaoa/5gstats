#!/bin/bash

rm statsnetw.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-spgwu --no-stream | awk '{ print $8 }' | awk '{if(NR>1) print $NF}' | tee --append statsnetw.txt;
    i=$(( $i + 1 ))

done

