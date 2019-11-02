#!/usr/bin/env bash

if [ $# -ne 1 ] || [[ ! $1 =~ ^[0-9]+$ ]]; then
    echo "Usage: leap.sh <year>"
    exit 1
fi


if [ $(($1 % 4)) -eq 0 ]  && [  $(($1 % 100)) -ne 0 ] || [ $(($1 % 400)) -eq 0 ]
then
    echo true
else
    echo false
fi