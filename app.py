import customtkinter as ctk

# App Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
app = ctk.CTk()
app.title("AI Video Studio")
app.geometry("1000x650")

# Title
title = ctk.CTkLabel(
    app,
    text="AI VIDEO STUDIO",
    font=("Arial", 30, "bold")
)
title.pack(pady=20)

# Project Name
project_label = ctk.CTkLabel(app, text="Project Name")
project_label.pack()

project_entry = ctk.CTkEntry(app, width=500)
project_entry.pack(pady=10)

# Prompt
prompt_label = ctk.CTkLabel(app, text="Enter Your Prompt")
prompt_label.pack()

prompt_box = ctk.CTkTextbox(app, width=800, height=220)
prompt_box.pack(pady=10)

# Buttons
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

image_btn = ctk.CTkButton(
    button_frame,
    text="Generate Images"
)
image_btn.grid(row=0, column=0, padx=10)

video_btn = ctk.CTkButton(
    button_frame,
    text="Generate Video"
)
video_btn.grid(row=0, column=1, padx=10)

# Status
status = ctk.CTkLabel(
    app,
    text="Status: Ready"
)
status.pack(side="bottom", pady=15)

app.mainloop()