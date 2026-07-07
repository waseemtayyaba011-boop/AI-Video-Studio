import customtkinter as ctk

class Sidebar(ctk.CTkFrame):

    def __init__(self, master, callback):
        super().__init__(master, width=220)

        self.pack_propagate(False)
        self.callback = callback

        ctk.CTkLabel(
            self,
            text="AI VIDEO STUDIO",
            font=("Arial",20,"bold")
        ).pack(pady=20)

        pages = [
            "Dashboard",
            "Projects",
            "Prompt",
            "Characters"
        ]

        for page in pages:
            ctk.CTkButton(
                self,
                text=page,
                command=lambda p=page: self.callback(p)
            ).pack(fill="x", padx=15, pady=5)