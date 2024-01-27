from flask import Flask, make_response, render_template
import json
import time
import RPi.GPIO as GPIO


GPIO_SIG = 17
GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


class UltSonicCtrl:
    def fetchDistance(self):
        GPIO.setup(GPIO_SIG, GPIO.OUT)  # type: ignore

        GPIO.output(GPIO_SIG, GPIO.LOW)  # type: ignore
        time.sleep(0.2)
        GPIO.output(GPIO_SIG, GPIO.HIGH)  # type: ignore
        time.sleep(0.5)
        GPIO.output(GPIO_SIG, GPIO.LOW)  # type: ignore
        start = time.time()
        stop = 0.00

        GPIO.setup(GPIO_SIG, GPIO.IN)  # type: ignore

        while GPIO.input(GPIO_SIG) == 0:  # type: ignore
            start = time.time()

        while GPIO.input(GPIO_SIG) == 1:  # type: ignore
            stop = time.time()

        return self.calcDistance(start, stop)

    def calcDistance(self, start, stop):
        elapsed = stop - start
        distance = elapsed * 34350
        distance = distance / 2
        return distance


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/sse")
def sse():
    resp = make_response()
    resp.headers["content-type"] = "text/event-stream"
    resp.response = sse_make()
    return resp


def sse_make():
    while True:
        distance = "%.1f" % ultsonic.fetchDistance()
        data = {"distance": distance}
        yield "data: {}\n\n".format(json.dumps(data))
        time.sleep(3)
    pass


ultsonic = UltSonicCtrl()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    pass
