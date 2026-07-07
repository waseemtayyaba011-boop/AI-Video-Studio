import customtkinter as ctk

from ui.sidebar import Sidebar


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        self.main = ctk.CTkFrame(self)
        self.main.pack(side="right", fill="both", expand=True)

        title = ctk.CTkLabel(
            self.main,
            text="AI VIDEO STUDIO PRO",
            font=("Arial", 28, "bold")
        )

        title.pack(pady=30)