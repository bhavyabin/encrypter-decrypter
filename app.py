from flask import Flask,render_template,request
from cryptography.fernet import Fernet
import textwrap
from flask_json import FlaskJSON, JsonError, json_response
from dotenv import dotenv_values

config = dotenv_values(".env")
app = Flask(__name__)
json = FlaskJSON(app)
wrapper = textwrap.TextWrapper(width=22)



@app.route("/",methods=["GET","POST"])
def encrypt_decrypt():
    if request.method == "POST":
        print("posted")
        state = request.form["state"]
        message = request.form["message"]
        f = Fernet(open("secret.key","rb+").read())

        if state == "encrypt":
            encoded_message = message.encode()
            message = f.encrypt(encoded_message)
            message = message.decode("ascii")
        else:
            decrypted_message = f.decrypt(message)
            message = decrypted_message.decode()

        message = "\n".join(wrapper.wrap(message))

        return render_template("index.html", main_val=f"{message}")
    else:
        return render_template("index.html")

@app.route("/api",methods=["POST"])
def api_encrypt_decrypt():
    data = request.get_json(force=True)
    try:
        state = data["state"]
        message = data["message"]

        f = Fernet(open(config["KEY"]))

        if state == "encrypt":
            encoded_message = message.encode()
            message = f.encrypt(encoded_message)
            message = message.decode("ascii")
        else:
            message = f.decrypt(message)
            message = message.decode("ascii")

    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')

    return json_response(message=message,state=state)



if __name__ == "__main__":
    app.run(debug=True)

