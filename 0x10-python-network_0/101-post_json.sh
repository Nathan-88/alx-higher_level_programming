#!/bin/bash
# sends a JSON POST req to URL $!, display response body
curl -sI -H "content-type:application/json" -d @"$2" -X POST "$1"