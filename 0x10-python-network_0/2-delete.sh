#!/bin/bash
#Bash script that sends a DELETE request to the URL passed as the first argument
#displays the body of the response in output
curl -s "$1" -X DELETE
