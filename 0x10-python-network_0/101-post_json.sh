#!/bin/bash
curl -sI -H "content-type:application/json" -d @"$2" -X POST "$1"