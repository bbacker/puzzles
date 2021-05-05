#!/bin/sh -x
docker run --rm -it perm_letters:latest -s $1 | sort | tee out.txt
