#!/bin/bash

/bin/bash ./dockerstatmemamf.sh $1 &
/bin/bash ./dockerstatmemsmf.sh $1 &
/bin/bash ./dockerstatmemupf.sh $1 &
/bin/bash ./dockerstatmemausf.sh $1 &
/bin/bash ./dockerstatmemudm.sh $1 &
/bin/bash ./dockerstatmemudr.sh $1 &
/bin/bash ./dockerstatmemnrf.sh $1 &
