#!/bin/bash
#Script that posts an e-mail and subject matter onto URL with cURL
curl -X POST -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
