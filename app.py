from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Bengaluru',
  'salary': 'Rs. 10,50,000'
}, {
  'id': 2,
  'title': 'Data Engineer',
  'location': 'Delhi',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  'salary': 'Rs. 12,50,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Californa',
  'salary': '$ 120,000'
}]


@app.route("/")
def hello():
  return render_template('Home.html', jobs=JOBS, c_name="JOBS")


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
