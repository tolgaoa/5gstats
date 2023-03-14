#!/bin/bash

/bin/bash ./dockerstatcpuamf.sh $1 &
/bin/bash ./dockerstatcpusmf.sh $1 &
/bin/bash ./dockerstatcpuupf.sh $1 &
/bin/bash ./dockerstatcpuausf.sh $1 &
/bin/bash ./dockerstatcpuudm.sh $1 &
/bin/bash ./dockerstatcpuudr.sh $1 &
/bin/bash ./dockerstatcpunrf.sh $1 &
