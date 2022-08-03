from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto
import json
import any 

@dataclass
class RequestMixin:
    @classmethod
    def from_request(cls, request):
        values = request.get("input")
        return cls(**values)
    
    @classmethod
    def from_json(cls, jsn):
      return cls(**jsn)

    def to_json(self):
        return json.dumps(asdict(self))

    def to_Any(self):
        return any.dumps(asdict(self))

@dataclass
class Author(RequestMixin):
  id: int
  author: str
  books: List[int]
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
class Query(RequestMixin):
  getbook_by_id: Optional[Book]

@dataclass
class getbook_by_idArgs(RequestMixin):
  id: str