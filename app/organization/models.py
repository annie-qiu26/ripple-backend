from datetime import datetime

from app.database import Model
from app import db

class Organization(Model):
    collection = db.organizations

    def __init__(self, name=None, url=None, category=None):
        super().__init__()

        self._id = None # str, token that uniquely identiifes Node
        self.name = name # str, name of the organization
        self.url = url # str, url of the organization
        self.category = category # Optional

    def dict(self):
        dic = {}
        dic.update(self.__dict__)
        return dic

