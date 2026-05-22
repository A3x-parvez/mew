import subprocess


class CondaBackend:

    @staticmethod
    def create(name: str, python_version: str):
        subprocess.run(
            [
                "conda",
                "create",
                "-y",
                "-n",
                name,
                f"python={python_version}"
            ],
            check=True
        )