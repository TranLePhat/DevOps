#!/bin/bash

echo "LOG ARCHIVE TOOL"
echo

LOG_DIR=$1

if [ -z "$LOG_DIR" ]
then
    echo "Usage: ./log-archive.sh <log-directory>"
    exit 1
fi

echo "Selected Directory: $LOG_DIR"

if [ ! -d "$LOG_DIR" ]
then
    echo "Directory does not exist!"
    exit 1
fi