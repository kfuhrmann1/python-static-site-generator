import re
from yaml import load,FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = __regex.split(string, 2)
        self.load(fm, Loader=FullLoader)

        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content
    
    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if self.data["type"] else False
    
    @type.setter
    def type(self):
        self._type = self.data["type"]

    
    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return self.data.__iter__()
    
    def __len__(self):
        return self.data.length()

    
    def __repr__(self):
        data = []

        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        
        return str(data)