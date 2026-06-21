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
#top 5 CPU
echo
echo "TOP 5 CPU PROCESSES"

ps -eo pid,comm,%cpu --sort=-%cpu | head -6
#Top 5 mem process
echo
echo "TOP 5 MEMORY PROCESSES"

ps -eo pid,comm,%mem --sort=-%mem | head -6
#Uptime
echo
echo "SYSTEM UPTIME"

uptime