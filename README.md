# IoT-desktop-app
IoT based Desktop Application using Python

This is simple LED controlled IoT Application where you will control LED through Desktop Application. Its a cloud based Application.
We use <a href="https://thingspeak.com">ThingSpeak</a> for cloud storage.


<b>Dependencies:</b>
 1. Tkinter (Which is pre-build)
 2. pyserial (For serial communication from python to arduino)
 3. requests (To communicate with ThingSpeak Cloud API)
 4. pyfirmata (To controll Arduino from Python)
 
 <b>Steps</b>
 1. You have to open an Account in <a href="https://thingspeak.com">ThingSpeak</a>.
 2. Setup LED in pin 12(OUTPUT) another one is GND.
 3. Choose PORT from your Arduino and put it in the code.
 4. In Arduino choose one lib file called <b>StandardFirmata</b>
 <img src="https://github.com/sayandeepmajumdar/iot-desktop-app/blob/master/standarfirmata.png">
 5. Upload that code to Arduino UNO. (This Lib will help to communicate between Python and Arduino)<br>
 6. Get your Write and Read API_KEY from <a href="https://thingspeak.com">ThingSpeak</a> account.<br>
 7. Get to your folder and run your code.
    <code>python gui.py</code>
 
 <b>Output:</b>
 <img src="https://github.com/sayandeepmajumdar/iot-desktop-app/blob/master/gui.png">
 
 Click on the On Off button and see the output.
 
 <b>Have Fun</b> !!!
 
 
