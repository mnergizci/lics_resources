#!/usr/bin/env python3

'''
## check2removelist.py
Convert frame.check.txt list into a list of ifgs and unique epochs.
Epochs are selected for removal if they appear equal to or more times than epoch_threshold.
We ignore ifgs with error code 5, as these are missing unwrapped data which doesn't require a full remake.
'''

import sys

try:
    in_file = str(sys.argv[1])
except IndexError:
    print('Provide frame.check.txt file')

try:
    out_file = sys.argv[2]
except IndexError:
    frame = in_file[-27:-10]
    out_file = frame + '.remove.list'

epoch_threshold = 20 # how many times an epoch has to appear in bad ifgs to be deleted

# open file
with open(in_file,'r') as f:
    f.readline()
    rows = [[str(x) for x in line.split()] for line in f]

# pull out ifg dates and error codes
ifg_dates = []
error_codes = []
for line in rows:
    try:
        if len(line[0]) == 17 and line[1] != '5':
            ifg_dates.append(line[0])
            error_codes.append(line[1])
    except IndexError: # skip empty lines
        continue

#print(ifg_dates)

# get epochs
dates1 = [x[-17:-9] for x in ifg_dates]
dates2 = [x[-8:] for x in ifg_dates]
dates = dates1 + dates2

# test for repeat dates (those likely to have broken at coreg)
epoch_dates = []
for date in dates:
    if dates.count(date) >= epoch_threshold:
        epoch_dates.append(date)

# remove duplicates
epoch_dates = sorted(list(set(epoch_dates)))

# output
with open(out_file,'w') as f:
    for ifg in ifg_dates:
        f.write("%s\n" % ifg)
    for epoch in epoch_dates:
        f.write("%s\n" % epoch)
