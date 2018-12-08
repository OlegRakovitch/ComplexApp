#!/bin/bash

POD_NAME=fitnesse-port-forward

docker stop $POD_NAME
docker rm $POD_NAME

docker run -d \
  -v ${HOME}:/root \
  --rm \
  -p 8081:8081 \
  --name=$POD_NAME \
  geslot/k8s-kubectl:v1.13.0-beta.1 \
  port-forward \
  --address=0.0.0.0 \
  -n complex-app \
  --pod-running-timeout=1h \
  deployment/complex-app-debug \
  8081:80
