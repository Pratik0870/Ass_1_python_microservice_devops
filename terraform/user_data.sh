#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y docker.io docker-compose
cd /home/ubuntu
docker-compose up -d
