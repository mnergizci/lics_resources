#!/usr/bin/env bash
for epoch in `ls $LiCSAR_public/*/$frame/epochs/`; do ls
$LiCSAR_public/*/$frame/epochs/$epoch/*.sltd; done
