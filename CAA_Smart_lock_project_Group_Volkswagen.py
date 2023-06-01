from m5stack import *
from m5stack_ui import *
from uiflow import *
import imu
import time
from m5mqtt import M5mqtt
import urequests
import machine
import ntptime
import unit

remoteInit()


################# Initial Screen #################

# Initialize the M5Screen object and set the screen background color
screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

# Initialize the GPS unit
gps_0 = unit.get(unit.GPS, unit.PORTC)

# Definition of UI Elements 
#Labels
label0 = M5Label('label0', x=101, y=88, color=0xFFFFFF, font=FONT_MONT_14, parent=None)
label0.set_align(ALIGN_CENTER, x=0, y=0, ref=screen.obj)
ALERT = M5Label('ALARM', x=105, y=13, color=0x000, font=FONT_MONT_30, parent=None)
ALERT.set_align(ALIGN_IN_TOP_RIGHT, x=0, y=0, ref=screen.obj)

#Images
image0 = M5Img("res/default.png", x=210, y=129, parent=None)
image1 = M5Img("res/default.png", x=210, y=129, parent=None)
image3 = M5Img("res/default.png", x=210, y=129, parent=None)

# Buttons
verif = M5Btn(text='OK', x=125, y=40, w=80, h=45, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
verif.set_hidden(True)

################# Global variables##############

on_off = None
date = None
latitude = None
longitude = None
imu0 = imu.IMU() # Acceleration as (x,y,z)

################# Initial set up #################

# Cloud setup variables
project_id = ""
cloud_region = ""
registry_id = ""
device_id = ""
jwt = ''
wifi_ssid = ""
wifi_password = ""

# MQTT setup variables
client_id = "projects/{}/locations/{}/registries/{}/devices/{}".format(
    project_id, cloud_region, registry_id, device_id
)

mqtt_topic = "/devices/{}/events".format(device_id)

mqtt_bridge_hostname = 'mqtt.googleapis.com'
mqtt_bridge_port = 8883
roots = urequests.get('https://pki.goog/roots.pem')


################# Methods #################

# Function to send data to Google Cloud Platform (BigQuery)
def send_bigquery():
    try:
        # Create M5mqtt client and connect to MQTT broker
        client = M5mqtt(
            client_id,
            mqtt_bridge_hostname,
            port=mqtt_bridge_port,
            user="unused",
            password=jwt,
            keepalive=300,
            ssl=True,
            ssl_params={"cert": roots}
        )

        client.start()

        # Send data to MQTT topic
        global date, latitude, longitude
        payload = "{{\"date\": \"{}\", \"latitude\": {}, \"longitude\": {}}}".format(date, latitude, longitude)
        client.publish(mqtt_topic, payload, qos=1)

        # Update label with alarm triggered message
        label0.set_text("Alarm triggered on {}".format(date))
        label0.set_align(ALIGN_CENTER, x=0, y=0, ref=screen.obj)
        wait_ms(1000)
        wait(3)

    except:
        # Handle connection error with MQTT
        label0.set_text('Error in connecting to mqtt')
        wait(3)

# Function to play the alarm sound
def ring():
    for count in range(3):
        # Play the WAV file with the speaker unit
        speaker.playWAV("res/mixkit-alarm-tone-996.wav", volume=6)
        wait(0.2)

# Function to turn on the alarm
def alarm_on():
    global on_off
    image3.set_hidden(True)
    while on_off == 1:
        # Definition of UI Elements 
        #Labels
        ALERT.set_hidden(False)
        ALERT.set_text('ALARM ON')
        ALERT.set_align(ALIGN_IN_TOP_MID, x=0, y=0, ref=screen.obj)
        label0.set_text("No alert detected")
        label0.set_align(ALIGN_CENTER, x=0, y=0, ref=screen.obj)
        
        #RGB Bar
        rgb.setColorAll(0x009900)

        #Images and Screens
        image0.set_hidden(False)
        image0.set_img_src("res/Scan to turn the alarm on! (2).png")
        image0.set_align(ALIGN_IN_LEFT_MID, x=0, y=0, ref=screen.obj)
        ALERT.set_text_color(0x009900)
        screen.set_screen_bg_color(0xffffff)

        #Buttons
        verif.set_hidden(True)
      
  
    # Check if the Z-axis acceleration is less than 1 (alert condition)
        if (imu0.acceleration[2]) < 1: #Alarm triggered
            # Definition of UI Elements 
            #RGB Bar
            rgb.setColorAll(0xff0000)

            #Labels
            ALERT.set_text('ALERT')
            ALERT.set_align(ALIGN_IN_TOP_MID, x=0, y=0, ref=screen.obj)
            ALERT.set_text_color(0xff0000)

            # Call the ring function to play the alarm sound
            ring()

            #Images
            image0.set_img_src("res/Scan to turn the alarm on! (1).png")
            image0.set_align(ALIGN_IN_LEFT_MID, x=0, y=0, ref=screen.obj)

            # Get current date, longitude, and latitude
            ntp = ntptime.client(host='cn.pool.ntp.org', timezone=2)
            global date, longitude, latitude
            date = ntp.formatDatetime('-', ':')  # variable date
            longitude = gps_0.longitude_decimal
            latitude = gps_0.latitude_decimal

            # Send data to Google Cloud Platform (BigQuery)
            send_bigquery()

# Function to turn off the alarm
def alarm_off():
    global on_off
    while on_off == 0:
        # Definition of UI Elements 
        #Buttons
        verif.set_hidden(False)

        #Screen
        screen.set_screen_bg_color(0xffffff)

        #RGB Bar
        rgb.setColorAll(0xcc0000)

        #Labels
        ALERT.set_text('ALARM OFF')
        ALERT.set_hidden(False)
        ALERT.set_align(ALIGN_IN_TOP_MID, x=0, y=0, ref=screen.obj)
        ALERT.set_text_color(0xcc0000)
        wait(0.2)
        ALERT.set_hidden(True)

# Callback function for the verification button press event
def verif_pressed():
    image3.set_hidden(False)
    global on_off
    ALERT.set_text('ALARM')
    ALERT.set_text_color(0x000000)
    ALERT.set_align(ALIGN_IN_TOP_RIGHT, x=0, y=0, ref=screen.obj)
    verif.set_hidden(True)
    rgb.setColorAll(0x000000)
    image0.set_hidden(True)
    # Generate the QR code on the LCD screen
    lcd.qrcode('https://flow.m5stack.com/remote?id=833872650228203520', 0, 100, 150)
    on_off = 2
    pass


verif.pressed(verif_pressed)
image3.set_img_src("res/text2.png")
image3.set_align(ALIGN_IN_TOP_LEFT, x=0, y=0, ref=screen.obj)


def button_alarm_off_callback():
    global on_off, alarm_off, alarm_on
    on_off = 0


def button_alarm_on_callback():
    global on_off, alarm_off, alarm_on
    on_off = 1



verif.set_hidden(True)
lcd.qrcode('https://flow.m5stack.com/remote?id=833872650228203520', 0, 100, 150)
image1.set_img_src("res/robi.png")
image1.set_align(ALIGN_IN_BOTTOM_RIGHT, x=0, y=0, ref=screen.obj)

while True:
    # Check the value of the on_off variable and call the corresponding function
    if on_off == 0:
        alarm_off()
    elif on_off == 1:  
        alarm_on()
    wait_ms(2)
