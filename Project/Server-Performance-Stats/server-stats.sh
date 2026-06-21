#!/bin/bash


echo "SERVER PERFORMANCE REPORT"
echo "=============================="

echo "CPU USAGE"

top -bn1 | grep "Cpu(s)"
echo
echo "=============================="
echo "MEMORY USAGE"
free -h