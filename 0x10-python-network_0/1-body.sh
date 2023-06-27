#!/bin/bash
#Bash script that takes a URL, sends a GET reqest to URL and display response body
curl -sfL "$1" -X GET
