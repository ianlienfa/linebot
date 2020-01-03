from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('m/MWj0OPtkTAZKNHe2ZbIpTSbE82Ql945fel1e359GeIylan5D3efACtp2GW7/R4K4Y4V29B3KCBXLA2loP4/uSUDX9WXbMMrb8j7XO5IP51TVnn19Ul911xX0blG4evD1K5HHiOJAb1I46Gm1gPUgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e40ee7f5a5a675374e66df4d28042490')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()