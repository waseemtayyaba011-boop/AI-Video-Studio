import customtkinter as ctk

class CharactersPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="Characters",
            font=("Arial", 28, "bold")
        ).pack(pady=30)