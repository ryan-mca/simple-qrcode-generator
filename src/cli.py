"""Handles the CLI stuff
"""
# --- Imports ---
from getpass import getpass
from qr_logic import gen_wifi_qr_code, gen_email_qr_code, gen_reg_qr_code, gen_vcard_qr_code

# --- Functions ---
def reg_qr():
    """asks the user for a string and creates a QR-Code
    """
    # Asks the user for the string
    print("What would you like to encode?")
    print("Can be any text, including URLs")
    text = input("Text: ")

    # Creates the QR-Code
    gen_reg_qr_code(text)
    exit(1)

def wifi_qr():
    """Asks the user for the security type, SSID, and password for the WiFi network
    """
    # Asks the user for security type
    # Converts the type to uppercase
    print("What's the security type of the network?")
    print("WEP\nWPA/WPA2\nNone")
    sec_type = input("Type out the security type: ").upper()

    # Gets the SSID
    print("What's the SSID (name) of the network?")
    ssid = input("SSID: ")

    # Gets the users password using the getpass library
    print("Finally, what's the password of the network?")
    passwd = getpass()

    gen_wifi_qr_code(ssid, passwd, sec_type)
    exit(1)

def email_qr_code():
    """Creates a template for an email
    """
    # Asks the user for the recipient
    rec = input("Recipient email: ")

    # Asks the user for a CC email
    cc = input("CC email (blank if none): ")

    # Asks the user for a BCC email
    bcc = input("BCC email (blank if none): ")

    # Asks the user for a subject
    subject = input("Subject: ")

    # Asks the user for the body of the email
    body = input("Body: ")

    gen_email_qr_code(rec, cc, bcc, subject, body)
    exit(1)

def vcard_qr():
    """Creates a virtual business card
    """
    # Asks the user for their name
    name = input("Name: ")

    # Asks the user for their company
    company = input("Company: ")

    # Asks the user for their phone number
    number = input("Phone Number: ")

    # Asks the user for their email
    email = input("Email: ")

    # Asks the user for their website
    website = input("Website: ")

    gen_vcard_qr_code(name, company, number, email, website)
    exit(1)
