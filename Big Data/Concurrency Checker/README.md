# Distributed System Concurrency Checker
## Overview :
In large-scale Big Data environments, multiple processes often compete for the same resources (like a database or a file system). This project uses Formal Methods to mathematically prove that a distributed locking mechanism is free from Race Conditions and Deadlocks. Instead of traditional testing, which only checks specific cases, this project uses Model Checking to explore every possible execution path.

## Tools :
- <ins>Promela (Process Meta Language)</ins>: Used to model process behavior and non-deterministic interactions.
- <ins>SPIN Model Checker</ins>: The verification engine used to perform a full state-space search for errors.
- <ins>Assertion-Based Verification</ins>: Implementing safety properties to detect concurrent access violations.
- <ins>Linux (Ubuntu)</ins>: Compiled and executed the generated pan (Protocol Analyzer) verifier.

## Architecture :
- <ins>Shared Resource</ins>: A boolean lock representing access to a database.
- <ins>Global Observer</ins>: A critical_section_count variable used to detect if more than one process enters the restricted zone.
- <ins>Processes</ins>: Two active User proctypes attempting to read/write to the database simultaneously.
- <ins>The Mutex Protocol</ins>: An atomic check-and-set operation to ensure only one process can toggle the lock at a time.

## Setup and Execution :
1. Installation :
Ensure the SPIN model checker is installed on your Ubuntu system
```
sudo apt update
sudo apt install spin
```
2. Running a Simulation :
To see a random execution of the processes interacting
``` spin safety.pml```
3.  Exhaustive Model Verification :
To prove the system is safe under all possible timings
```
# 1. Generate the verifier source code (pan.c)
spin -a safety.pml

# 2. Compile the verifier
gcc -o pan pan.c

# 3. Execute the search
./pan
```
