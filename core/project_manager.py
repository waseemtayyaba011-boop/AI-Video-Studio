import os

class ProjectManager:

    PROJECTS_DIR = "projects"

    @staticmethod
    def create_project(project_name):

        if not project_name.strip():
            return False, "Project name required"

        path = os.path.join(ProjectManager.PROJECTS_DIR, project_name)

        os.makedirs(path, exist_ok=True)
        os.makedirs(os.path.join(path, "images"), exist_ok=True)
        os.makedirs(os.path.join(path, "videos"), exist_ok=True)
        os.makedirs(os.path.join(path, "audio"), exist_ok=True)

        return True, path