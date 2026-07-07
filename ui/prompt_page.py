import customtkinter as ctk
from tkinter import messagebox

from core.project_manager import ProjectManager


class PromptPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Project Name").pack(pady=(20,5))

        self.project_name = ctk.CTkEntry(self, width=400)
        self.project_name.pack()

        ctk.CTkButton(
            self,
            text="Create Project",
            command=self.create_project
        ).pack(pady=20)

    def create_project(self):

        ok, msg = ProjectManager.create_project(
            self.project_name.get()
        )

        if ok:
            messagebox.showinfo("Success", f"Project Created\n\n{msg}")
        else:
            messagebox.showerror("Error", msg)