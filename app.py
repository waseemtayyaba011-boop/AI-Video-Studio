import customtkinter as ctk
from ui.dashboard import Dashboard

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("AI Video Studio Pro")
app.geometry("1200x700")

dashboard = Dashboard(app)
dashboard.pack(fill="both", expand=True)

app.mainloop()