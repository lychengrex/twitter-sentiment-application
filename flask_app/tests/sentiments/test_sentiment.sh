#!/bin/bash
mkdir -p tmp
curl "http://"$(cat IP.txt)"/sentiment/CathieDWood" > tmp/wood-tweets.html
curl "http://"$(cat IP.txt)"/sentiment/realdonaldtrump" > tmp/trump-tweets.html