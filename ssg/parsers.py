from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions: List[str]

    def __init__(self, extensions):
        self.extensions = extensions
        self.extensions = []

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError
    

    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name

        with open(full_path, "w") as file:
            file.write(content)
    

    def copy(self, path, source, dest):
        shutil.copy2(path, dest.relative_to(source))


class ResourceParser(Parser):

    def __init__(self, extensions):
        super().__init__(extensions)
        self.extensions = [".jpg", ".png", ".gif", ".css", "html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)