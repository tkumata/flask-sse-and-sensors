# Flask SSE and Raspiberry Pi Sensors

Let make a backend to push sensor data from server to clients using Flask SSE.

```shell
sudo pip3 install flask
```

## Ultrasonic Distance Sensor

server-hcsr04.py

- Raspberry Pi Zero WH
- Grove Ultrasonic Distance Sensor
  - Connect VCC on sensor to 5V on Raspberry Pi.
  - Connect GND on sensor to GND on Raspberry Pi.
  - Connect SIG on sensor to GPIO17(11) on Raspberry Pi.

```python
python3 server-hcsr04.py
```

Then curl to Raspberry Pi.

```shell
curl "http://raspberrypi.local:5000/sse"
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

## Passive Infrared Ray motion sensor

server-pir.py

- Raspberry Pi Zero WH
- Grove PIR motion sensor
  - Connect VCC on sensor to 3V3 on Raspberry Pi.
  - Connect GND on sensor to GND on Raspberry Pi.
  - Connect SIG on sensor to GPIO17(11) on Raspberry Pi.

```python
python3 server-pir.py
```

Then curl to Raspberry Pi.

```shell
curl "http://raspberrypi.local:5000/sse"
data: {"motion": "True"}
data: {"motion": "True"}
data: {"motion": "False"}
data: {"motion": "False"}
data: {"motion": "False"}
:
:
```
