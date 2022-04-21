import requests
import os
from flask import Flask, request

rasa_url = os.environ.get("RASA_URL")
chatwoot_url = os.environ.get("CHATWOOT_URL")
chatwoot_bot_token = os.environ.get("CHATWOOT_BOT_TOKEN")
rasa_channel = os.environ.get("RASA_CHANNEL")
rasa_jwt_token = os.environ.get("RASA_JWT_TOKEN")


def send_to_bot(sender, message):
    data = {"sender": sender, "message": message}
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    r = requests.post(
        f"{rasa_url}/webhooks/{rasa_channel}/webhook?token={rasa_jwt_token}",
        json=data,
        headers=headers,
    )
    return r.json()[0]["text"]


def send_to_chatwoot(account, conversation, message):
    data = {"content": message}
    url = f"{chatwoot_url}/api/v1/accounts/{account}/conversations/{conversation}/messages"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api_access_token": f"{chatwoot_bot_token}",
    }

    r = requests.post(url, json=data, headers=headers)
    return r.json()


app = Flask(__name__)


@app.route("/", methods=["POST"])
def rasa():
    data = request.get_json()
    message_type = data["message_type"]
    message = data["content"]
    conversation = data["conversation"]["id"]
    contact = data["sender"]["id"]
    account = data["account"]["id"]
    create_message = None

    if message_type == "incoming":
        bot_response = send_to_bot(contact, message)
        create_message = send_to_chatwoot(account, conversation, bot_response)
    return create_message


if __name__ == "__main__":
    app.run(debug=1)
