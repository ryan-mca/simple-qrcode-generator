"""Holds all of the qrcode stuff
"""
# --- Imports ---
import qrcode

# --- Functions ---
def gen_wifi_qr_code(SSID,PASSWD,SEC_TYPE):
    """WIP. Generates a WiFi QR-Code

    Args:
        SSID (String): The SSID of the WiFi network
        PASSWD (String): The password of the WiFi network
        SEC_TYPE (String): The security type. Can be WEP, WPA or None
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )

    wifi_data = f"WIFI:T:{SEC_TYPE};S:{SSID};P:{PASSWD}"

    qr.add_data(wifi_data)

    qrcode.make()
    img = qr.make_image()

    img.save(f'{SSID}.png')

def gen_reg_qr_code(text):
    """Generates the users input

    Args:
        text (String): Holds the users input
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )

    qr.add_data(text)
    qrcode.make()

    img = qr.make_image()
    img.save("regular_qrcode.png")

def gen_vcard_qr_code(NAME, COMPANY, PHONE, EMAIL, URL):
    """Creates a QR-Code for a virtual business card

    Args:
        NAME (String): The users name
        COMPANY (String): The users company
        PHONE (String): The users phone number
        EMAIL (String): The user email address
        URL (String): The users website
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )

    vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nN:{NAME}\nORG{COMPANY}\nTEL:{PHONE}\nEMAIL:{EMAIL}\nURL:{URL}\nEND:VCARD"

    qr.add_data(vcard_data)
    qrcode.make()

    img = qr.make_image()
    img.save("VCard-QR-Code.png")

def gen_email_qr_code(RECIPIENT, SUBJECT, BODY):
    """Creates a QR-Code for an email

    Args:
        RECIPIENT (String): The recieving email address
        SUBJECT (String): The emails subject
        BODY (String): The emails body
    """
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )

    email_data = f"MATMSG:TO:{RECIPIENT};SUB:{SUBJECT};BODY:{BODY};;"

    qr.add_data(email_data)
    qrcode.make()

    img = qr.make_image()
    img.save("EMail-QR-COde.png")
    