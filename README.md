# simple-qrcode-generator

A simple app that can create several types of qrcodes

## Dependencies

### PIP

~~~shell
pip install customtkinter qrcode pillow
~~~

or

~~~shell
pip install -r requirements.txt
~~~

## Usage

### Command-Line Arguments

Prints the version

~~~shell
.py --version
~~~

or

~~~shell
.py -v
~~~

### GUI

Regular QR-Code:

- Can create QR-Codes that go to things like URLs
or even just plaintext

WiFi QR-Code:

- Creates QR-Codes that contain the log-in for a WiFi network

Virtual Business Card:

- Creates QR-Codes that contain information about someone such as a name, email, phone number, etc.

Email QR-Codes:

- Creates QR-Codes that contain a template for an email

## Installing

### Linux

Sorry fellow linux users but this is all manual.

If there are better ways to install please let me know

~~~shell
# Make sure that .bin is on your $PATH
mkdir ~/.bin/

# Creates the bash script thats the python script
echo "python </path/to/main.py>" > ~/.bin/qr-code-gen

# Allows the bash script to be executed
chmod +x ~/.bin/qr-code-gen
~~~

### Windows

Download the corresponding release and run it

Is currently only available as a portable file

## To-Dos

- Support more types of QR-Codes
- Start working on a CLI for this
