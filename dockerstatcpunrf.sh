#!/bin/bash

rm statscpunrf.txt

i=0
while [ $i -le $1 ]
do 
    docker stats oai-nrf --no-stream | awk '{ print $3 }' | awk '{if(NR>1) print $NF}' | tee --append statscpunrf.txt;
    i=$(( $i + 1 ))

done

