#!/bin/bash
sqlite3 network_data.db <<EOF
CREATE TABLE traffic (
    timestamp REAL,
    inter_arrival REAL,
    size INTEGER
);
.mode csv
.import network_traffic.csv traffic
.quit
EOF
echo "Data imported to SQL."
