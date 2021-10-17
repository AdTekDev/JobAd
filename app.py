from flask import Flask , render_template

app = Flask(__name__ , template_folder='views')

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/jobs")
def jobs():
    jobs = [
        { "title": "IT Admin", "describe" : "Fullstack Skills !" } ,
        { "title": "IT DevOps", "describe" : "Fullstack Skills !" } ,
    ]
    return render_template('jobs.html', jobs=jobs)

if __name__ == "__main__":
    app.run()

