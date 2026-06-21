#!/bin/bash


echo "SERVER PERFORMANCE REPORT"
echo "=============================="
#CPU
echo "CPU USAGE"

top -bn1 | grep "Cpu(s)"
#RAM
echo
echo "=============================="
echo "MEMORY USAGE"
free -h
#DISK
echo
echo "DISK USAGE"

df -h /
#NETWORK
