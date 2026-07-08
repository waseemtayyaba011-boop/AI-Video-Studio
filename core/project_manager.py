import os


class ProjectManager:

    PROJECTS_DIR = os.path.abspath("projects")

    @staticmethod
    def create_project(project_name):

        project_name = project_name.strip()

        if not project_name:
            return False, "Project name required"

        path = os.path.join(ProjectManager.PROJECTS_DIR, project_name)

        os.makedirs(path, exist_ok=True)
        os.makedirs(os.path.join(path, "images"), exist_ok=True)
        os.makedirs(os.path.join(path, "videos"), exist_ok=True)
        os.makedirs(os.path.join(path, "audio"), exist_ok=True)

        return True, path

    @staticmethod
    def save_prompt(project_name, prompt):

        project_name = project_name.strip()

        path = os.path.join(
            ProjectManager.PROJECTS_DIR,
            project_name,
            "prompt.txt"
        )

        with open(path, "w", encoding="utf-8") as file:
            file.write(prompt)

        return True