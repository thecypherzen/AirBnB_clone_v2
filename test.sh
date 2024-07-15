#!/usr/bin/bash

if ! res=$(test -f myfile); then
    echo "doesnt' exist"
    echo value: "$res"
else
    echo "value: $res"
fi
