#!/bin/bash
a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sI $1 -o /dev/null -w "%{http_code}"
