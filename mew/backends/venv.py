import subprocess


class VenvBackend:

    @staticmethod
    def create(path: str, python_executable: str = "python"):
        subprocess.run(
            [python_executable, "-m", "venv", path],
            check=True
        )