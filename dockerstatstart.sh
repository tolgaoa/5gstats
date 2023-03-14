#!/bin/bash

/bin/bash ./dockerstatmemstart.sh $1 &
/bin/bash ./dockerstatcpustart.sh $1 &
