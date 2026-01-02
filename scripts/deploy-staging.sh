#!/bin/bash
set -e

echo " Deploying to STAGING environment..."

docker-compose down
docker-compose pull
docker-compose up -d --build

echo " Deployment completed"

echo " Verifying services..."
docker ps