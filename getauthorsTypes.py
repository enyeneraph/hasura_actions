from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto
import json

@dataclass
class RequestMixin:
    @classmethod
    def from_request(cls, request):
        values = request.get("input")
        return cls(**values)

    def to_json(self):
        return json.dumps(asdict(self))

@dataclass
class Author(RequestMixin):
  id: int
  author: str
  books: Optional[List[int]]
  gender: Optional[str]
  location: Optional[str]
  name: str
  num_of_books: Optional[int]

@dataclass
class Book(RequestMixin):
  id: str
  title: str
  genre: Optional[str]
  height: Optional[int]
  publisher: Optional[str]
  author: Author




@dataclass
class Authors(RequestMixin):
  authors: Optional[List[Author]]

@dataclass
class Query(RequestMixin):
  getauthors: Optional[Authors]

