import shutil
import subprocess


class Detector:

    @staticmethod
    def detect_python_versions():

        versions = []
        seen = set()

        possible = [
            "py",
            "python",
            "python3",
            "python3.10",
            "python3.11",
            "python3.12"
        ]

        for cmd in possible:

            if not shutil.which(cmd):
                continue

            try:

                if cmd == "py":

                    output = subprocess.check_output(
                        [cmd, "--version"],
                        text=True,
                        stderr=subprocess.DEVNULL
                    ).strip()

                else:

                    output = subprocess.check_output(
                        [cmd, "--version"],
                        text=True,
                        stderr=subprocess.DEVNULL
                    ).strip()

                if output not in seen:

                    versions.append({
                        "command": cmd,
                        "version": output
                    })

                    seen.add(output)

            except Exception:
                pass

        return versions

    @staticmethod
    def conda_available() -> bool:
        return shutil.which("conda") is not None