<h1 align="center">Smart Lock 2.0 – the future of security</h1>
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Université_de_Lausanne.svg/1280px-Logo_Université_de_Lausanne.svg.png" width="250" height="100"/> <br>
 </p>
Team : Volkswagen 
<br>
Team members : Vanja Hug, Feryel Ben Rhaiem, and Pierre Devillers
 
#### This github repository contains the following folders:
* **M5 Flow code** : python code to implement on the device in the M5 flow interface. 
* **Google Functions** : python code to implement in a Google function on Google cloud platform

## 🚧   Project Description  
As part of Cloud and Advanced Analytics class, we designed **The Smart Lock 2.0** is a tamper detection device that sends an alert, as well as the location to your phone via SMS and triggers an alarm if someone attempts to move your belongings without your permission. This device is perfect for safety-conscious people who want to protect their valuable items.

## 🤔   Methodology 
We used the already existing sensors implemented in the M5 Core 2 device, completed with a GPS Unit. We decided to define the alarm trigger by measuring the acceleration of the device on the Z-axis (vertical acceleration). We implemented different interfaces regarding the state of the device (Welcome page, Alarm on, Alarm triggered, Alarm off). A QR code that is shown when the Smart Lock 2.0 is switched on can be scanned and this will show two buttons (Alarm on, Alarm off) on the mobile phone. When the "Alarm On" button is pressed, the IoT is switched into alarm mode and generates an alarm when the device is moved (e.g. in case of attempted theft). An SMS is also sent directly to the owner of the Smart Lock 2.0. This SMS contains the current location and that an alarm has been triggered. The Smart Lock 2.0 can only be switched off by first pressing the "OFF" button on the mobile phone and then the “OK” button that displays on the IoT itself.

## 🚀   Deployment 
After establishing the connection between the device and the Google Cloud Platform (not possible anymore), you need to enter all the necessary information in the main code in python with identifiers, passwords, jwt, and wi-fi setup. Once this done, it is necessary to activate a Twillio account and modify the google cloud function with the needed ids and phone numbers. 

## ▶️   Video  
Click 👉 [here](https://clipchamp.com/watch/HQYIweiTWP3) to see the video. 
