"""Handles the main customtkinter stuff
"""
# --- Imports ---
import customtkinter as ctk
import qrcode

# --- Constants ---
win = ctk.CTk()

# --- CustomTkinter stuff ---
win.title("Simple QR-Code Generator")
win.geometry("500x350")
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

main_frame = ctk.CTkFrame(master=win)
wifi_qr_code_frame = ctk.CTkFrame(master=win)

file_or_show_cbox = ctk.CTkComboBox(master=wifi_qr_code_frame, values=["Save to File", "Show"])
sec_type_cbox = ctk.CTkComboBox(master=wifi_qr_code_frame, values=["WEP", "WPA", "None"])
cbox = ctk.CTkComboBox(master=main_frame, values=["Regular QR-Code", "WiFi QR-Code"],
                        font=("Helvetica", 11))

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

    if choice == "WiFi QR-Code":
        main_to_wifi_qr_code()
    elif choice == "Regular QR-Code":
        return

def main_to_wifi_qr_code():
    """Gets rid of the main pages widgets and runs the 'wifi_qr_code' function
    """
    main_frame.pack_forget()

    wifi_qr_code()

def wifi_qr_code():
    """Shows all the wifi_qr_code widgets
    """
    wifi_qr_code_label = ctk.CTkLabel(master=wifi_qr_code_frame, text="WiFi QR-Code", font=("Helvetica", 24))
    wifi_ssid_input = ctk.CTkEntry(master=wifi_qr_code_frame, placeholder_text="WiFi SSID")
    wifi_passwd_input = ctk.CTkEntry(master=wifi_qr_code_frame, placeholder_text="WiFi Password", show="*")
    generate_qr_button = ctk.CTkButton(master=wifi_qr_code_frame, text="Generate")

    wifi_qr_code_label.pack(pady=12, padx=10)
    wifi_ssid_input.pack(pady=6, padx=10)
    wifi_passwd_input.pack(pady=6, padx=10)
    sec_type_cbox.pack(pady=6, padx=10)
    generate_qr_button.pack(pady=12, padx=10)
    sec_type_cbox.set("Security Type")

    wifi_qr_code_frame.pack(pady=20, padx=60, fill="both", expand=True)

if __name__ == "__main__":
    main()
