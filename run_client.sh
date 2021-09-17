#!/bin/bash

while true:
    timeout -k 0 60 unbuffer bash -c "echo =======; date; ./client.py 35.85.33.119 1048576 ; sleep 100" | tee "$1" 