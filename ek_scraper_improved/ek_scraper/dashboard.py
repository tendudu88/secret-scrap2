from flask import Flask, render_template_string
import psutil
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>ek-scraper Dashboard</title>
<style>
body {font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px;}
h1 {color: #333;}
.green {color: green; font-weight: bold;}
.yellow {color: orange;}
.red {color: red;}
table {border-collapse: collapse; width: 100%;}
th, td {border: 1px solid #ddd; padding: 8px; text-align: left;}
th {background-color: #f2f2f2;}
</style>
</head>
<body>
<h1>ek-scraper Monitoring</h1>
<p><strong>CPU Auslastung:</strong> {{ cpu }}% | <strong>RAM verfügbar:</strong> {{ ram }} MB</p>
<h2>Laufende Scraper-Prozesse</h2>
<table>
<tr><th>Name</th><th>Status</th><th>CPU</th><th>Letzter Lauf</th></tr>
{% for s in scrapers %}
<tr>
<td>{{ s.name }}</td>
<td class="{{ s.status_class }}">{{ s.status }}</td>
<td>{{ s.cpu }}%</td>
<td>{{ s.last_run }}</td>
</tr>
{% endfor %}
</table>
</body>
</html>
"""

@app.route("/")
def dashboard():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'cpu_percent']):
        cmd = ' '.join(proc.info['cmdline'] or [])
        if 'ek-scraper' in cmd or 'dashboard' in cmd:
            processes.append({
                "name": proc.info['name'],
                "status": "running",
                "status_class": "green",
                "cpu": round(proc.info['cpu_percent'], 1),
                "last_run": datetime.now().strftime("%H:%M:%S")
            })
    
    return render_template_string(HTML, 
                                  cpu=psutil.cpu_percent(),
                                  ram=round(psutil.virtual_memory().available / (1024**2)),
                                  scrapers=processes or [{"name":"Kein Scraper aktiv", "status":"inactive", "status_class":"yellow", "cpu":0, "last_run":"-"}])

if __name__ == "__main__":
    print("Dashboard läuft auf http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
