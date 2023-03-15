#!/bin/bash

### Andrew Watson 04/02/22 ###

# Updates the network.png in $LiCSAR_public
# Input is frame name.

frame=$1

echo "Updating network.png for $frame"

cd $LiCSAR_procdir/*/$frame
update_bperp_file.sh

cd $LiCSAR_public/*/$frame
plot_network.py `pwd` metadata/network.png metadata/gaps.txt

echo "Done"
