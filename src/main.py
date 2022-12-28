"""Handles the main customtkinter stuff
"""
# --- Imports ---
import customtkinter as ctk
import qrcode as qrc

# --- Constants ---
win = ctk.CTk()

# --- CustomTkinter stuff ---
win.title("Simple QR-Code Generator")
win.geometry("500x350")
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

main_frame = ctk.CTkFrame(master=win)

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
    choice = cbox.get()

    if choice == "WiFi QR-Code":
        return
    elif choice == "Regular QR-Code":
        return

if __name__ == "__main__":
    main()
