#!/bin/bash

python coding_challenge.py & export pid=$!

spin='-\|/'

i=0
while kill -0 $pid 2>/dev/null
do

  i=$(( (i+1) %4 ))
  printf "\r\tprocess:\t${spin:$i:1} \t"

  sleep 0.1
done

exit 0
