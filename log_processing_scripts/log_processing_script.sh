#!/bin/bash

# Add CSV header
echo "timestamp,level,service,email,ip"

# Process log entries
grep -E '\[(ERROR|WARN)\]' sample.log | 
  sed -E 's/\[([0-9-]+ [0-9:]+)\] \[(ERROR|WARN)\] \[([^]]+)\] .* user ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})( from ([0-9.]+))?.*$/\1,\2,\3,\4,\6/g' |
  awk -F ',' '{
    gsub(/^\[|\]$/, "", $3);
    if ($5 == "") {
      print $1","$2","$3","$4",N/A"
    } else {
      print $1","$2","$3","$4","$5
    }
  }' |
  sort -t ',' -k1,1