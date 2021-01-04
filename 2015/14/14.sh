#!/bin/bash

#Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.

awk -f 14.awk < $1 | sort -n

