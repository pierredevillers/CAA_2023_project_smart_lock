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

################# Global variables##############
on_off = None
date = None

##### Acceleration (x,y,z) ##############
imu0 = imu.IMU()


################# Initial set up############
# Labels
ALERT = M5Label('ALARM', x=105, y=13, color=0x000, font=FONT_MONT_30, parent=None)
label2 = M5Label('label2', x=138, y=96, color=0x000, font=FONT_MONT_14, parent=None)
today_label = M5Label('today_label', x=76, y=54, color=0x000, font=FONT_MONT_14, parent=None)

# Buttons
verif = M5Btn(text='OK', x=125, y=52, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)


# Set today date
#ntp = ntptime.client(host='cn.pool.ntp.org', timezone=2)
#date = ntp.formatDatetime('-', ':') # variable date
#today_label.set_text(str(date))


# Cloud set up
project_id = "upbeat-voice-380815"
cloud_region = "europe-west1"
registry_id = "cloud_and_advanced_analytics"
device_id = "M5_core_2"
jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2ODMzNzU2NDAsImV4cCI6MTY4MzQzNTY0MCwiYXVkIjoidXBiZWF0LXZvaWNlLTM4MDgxNSJ9.UWvNAonTVctVREzP2R6XarioJqfnBs26QhsT3jGP6idBDo_tedrlzZWfXXWiaK9Ib9pByNbmkrha5azGgcJw3CsBEPP5IUjnewbkcY78wJOrxS7Q5RhQsK1RLxmU6mOumIvo-e8UeK46xrMN-TFWl-jo4RegowOD-X03NfL_4zCDVAoE5d5rkmkpuGo9jwc6v_L5XbNLeOUQGDr77PJOfuqCH04dYKnzPXC6RsZodxxAkXKmUSAhmH3iaMS8qcScBhH2Wq52ZGKiRgpYEvEaEO8odoh38-mkeqz5boDZ3QQVrcYLEfG67LNpuQzhRUsGAtbE3stfO8sB5tFQTnYsJY0GiRjDv6UnbW39onZXiW7FcRoE5UEYDeStlxOvBXWRia_yj0AQgBxJkV0aRYUL21ARiKt5k92NqqSjDqzr3oHXpVzeEjjaff_k542oInvhSVy6GlNal8C1lAvqTXOlptPQmFRYr2hkbdN0RWKVszpd-Fwv6obeOryZMuLmwi7MS9eogRmqGCMiBtiwfE2gu_uAhcWh8xJqItFeXyIxUpa_lqZdbMDenTrG6Nrx7u2E7Wd6Vk2i0XzqRuSAswdU1_ctCjKKfjnRnU0pfcItEPheJHmt27Ytu-Jh0BkoJI4b187Wp7wqons24GRmo6G5r8bIXi1KgpgYxES7kdHjHrw"
wifi_ssid="iot-unil"
wifi_password= "4u6uch4hpY9pJ2f9"

client_id = "projects/{}/locations/{}/registries/{}/devices/{}".format(
    project_id, cloud_region, registry_id, device_id
)

mqtt_topic = "/devices/{}/events".format(device_id)

mqtt_bridge_hostname='mqtt.googleapis.com'
mqtt_bridge_port = 8883
roots = urequests.get('https://pki.goog/roots.pem')

label0.set_text('Hello!')



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
    label0.set_text("Alarm date published, content : {}".format(date))
    wait_ms(1000)
    wait(3)
  except:
    label0.set_text('Error in connecting to mqtt')
    wait(3)    
    

# Set alarm method
def alarm_on():
  global on_off
  while on_off == 1:
    label2.set_hidden(False)
    screen.set_screen_bg_color(0x000000)
    verif.set_hidden(True)
    ALERT.set_hidden(False)
    ALERT.set_text('ALARM ON')
    label2.set_hidden(False)
    rgb.setColorAll(0x009900)
    ALERT.set_text_color(0x009900)
    label2.set_text_color(0xffffff)
    label2.set_text(str(imu0.acceleration[2]))
    if (imu0.acceleration[2]) < 1:
      rgb.setColorAll(0xff0000)
      ALERT.set_text('ALERT')
      ALERT.set_text_color(0xff0000)
      ntp = ntptime.client(host='cn.pool.ntp.org', timezone=2)
      global date
      date = ntp.formatDatetime('-', ':') # variable date
      today_label.set_text(str(date))
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
    label2.set_hidden(True)
    verif.set_hidden(False)
    screen.set_screen_bg_color(0xffffff)
    rgb.setColorAll(0xcc0000)
    verif.set_hidden(False)
    label2.set_hidden(True)
    ALERT.set_text('ALARM OFF')
    label2.set_text_color(0x000000)
    ALERT.set_text_color(0xcc0000)


def verif_pressed():
  global on_off
  ALERT.set_text('ALARM')
  ALERT.set_text_color(0x000000)
  label2.set_hidden(True)
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

label2.set_hidden(True)
verif.set_hidden(True)
lcd.qrcode('https://flow.m5stack.com/remote?id=833872650228203520', 85, 100, 150)

while True:
  if on_off == 0:
    alarm_off()
  elif on_off == 1:
    alarm_on()
  wait_ms(2)




