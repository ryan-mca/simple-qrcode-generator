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
