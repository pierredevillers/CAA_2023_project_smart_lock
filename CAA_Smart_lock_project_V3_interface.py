from m5stack import *
from m5stack_ui import *
from uiflow import *
import imu
import time
from m5ui import *
from m5mqtt import M5mqtt
import urequests
import machine
import ntptime

remoteInit()

############################################### Initial Screen ##
screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

################# Definition of Butttons & labels & images ##############
label0 = M5Label('label0', x=101, y=88, color=0xFFFFFF, font=FONT_MONT_14, parent=None)
label0.set_align(ALIGN_CENTER, x=0, y=0, ref=screen.obj)

################# Global variables##############
on_off = None
date = None

##### Acceleration (x,y,z) ##############
imu0 = imu.IMU()

################# Initial set up############
# Labels
ALERT = M5Label('ALARM', x=105, y=13, color=0x000, font=FONT_MONT_30, parent=None)

# Buttons
verif = M5Btn(text='OK', x=125, y=52, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

verif.set_hidden(True)

# Set today date
# ntp = ntptime.client(host='cn.pool.ntp.org', timezone=2)
# date = ntp.formatDatetime('-', ':') # variable date
# today_label.set_text(str(date))


# Cloud set up
project_id = "upbeat-voice-380815"
cloud_region = "europe-west1"
registry_id = "cloud_and_advanced_analytics"
device_id = "M5_core_2"
jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2ODQzMzk0MjUsImV4cCI6MTY4NDM5OTQyNSwiYXVkIjoidXBiZWF0LXZvaWNlLTM4MDgxNSJ9.fHVXrjetZeyYEtq2cT6ARuIXCy50YerY9ytpvTTJdlmQZwbVvmJksS0txFaKW8T1x_Hh3oGJI1Tp8kWOj8mjxN8USwNgRcUzahL0lb_lU7_xO2uZjUjBJHFqv3f5IIlwhKJcY3wMwSt9_DfW0CVXtn8N0G6sQnvWly1JC2Pv4VfpPqDsVKlAwJC7fJXVGEX72ySmteRv4fdJ9bIdB6mKXq0-v72-NW5jX918OtRgesRT4oacEJ5qUk6LLQYsrgwhB7tn2EurnEXf6-BBu5QsgeZDLaeUK0z3PKtwWIiMQglj8lFw-otsmq83_4zYzKNkJjKHJnj5oeITb9PjfJFJrrqSrjFGyzUhrYiNtSZNu-HZ0wTTkSoBT-GY8HPXkkQ-UCsmkvmRJqkoUm8feTPcrzXYrXAaPRhgvS8ANZwA7ID7y95lXlVU262yVU9MV97A6B93Hfx7ucFgu_Dyh89zWpZQtW0svxcND76IM_gLpmXGv0kntIJUwkd9S3W8sgjkyouTaznul27ev8nqRTSe1h8mauZLhvMfAi7kZb-6TqH8yI8cJgXR-4iSNtDNlzbpVWoQWNFN_BMBizH7JiVYo4CrK5V_N34JjwqyBOG11KBj-5Lhfd-cqHQLHx3VbRHKqhPos1-D-uVCSUVY4GNzC7jzTOAb_NjRiIZp6StNR8c"
wifi_ssid = "iot_unil"
wifi_password = "4u6uch4hpY9pJ2f9"

client_id = "projects/{}/locations/{}/registries/{}/devices/{}".format(
    project_id, cloud_region, registry_id, device_id
)

mqtt_topic = "/devices/{}/events".format(device_id)

mqtt_bridge_hostname = 'mqtt.googleapis.com'
mqtt_bridge_port = 8883
roots = urequests.get('https://pki.goog/roots.pem')


############################################### Methods

# What to send to GCP
def send_bigquery():
    try:
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

        global date
        payload = "{}".format(date)
        client.publish(mqtt_topic, payload, qos=1)
        label0.set_text("Alarm triggered on {}".format(date))
        label0.set_align(ALIGN_CENTER, x=0, y=0, ref=screen.obj)
        wait_ms(1000)
        wait(3)
    except:
        label0.set_text('Error in connecting to mqtt')
        wait(3)

    # Set alarm method


def alarm_on():
    global on_off
    while on_off == 1:

        screen.set_screen_bg_color(0x000000)
        verif.set_hidden(True)
        ALERT.set_hidden(False)
        ALERT.set_text('ALARM ON')
        ALERT.set_align(ALIGN_IN_TOP_MID, x=0, y=0, ref=screen.obj)
        label0.set_text("No alert detected")
        label0.set_align(ALIGN_CENTER, x=0, y=0, ref=screen.obj)

        rgb.setColorAll(0x009900)
        ALERT.set_text_color(0x009900)

        if (imu0.acceleration[2]) < 1:
            rgb.setColorAll(0xff0000)
            ALERT.set_text('ALERT')
            ALERT.set_align(ALIGN_IN_TOP_MID, x=0, y=0, ref=screen.obj)
            ALERT.set_text_color(0xff0000)
            ntp = ntptime.client(host='cn.pool.ntp.org', timezone=2)
            global date
            date = ntp.formatDatetime('-', ':')  # variable date
            ring()
            send_bigquery()


def ring():
    for count in range(3):
        speaker.playWAV("res/mixkit-alarm-tone-996.wav", volume=6)
        wait(0.2)


# Describe this function...
def alarm_off():
    global on_off
    while on_off == 0:
        verif.set_hidden(False)
        screen.set_screen_bg_color(0xffffff)
        rgb.setColorAll(0xcc0000)
        verif.set_hidden(False)
        ALERT.set_text('ALARM OFF')
        ALERT.set_align(ALIGN_IN_TOP_MID, x=0, y=0, ref=screen.obj)
        ALERT.set_text_color(0xcc0000)


def verif_pressed():
    global on_off
    ALERT.set_text('ALARM')
    ALERT.set_text_color(0x000000)
    ALERT.set_align(ALIGN_IN_TOP_MID, x=0, y=0, ref=screen.obj)
    verif.set_hidden(True)
    rgb.setColorAll(0x000000)
    lcd.qrcode('https://flow.m5stack.com/remote?id=833872650228203520', 85, 100, 150)
    on_off = 2
    pass


verif.pressed(verif_pressed)


def button_alarm_off_callback():
    global on_off, alarm_off, alarm_on
    on_off = 0


def button_alarm_on_callback():
    global on_off, alarm_off, alarm_on
    on_off = 1


lcd.qrcode('https://flow.m5stack.com/remote?id=833872650228203520', 85, 100, 150)

while True:
    if on_off == 0:
        alarm_off()
    elif on_off == 1:
        alarm_on()
    wait_ms(2)