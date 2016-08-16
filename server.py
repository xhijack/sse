import json

from flask import Flask, render_template
from flask import request
from flask_sse import sse

app = Flask(__name__, static_url_path='/static')
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')


@app.route('/', methods=['GET'])
def index():
    """ render index
    :return:
    """
    return render_template("index.html")


@app.route('/send')
def send():
    """
        sending messagest to group
    :return:
    """
    sender = request.args.get('username')
    group = request.args.get('group')
    message = request.args.get('msg')

    sse.publish(
        {"message": request.args.get('msg'), 'sender': sender},
        type="chat",
        channel=group
    )

    return json.dumps({"status": "sent", "username": sender, "message": message})


@app.route('/register')
def register():
    """
        register new user and notify to group there is new user
    :return:
    """
    username = request.args.get('username')
    group = "group.{}".format(request.args.get('group'))

    sse.publish(
        {"username": username},
        type="register",
        channel=group
    )

    return json.dumps({"status": "registered", "username": username, "channel": group})

if __name__ == '__main__':
    app.run()
