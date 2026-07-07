import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.home_page import HomePage
from ui.projects_page import ProjectsPage
from ui.prompt_page import PromptPage
from ui.characters_page import CharactersPage


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.sidebar = Sidebar(self, self.show_page)
        self.sidebar.pack(side="left", fill="y")

        self.container = ctk.CTkFrame(self)
        self.container.pack(side="right", fill="both", expand=True)

        self.pages = {
            "Dashboard": HomePage(self.container),
            "Projects": ProjectsPage(self.container),
            "Prompt": PromptPage(self.container),
            "Characters": CharactersPage(self.container),
        }

        self.show_page("Dashboard")

    def show_page(self, name):

        for page in self.pages.values():
            page.pack_forget()

        self.pages[name].pack(fill="both", expand=True)