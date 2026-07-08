import customtkinter as ctk
from tkinter import messagebox

from core.project_manager import ProjectManager
from ai.image_generator import ImageGenerator


class PromptPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Project Name").pack(pady=(20, 5))

        self.project_name = ctk.CTkEntry(self, width=400)
        self.project_name.pack()

        self.prompt = ctk.CTkTextbox(
            self,
            width=700,
            height=250
        )
        self.prompt.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Save Prompt",
            command=self.create_project
        ).pack(pady=20)

    def create_project(self):

        project_name = self.project_name.get()

        ok, msg = ProjectManager.create_project(project_name)

        if ok:
            ProjectManager.save_prompt(
                project_name,
                self.prompt.get("1.0", "end")
            )

            generator = ImageGenerator()
            generator.generate(
                self.prompt.get("1.0", "end")
            )

            messagebox.showinfo(
                "Success",
                "Prompt Saved Successfully"
            )

        else:
            messagebox.showerror("Error", msg)