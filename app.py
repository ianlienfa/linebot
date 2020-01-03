from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('m/MWj0OPtkTAZKNHe2ZbIpTSbE82Ql945fel1e359GeIylan5D3efACtp2GW7/R4K4Y4V29B3KCBXLA2loP4/uSUDX9WXbMMrb8j7XO5IP51TVnn19Ul911xX0blG4evD1K5HHiOJAb1I46Gm1gPUgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e40ee7f5a5a675374e66df4d28042490')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
