#!/bin/bash
#Bash script that takes a url, sends a request to that url and displays the size of the body (in bytes) of the response 
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
