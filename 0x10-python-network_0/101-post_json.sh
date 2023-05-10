#!/bin/bash
# sends a JSON POST req to URL $!, display response body
curl -sI $1 -X POST -d @"$2" -H 'content-type: application/json'