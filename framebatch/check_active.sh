while IFS= read -r line; do
	echo $line
	getFrameStatus.py $line 1
done < iran_frames.txt
