# Flask SSE and Raspiberry Pi Sensors

Let make a backend to push sensor data from server to clients using Flask SSE. SSE is Server-Sent Events.

```text
+--------+                   +--------+
|        |<-- SSE Request ---|        |
| Server |-- SSE Response -->| Client |
|        |-- SSE Response -->|        |
|        |-- SSE Response -->|        |
+--------+                   +--------+
```

Install Flask library into your Raspberry Pi.

```shell
sudo pip3 install flask
```

## Ultrasonic Distance Sensor

Please look at server-hcsr04.py.

- Raspberry Pi Zero WH
- Grove Ultrasonic Distance Sensor
  - Connect VCC on sensor to 5V on Raspberry Pi.
  - Connect GND on sensor to GND on Raspberry Pi.
  - Connect SIG on sensor to GPIO17(11) on Raspberry Pi.

```shell
python3 server-hcsr04.py
```

Then accessing to Raspberry Pi using curl. You can get the result that server push sensor data, Like a below.

```shell
curl "http://<raspberrypi>:5000/sse"
data: {"distance": "55.2"}
data: {"distance": "49.7"}
data: {"distance": "519.4"}
data: {"distance": "47.8"}
data: {"distance": "46.4"}
data: {"distance": "519.1"}
data: {"distance": "519.3"}
data: {"distance": "51.3"}
data: {"distance": "49.1"}
:
:
```

Or accessing `http://<raspberrypi>:5000/` using a browser.

## Passive Infrared Ray motion sensor

Please look at server-pir.py.

- Raspberry Pi Zero WH
- PIR Motion Sensor
  - Connect VCC on sensor to 3V3 on Raspberry Pi.
  - Connect GND on sensor to GND on Raspberry Pi.
  - Connect OUT on sensor to GPIO4 on Raspberry Pi.

```shell
python3 server-pir.py
```

Then accessing to Raspberry Pi using curl.

```shell
curl "http://<raspberrypi>:5000/sse"
data: {"motion": "True"}
data: {"motion": "True"}
data: {"motion": "False"}
data: {"motion": "False"}
data: {"motion": "False"}
:
:
```
