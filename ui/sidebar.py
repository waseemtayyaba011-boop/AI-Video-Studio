import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=220)

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text="MENU",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        buttons = [
            "Dashboard",
            "Projects",
            "Prompt",
            "Characters",
            "Images",
            "Videos",
            "Settings"
        ]

        for item in buttons:
            ctk.CTkButton(
                self,
                text=item
            ).pack(fill="x", padx=15, pady=5)