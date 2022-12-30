"""Handles the main customtkinter stuff
"""
# --- Imports ---
import customtkinter as ctk
from qr_logic import gen_wifi_qr_code, gen_reg_qr_code

# --- Constants ---
win = ctk.CTk()

# --- Extra Variables ---
qr_type = None

# --- CustomTkinter stuff ---
# Window settings
win.title("Simple QR-Code Generator")
win.geometry("500x350")
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

# Used in 'main()'
main_frame = ctk.CTkFrame(master=win)
cbox = ctk.CTkComboBox(master=main_frame, values=["Regular QR-Code WIP", "WiFi QR-Code"],
                        font=("Helvetica", 11))

# Used in 'wifi_qr_code()'
wifi_qr_code_frame = ctk.CTkFrame(master=win)
#file_or_show_cbox = ctk.CTkComboBox(master=wifi_qr_code_frame, values=["Save to File", "Show"]) WIP
sec_type_cbox = ctk.CTkComboBox(master=wifi_qr_code_frame, values=["WEP", "WPA", "None"])
wifi_ssid_input = ctk.CTkEntry(master=wifi_qr_code_frame, placeholder_text="WiFi SSID")
wifi_passwd_input = ctk.CTkEntry(master=wifi_qr_code_frame, placeholder_text="WiFi Password", show="*")

# Used in 'reg_qr_code()'
reg_qr_code_frame = ctk.CTkFrame(master=win)

# --- Functions ---
def main():
    """Runs the main window
    """

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
    main_frame.pack_forget()

    if choice == "WiFi QR-Code":
        wifi_qr_code()
    elif choice == "Regular QR-Code":
        reg_qr_code()

def reg_qr_code():
    """Shows all the reg_qr_code widgets
    """
    qr_type = "regular"

    reg_qr_code_label = ctk.CTkLabel(master=reg_qr_code_frame, text="Regular QR-Code", font=("Helvetica", 24))

    reg_qr_code_label.pack(pady=12, padx=10)
    reg_qr_code_frame.pack(pady=20, padx=60, fill="both", expand=True)

def wifi_qr_code():
    """Shows all the wifi_qr_code widgets
    """
    qr_type = "wifi"

    wifi_qr_code_label = ctk.CTkLabel(master=wifi_qr_code_frame, text="WiFi QR-Code", font=("Helvetica", 24))
    gen_qr_button = ctk.CTkButton(master=wifi_qr_code_frame, text="Generate", command=create_qr)

    wifi_qr_code_label.pack(pady=12, padx=10)
    wifi_ssid_input.pack(pady=6, padx=10)
    wifi_passwd_input.pack(pady=6, padx=10)
    sec_type_cbox.pack(pady=6, padx=10)
    gen_qr_button.pack(pady=12, padx=10)
    sec_type_cbox.set("Security Type")

    wifi_qr_code_frame.pack(pady=20, padx=60, fill="both", expand=True)

def create_qr():
    """Checks the type of QR-Code and creates the respective type
    """
    if qr_type == "wifi":
        gen_wifi_qr_code(wifi_ssid_input.get(), wifi_passwd_input.get(), sec_type_cbox.get())
        qr_type = None

    elif qr_type == "regular":
        gen_reg_qr_code()
        qr_type = None

if __name__ == "__main__":
    main()
