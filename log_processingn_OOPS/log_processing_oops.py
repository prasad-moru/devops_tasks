#!/usr/bin/env python3
import re
import csv
import sys
from datetime import datetime
from typing import List, Optional


class LogEntry:
    
    def __init__(self, timestamp: str, level: str, service: str, 
                 email: str, ip: Optional[str] = None):
        self.timestamp = timestamp
        self.level = level
        self.service = service
        self.email = email
        self.ip = ip if ip else "N/A"
    
    def to_csv_row(self) -> List[str]:
        return [self.timestamp, self.level, self.service, self.email, self.ip]
    
    def __lt__(self, other):
        if not isinstance(other, LogEntry):
            return NotImplemented
        return self.timestamp < other.timestamp


class LogProcessor:
    LOG_PATTERN = re.compile(
        r'\[([0-9-]+ [0-9:]+)\] \[(ERROR|WARN)\] \[([^]]+)\] '
        r'.*user ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
        r'(?: from ([0-9.]+))?.*'
    )
    
    def __init__(self, log_file_path: str):
        self.log_file_path = log_file_path
        self.entries = []
    def process(self) -> None:
        try:
            with open(self.log_file_path, 'r') as file:
                for line in file:
                    self._process_line(line.strip())
        except FileNotFoundError:
            print(f"Error: File {self.log_file_path} not found", file=sys.stderr)
            sys.exit(1)
    def _process_line(self, line: str) -> None:
        match = self.LOG_PATTERN.match(line)
        if match:
            timestamp, level, service, email, ip = match.groups()
            
            if level in ('ERROR', 'WARN'):
                entry = LogEntry(timestamp, level, service, email, ip)
                self.entries.append(entry)
    
    def write_csv(self, output_file=None) -> None:
        self.entries.sort()
        
        output = output_file if output_file else sys.stdout
        writer = csv.writer(output)
        
        writer.writerow(['timestamp', 'level', 'service', 'email', 'ip'])
        
        for entry in self.entries:
            writer.writerow(entry.to_csv_row())

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} sample.log", file=sys.stderr)
        sys.exit(1)
    
    log_file = sys.argv[1]
    processor = LogProcessor(log_file)
    processor.process()
    processor.write_csv()


if __name__ == "__main__":
    main()