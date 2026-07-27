from pathlib import Path
from setuptools import setup, find_packages


def read_requirements(path: str = "requirements.txt") -> list[str]:
    req_file = Path(__file__).parent / path
    requirements = []
    for line in req_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Drop inline comments, e.g. "foo>=1.0  # reason"
        if " #" in line:
            line = line.split(" #", 1)[0].strip()
        requirements.append(line)
    return requirements


setup(
    name="octo",
    packages=find_packages(),
    install_requires=read_requirements(),
)
