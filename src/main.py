"""Handles the main customtkinter stuff
"""
# --- Imports ---
import argparse
import customtkinter as ctk
from qr_logic import gen_wifi_qr_code, gen_reg_qr_code, gen_vcard_qr_code, gen_email_qr_code
# Required to package to an exe
from sys import exit
# --- Constants ---
win = ctk.CTk()
VERSION = "1.2.1"

# --- CustomTkinter stuff ---
# Window settings
win.title("Simple QR-Code Generator")
win.geometry("500x350")
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

# Used in 'main()'
main_frame = ctk.CTkFrame(master=win)
cbox = ctk.CTkComboBox(master=main_frame, values=["Regular QR-Code", "WiFi QR-Code", "Business Card QR-Code", "Email QR-Code"],
                        font=("Helvetica", 11))

# Used in 'wifi_qr_code()'
wifi_qr_code_frame = ctk.CTkFrame(master=win)
#file_or_show_cbox = ctk.CTkComboBox(master=wifi_qr_code_frame, values=["Save to File", "Show"]) WIP

# Used in 'reg_qr_code()'
reg_qr_frame = ctk.CTkFrame(master=win)

# Used in 'vcard_qr_code()'
vcard_qr_frame = ctk.CTkFrame(master=win)

# Used in 'email_qr_code()'
email_qr_frame = ctk.CTkFrame(master=win)

# --- Functions ---
def main():
    """Runs the main window
    """
    parser = argparse.ArgumentParser(description="Creates Different types of QR-Codes")
    parser.add_argument("-v", "--version", help="Prints the version", action="store_true")
    args = parser.parse_args()
    if args.version:
        print(f"Current Version: {VERSION}")
        exit()

    cbox_select = ctk.CTkButton(master=main_frame, text="Select", command=cbox_logic)
    main_title = ctk.CTkLabel(master=main_frame, text="Simple QR-Code Generator",
                            font=("Helvetica", 24))

    exit_button = ctk.CTkButton(master=main_frame, text="Exit", command=exit, fg_color="red")

    main_title.pack(pady=12, padx=10)
    cbox.pack(pady=12, padx=10)
    cbox_select.pack(pady=1, padx=10)
    exit_button.pack(pady=50, padx=10)

    cbox.set("Pick QR-Code Type")

    main_frame.pack(pady=20, padx=60, fill="both", expand=True)

    win.mainloop()

def cbox_logic():
    """Checks the users choice and runs the respective function
    """
    choice = cbox.get()

    if choice == "WiFi QR-Code":
        main_frame.pack_forget()
        wifi_qr_code()
    elif choice == "Regular QR-Code":
        main_frame.pack_forget()
        reg_qr_code()
    elif choice == "Business Card QR-Code":
        main_frame.pack_forget()
        vcard_qr_code()
    elif choice == "Email QR-Code":
        main_frame.pack_forget()
        email_qr_code()

def reg_qr_code():
    """Shows all the reg_qr_code widgets
    """
    title = ctk.CTkLabel(master=reg_qr_frame, text="Regular QR-Code", font=("Helvetica", 24))
    text_input = ctk.CTkEntry(master=reg_qr_frame, placeholder_text="Text / URL")
    submit_button = ctk.CTkButton(master=reg_qr_frame, text="Generate", command=lambda: gen_reg_qr_code(text_input.get()))

    title.pack(pady=12, padx=10)
    text_input.pack(pady=12, padx=10)
    submit_button.pack(pady=12, padx=10)
    reg_qr_frame.pack(pady=20, padx=60, fill="both", expand=True)

def wifi_qr_code():
    """Shows all the wifi_qr_code widgets
    """
    sec_type_cbox = ctk.CTkComboBox(master=wifi_qr_code_frame, values=["WEP", "WPA", "None"])
    wifi_ssid_input = ctk.CTkEntry(master=wifi_qr_code_frame, placeholder_text="WiFi SSID")
    wifi_passwd_input = ctk.CTkEntry(master=wifi_qr_code_frame, placeholder_text="WiFi Password", show="*")
    wifi_qr_code_label = ctk.CTkLabel(master=wifi_qr_code_frame, text="WiFi QR-Code", font=("Helvetica", 24))
    gen_qr_button = ctk.CTkButton(master=wifi_qr_code_frame, text="Generate", command=lambda: gen_wifi_qr_code(wifi_ssid_input.get(), wifi_passwd_input.get(), sec_type_cbox.get()))

    wifi_qr_code_label.pack(pady=12, padx=10)
    wifi_ssid_input.pack(pady=6, padx=10)
    wifi_passwd_input.pack(pady=6, padx=10)
    sec_type_cbox.pack(pady=6, padx=10)
    gen_qr_button.pack(pady=12, padx=10)
    sec_type_cbox.set("Security Type")

    wifi_qr_code_frame.pack(pady=20, padx=60, fill="both", expand=True)

def vcard_qr_code():
    """Shows all the vcard_qr_code widgets
    """
    title = ctk.CTkLabel(master=vcard_qr_frame, text="Business Card", font=("Helvetica",24))
    name_entry = ctk.CTkEntry(master=vcard_qr_frame, placeholder_text="Your Name")
    company_entry = ctk.CTkEntry(master=vcard_qr_frame, placeholder_text="Your Company")
    phone_entry = ctk.CTkEntry(master=vcard_qr_frame, placeholder_text="Your Phone Number")
    email_entry = ctk.CTkEntry(master=vcard_qr_frame, placeholder_text="Your Email")
    url_entry = ctk.CTkEntry(master=vcard_qr_frame, placeholder_text="Your Website")
    submit_button = ctk.CTkButton(master=vcard_qr_frame, text="Generate",
    command=lambda: gen_vcard_qr_code(name_entry.get(), company_entry.get(), phone_entry.get(),
    email_entry.get(), url_entry.get()))

    title.pack(pady=6, padx=10)
    name_entry.pack(pady=6, padx=10)
    company_entry.pack(pady=6, padx=10)
    phone_entry.pack(pady=6, padx=10)
    email_entry.pack(pady=6, padx=10)
    url_entry.pack(pady=6, padx=10)
    submit_button.pack(pady=6, padx=10)

    vcard_qr_frame.pack(pady=20, padx=60, fill="both", expand=True)

def email_qr_code():
    """Shows all the email_qr_code widgets
    """
    title = ctk.CTkLabel(master=email_qr_frame, text="Calendar QR-Code", font=("Helvetica", 24))
    recipient = ctk.CTkEntry(master=email_qr_frame, placeholder_text="Recipient")
    cc = ctk.CTkEntry(master=email_qr_frame, placeholder_text="CC")
    bcc = ctk.CTkEntry(master=email_qr_frame, placeholder_text="BCC")
    subject = ctk.CTkEntry(master=email_qr_frame, placeholder_text="Subject")
    body = ctk.CTkEntry(master=email_qr_frame, placeholder_text="Body")
    submit = ctk.CTkButton(master=email_qr_frame, text="Generate", command=lambda: gen_email_qr_code(recipient.get(), cc.get(), bcc.get(),subject.get(), body.get()))

    title.pack(pady=6, padx=10)
    recipient.pack(pady=6, padx=10)
    cc.pack(pady=6, padx=10)
    bcc.pack(pady=6, padx=10)
    subject.pack(pady=6, padx=10)
    body.pack(pady=6, padx=10)
    submit.pack(pady=6, padx=10)
    
    email_qr_frame.pack(pady=20, padx=60, fill="both", expand=True)
    

if __name__ == "__main__":
    main()
