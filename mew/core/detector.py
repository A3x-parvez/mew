import shutil
import subprocess


class Detector:

    @staticmethod
    def detect_python_versions():
        versions = []

        possible = [
            "python",
            "python3",
            "python3.10",
            "python3.11",
            "python3.12"
        ]

        for cmd in possible:
            if shutil.which(cmd):
                try:
                    output = subprocess.check_output(
                        [cmd, "--version"],
                        text=True
                    ).strip()

                    versions.append({
                        "command": cmd,
                        "version": output
                    })

                except Exception:
                    pass

        return versions

    @staticmethod
    def conda_available() -> bool:
        return shutil.which("conda") is not None