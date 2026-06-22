#!/bin/bash

SOURCE_DIR="./website/"

TARGET_DIR="/var/www/html/"

sudo rsync -av --delete \
$SOURCE_DIR \
$TARGET_DIR

echo "Deployment completed."