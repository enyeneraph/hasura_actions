from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto
import json,requests

@dataclass
class RequestMixin:
    @classmethod
    def from_request(cls, request):
      #verify that it is indeed a json
        values = request.get("input")
        # values = request
        return cls(**values)
    
    @classmethod
    def from_json(cls, jsn):
      return cls(**jsn)

    def to_json(self):
        return json.dumps(asdict(self))


@dataclass
class Author(RequestMixin):
  age: Optional[int]
  books: Optional[List[int]]
  gender: Optional[str]
  id: Optional[int]
  location: Optional[str]
  name: Optional[str]
  num_of_books: Optional[int]

@dataclass
class Query(RequestMixin):
  getauthor: Optional[Author]
  # if i need to use an argument (id:ID), how does it handle it?

@dataclass
class getauthorArgs(RequestMixin):
  id: int