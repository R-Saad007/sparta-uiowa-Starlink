#!/bin/bash

while true
do
    echo "===== START `date`"
    timeout -k 0 60 bash -c "python3 ./client.py 35.85.33.119 1048576; sleep 100"
    echo "===== END `date`"
done

#./run_client.sh | tee ../udp1.txt

