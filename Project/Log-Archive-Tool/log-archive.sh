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

ARCHIVE_DIR="archive"

mkdir -p "$ARCHIVE_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

ARCHIVE_NAME="logs_archive_${TIMESTAMP}.tar.gz"

tar -czf "$ARCHIVE_DIR/$ARCHIVE_NAME" "$LOG_DIR"

echo $ARCHIVE_NAME

echo
echo "Archive created!"

echo "$ARCHIVE_DIR/$ARCHIVE_NAME"

