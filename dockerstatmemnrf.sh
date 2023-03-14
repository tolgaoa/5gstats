#!/bin/bash

rm statsmemnrf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-nrf --no-stream | awk '{ print $4 }' | awk '{if(NR>1) print $NF}' | tee --append statsmemnrf.txt;
    i=$(( $i + 1 ))

done

