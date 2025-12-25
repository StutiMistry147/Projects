from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

HTML_TEMPLATE = '''
<html>
    <head><title>Live Traffic</title><meta http-equiv="refresh" content="2"></head>
    <body>
        <h1>Real-Time Traffic Dashboard</h1>
        <table border="1">
            <tr><th>Page Path</th><th>Total Hits</th><th>Avg Latency (ms)</th></tr>
            {% for row in data %}
            <tr>
                <td>{{ row[0] }}</td><td>{{ row[1] }}</td><td>{{ row[2]|round(2) }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
</html>
'''

@app.route('/')
def index():
    conn = sqlite3.connect('traffic.db')
    cursor = conn.cursor()
    cursor.execute('SELECT page_path, COUNT(*), AVG(response_time_ms) FROM web_logs GROUP BY page_path')
    data = cursor.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


