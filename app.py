from flask import Flask, render_template, render_template_string, session, request
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = "{i_like_your_skill}"


@app.route("/")
def index():
    session['flag'] = "HTBSRMIST{THIS_IS_THE_FLAG}"
    return render_template("index.html")

@app.route("/plaintext", methods=['POST', 'GET'])
def plaintext():
    string = request.form['encrypted_string']
    

    string = string.encode("ascii")
    plain_string = base64.b64decode(string)
    plain_string = plain_string.decode("ascii")

    # Vulnerable to SSTI

    template = "<h1>PLAINTEXT: {}</h1>".format(plain_string)
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
