#!/bin/bash

# Check if URL is provided as input
if [ $# -eq 0 ]
then
	echo "Usage: $0 [URL]"
	exit 1
fi

# Send request and get size of response body in bytes
response=$(curl -s -w '\n%{size_download}' $1)
size=$(echo "$response" | tail -n 1)
# Display size of response body in bytes
echo "$size"
