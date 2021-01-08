import config
import websocket, json
def on_open(ws):
    print('opened')
    auth_data={
        'action':'authenticate',
        'data':{'key_id':config.api_key, 'secret_key':config.secret_key}
    }
    ws.send(json.dumps(auth_data))

    channel_data={

    }
    listen_message={"action": "listen","data": {"streams": ["T.TSLA",'T.AAPL','T.BTC'] }}
    ws.send(json.dumps(listen_message))
def on_message(ws, message):
    print('receipt')
    print(message)
socket="wss://data.alpaca.markets/stream"
ws=websocket.WebSocketApp(socket,on_open=on_open, on_message=on_message)
ws.run_forever()
#{"action": "authenticate", "data": {"key_id": "PK6LSEON7GI2M843HE7X",  "secret_key": "SIM7FLtE3DzMzZtKxHRJYZjL7SrZRE9iXEGrYT7V"}}

#{"action": "listen","data": {"streams": ["T.SPY"] }}