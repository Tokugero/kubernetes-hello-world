from flask import Flask, Response
import os
import psycopg2

app = Flask(__name__)
query = ("select * from actor order by random() limit 5;")
host = os.getenv("host")
password = os.getenv("PSQL_PASSWORD")
user = os.getenv("PSQL_USERNAME")
dbname = os.getenv("PSQL_DBNAME")

print(host)
print(user)
print(dbname)

def callpsql():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port="5432")
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

@app.route('/')
def index():
    response = callpsql()
    print("Getting some juicy logs")
    results = "I've sold to these famous people from server "+os.getenv("DYNO")+": <br>\n"
    for row in response:
        results = results+"<br>\n"+str(row[1])+"\t"+str(row[2])
    return results 

@app.route('/health')
def health():
    f = open("/tmp/healthy", "r")
    print(f)
    health = f.readline().rstrip()
    resp = Response(health)
    if health != "healthy":
        resp.status=500
    resp.headers['health-check'] = health
    return resp 

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
