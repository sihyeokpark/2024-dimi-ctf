#!/bin/sh

docker run -dp 5000:8000 you_are_l_medium
docker run -dp 5001:3000 you_are_l_easy
docker run -dp 5002:13000 ssti

docker run -dp 5003:13370 unreliable