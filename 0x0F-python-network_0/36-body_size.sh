#!/bin/bash
#Displays the size of the body of the response
curl -si $1 | grep Length | cut -d' ' -f2
