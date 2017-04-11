#!/bin/bash
#Script takes a cURL and displays all valid HTTP methods
curl -si $1 | grep Allow: | awk -F': ' '{print $2 $3 $4}'
