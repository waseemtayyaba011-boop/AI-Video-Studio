import customtkinter as ctk

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 28, "bold")
        ).pack(pady=30)