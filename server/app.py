from flask import Flask, render_template
from brute import bruteforce

app = Flask(__name__)
app.register_blueprint(bruteforce)


@app.route('/')
def index():
    return render_template('index.html.j2')


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()
