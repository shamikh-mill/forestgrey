from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/designs')
def designs():
    return render_template('designs.html')


if __name__ == "__main__":
    app.run()


