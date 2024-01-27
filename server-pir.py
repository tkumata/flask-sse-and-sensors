from flask import Flask, make_response
from gpiozero import MonitorSensor
import json


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

pir = MonitorSensor(17)


@app.route("/sse")
def sse():
    resp = make_response()
    resp.headers["content-type"] = "text/event-stream"
    resp.response = sse_make()
    return resp


def sse_make():
    while True:
        data = {"motion": pir.motion_detected}  # True or False
        yield "data: {}\n\n".format(json.dumps(data))
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    pass
