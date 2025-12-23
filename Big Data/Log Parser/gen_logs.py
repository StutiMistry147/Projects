import random
import time


# Sample data to make it look real
ips = ["192.168.1.1", "10.0.0.50", "172.16.0.5", "112.45.12.1"]
methods = ["GET", "POST", "DELETE", "PUT"]
resources = ["/index.html", "/api/login", "/images/logo.png", "/css/style.css"]
status_codes = [200, 404, 500, 301]


with open("access.log", "w") as f:
   for i in range(5000000):  # 1 million lines
       ip = random.choice(ips)
       dt = time.strftime("%d/%b/%Y:%H:%M:%S +0000")
       method = random.choice(methods)
       res = random.choice(resources)
       status = random.choice(status_codes)
       size = random.randint(100, 5000)
      
       # Standard Apache Log Format
       line = f'{ip} - - [{dt}] "{method} {res} HTTP/1.1" {status} {size}\n'
       f.write(line)


print("Generated access.log with 1 million lines.")

