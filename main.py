from flask import Flask, render_template, redirect, request
from chatbot import predict_class, get_response, intents
import os

app = Flask(__name__)

app.config['SECRET__KEY'] = 'a_very_secretive_key_123456789'
IMG_FOLDER = os.path.join('assets', 'images')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


answer_list = []


@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    robot_img = os.path.join(app.config['UPLOAD_FOLDER'], 'robot.jpg')

    if request.method == "POST":

        message = request.form['message']
        ints = predict_class(message)
        res = get_response(ints, intents)
        answer_list.append(res)
        print(answer_list)
        if len(answer_list) > 5:
            answer_list.remove(answer_list[0])
        return render_template("chatbot.html", message=message, res=res, answer_list=answer_list, robot_img=robot_img)
    return render_template("chatbot.html", message="", answer_list=answer_list)


if __name__ == "__main__":
    app.run(debug=True)
