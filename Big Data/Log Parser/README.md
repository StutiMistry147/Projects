# High-Performance Big Data Log Parser
## Overview : 
This project is a high-speed data pipeline designed to process massive server logs (5M+ lines) efficiently. It demonstrates the "right tool for the right job" philosophy in Big Data Engineering by using C++ for low-level data extraction and Python for high-level data analysis.

## Tools : 
- Linux (Ubuntu): Utilized system-level calls and the terminal environment
- C++: Implemented memory-mapping (mmap) for high-speed File I/O.
- Python: Used Pandas for data aggregation and statistical analysis.
- Big Data Concepts: Serialization/Deserialization (SerDe), Memory Management, and Data Pipelines.

## Architecture : 
- Ingestion Layer: A Python generator creates simulated Apache-style access logs.
- Processing Layer (The Engine): A C++ program maps the log file directly into virtual memory. It scans the memory address space for specific - HTTP status codes (e.g., 404) and extracts the associated IP addresses.
- Analysis Layer: A Python script reads the refined data (CSV) and performs a "Top N" frequency analysis to identify potential security threats or broken links.

## How To Run : 
1. _Generate the data_:
   ```python3 gen_logs.py```
2. _Compile the high-performance parser_ :
   ```g++ -O3 parser.cpp -o parser```
3.  _Execute the pipeline_ : 
   ```./parser && python3 analyzer.py```
