# Stochastic Network Congestion Simulator
## Overview 
This project involves developing a formal prototype of a High-Performance Network Congestion Simulator using C++, SQL, Python, and the SPIN Model Checker. The system is designed as a Stochastic Data Pipeline, modeling real-world "bursty" network traffic where packet arrivals follow a Poisson distribution.
The primary challenge of this project was validating that a low-level, high-speed C++ engine correctly adheres to mathematical stochastic models while ensuring the system's buffer management logic is formally verified to prevent deadlocks during extreme traffic spikes.

## Specification 
The simulator operates across three stages of data maturity:
- <ins>Generation Stage</ins>: Produces high-volume synthetic traffic using an Exponential Distribution for inter-arrival times.
- <ins>Verification Stage</ins>: Uses Promela to prove that the "Drop Policy" and "Buffer Consumption" logic is safe and liveness-compliant.
- <ins>Analysis Stage</ins>: Performs Time-Series Analysis on millions of records to identify congestion patterns and throughput volatility.

## Architecture
- <ins>Traffic Engine (C++)</ins>: Acts as the data producer, using stochastic differential logic($t = -\frac{\ln(U)}{\lambda}$) to generate realistic packet timestamps.
- <ins>Formal Model (Promela)</ins>: Models the producer-consumer relationship between the network line and the router buffer to ensure no system hangs occur when the buffer is full.
- <ins>Storage Layer (SQL)</ins>: A structured repository that utilizes SQLite to manage "Big Data" volumes, allowing for rapid querying and indexing of traffic logs.
- <ins>Analytics Engine (Python)</ins>: The master observer, utilizing Pandas and Seaborn to perform statistical validation and plot network throughput over time
