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
    wifi_data = f"WIFI:T:{SEC_TYPE};S:{SSID};P:{PASSWD}"

    img = qrcode.make(wifi_data)

    img.save(f"{SSID}_qr_code.png")
