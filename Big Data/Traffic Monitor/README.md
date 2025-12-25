# Real-Time SQL Traffic Monitor
## Overview : 
This project demonstrates a Live Stream Processing pipeline. It simulates real-time website traffic, stores the data in a relational database, and visualizes live analytics through a web-based dashboard. This mimics how modern platforms monitor server health and user activity.

## Tools :
- <u>Python<u>: Used for the data simulation and the backend web server.
- <u>SQL (SQLite)<u>: Used for real-time data storage and complex aggregations (GROUP BY, AVG, COUNT).
- HTML: Designed a self-refreshing dashboard for live visualization.
- Flask: A micro-framework used to bridge the SQL database with the Web UI.
- Linux (Ubuntu): Managed processes, virtual environments, and system-level networking.

## Architecture : 
- The Producer (simulator.py): Generates random web traffic data (path, response time) and performs INSERT operations into the database every 0.5 seconds.
- The Storage (traffic.db): An SQLite database that maintains a persistent record of all incoming "streams."
- The Consumer (app.py): A Flask server that executes SQL aggregation queries every time the page is viewed or refreshed.
- The Frontend: A simple HTML interface that uses a meta-refresh tag to poll the server for the latest analytics every 2 seconds.

## Execution :
1. Setting up the environment :
```
    # Create the virtual environment
      python3 -m venv venv
    # Activate the environment
      source venv/bin/activate
    # Install dependencies
      pip install flask
```
2. Running the Pipeline : You will need two terminal tabs open simultaneously
```
    #terminal 1
    source venv/bin/activate
    python3 simulator.py
    #terminal 2
    source venv/bin/activate
    python3 app.py
```
3. Accessing the Insights : Open your browser and navigate to: ```http://127.0.0.1:5000```
4. SQL Logic :
```
    SELECT 
    page_path, 
    COUNT(*) as total_hits, 
    AVG(response_time_ms) as avg_latency 
    FROM web_logs 
    GROUP BY page_path;
```
