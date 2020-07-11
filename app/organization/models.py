from datetime import datetime
import re

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

    @classmethod
    def fuzzySearch(cls, query):
        try:
            escaped = re.sub(r'[-[\]{}()*+?.,\\^$|#\s]', "\\$&", query)
            regex = re.compile(escaped, flags=re.I)

            documents = cls.collection.find({ "name": regex })
            results = []
            for i, doc in enumerate(documents):
                doc['_id'] = str(doc['_id'])
                results.append(doc)

            return results
        except Exception:
            return None
