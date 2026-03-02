from flask import Flask, render_template_string
import RPi.GPIO as GPIO

app = Flask(__name__)

# GPIO Pins
LED1 = 17
LED2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

led1_state = False
led2_state = False

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Two LED Control</title>
</head>
<body style="text-align:center; margin-top:100px;">
    <h1>Raspberry Pi - Two LED Control</h1>

    <h2>LED 1 is {{ led1 }}</h2>
    <a href="/toggle1">
        <button style="padding:15px 30px; font-size:18px;">Toggle LED 1</button>
    </a>

    <br><br>

    <h2>LED 2 is {{ led2 }}</h2>
    <a href="/toggle2">
        <button style="padding:15px 30px; font-size:18px;">Toggle LED 2</button>
    </a>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_PAGE,
        led1="ON" if led1_state else "OFF",
        led2="ON" if led2_state else "OFF"
    )

@app.route('/toggle1')
def toggle1():
    global led1_state
    led1_state = not led1_state
    GPIO.output(LED1, led1_state)
    return home()

@app.route('/toggle2')
def toggle2():
    global led2_state
    led2_state = not led2_state
    GPIO.output(LED2, led2_state)
    return home()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
