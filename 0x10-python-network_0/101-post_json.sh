#!/bin/bash
# sends a JSON POST req to URL $!, display response body
curl -sL -H "Content-Type: application/json" -d "$(cat "$2")" "$1"