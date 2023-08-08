from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' :1,
    'title' :'Data Analyst',
    'location' :'bengaluru',
    'salary' :'Rs,12,00,000'
  },

   {
    'id' :2,
    'title' :'Data Scientist',
    'location' :'Hydrabad',
    'salary' :'Rs,15,00,000'
  },

   {
    'id' :3,
    'title' :'Frontent Engineer',
    'location' :'Noida',
    'salary' :'Rs,15,00,000'
  },

   {
    'id' :4,
    'title' :'Backend Engineer',
    'location' :'Chennai',
    'salary' :'Rs,20,00,000'
  }
]


@app.route("/")
def Hello_Engineeringbrain():
    return render_template('home.html',
                          jobs=JOBS,
                          company_name="Accenture")
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)