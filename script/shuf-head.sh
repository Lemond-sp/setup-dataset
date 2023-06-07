#!/bin/sh

# set seed
# 500万文→shuf→600k
head -n 5000000 $1 > '${1}-5000k'
# shuf --random-source=test.txt '${1}-5000k' | head -n $2 > $3