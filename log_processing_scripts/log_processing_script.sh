#!/bin/bash


echo "timestamp,status,user,ip"

# Extract relevant login attempt details
grep -E "Failed password|Accepted password" auth.log | \
  sed -E 's/^(\S+ \S+ \S+) .* (Failed|Accepted) password for user ([a-zA-Z0-9_-]+) from ([0-9.]+).*/\1,\2,\3,\4/' | \
  awk -F',' '{print $1","$2","$3","$4}'