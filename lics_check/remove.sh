#!/usr/bin/env bash

for ifg in `cat $frame.remove.list`; do remove_from_lics.sh $frame $ifg; done
