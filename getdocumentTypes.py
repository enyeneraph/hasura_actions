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
    
    @classmethod
    def from_json(cls, jsn):
      return cls(**jsn)

# @dataclass
# class Input(RequestMixin):
#   index: str
#   type: str
#   id: int


@dataclass
class Source(RequestMixin):
  account_number: Optional[int]
  balance: Optional[int]
  firstname: Optional[str]
  lastname: Optional[str]
  age: Optional[int]
  gender: Optional[str]
  address: Optional[str]
  employer: Optional[str]
  email: Optional[str]
  city: Optional[str]
  state: Optional[str]

@dataclass
class Document(RequestMixin):
  _index: Optional[str]
  _type: Optional[str]
  _id: Optional[str]
  _version: Optional[int]
  _seq_no: Optional[int]
  _primary_term: Optional[int]
  found: Optional[bool]
  _source: Optional[Source]

@dataclass
class Query(RequestMixin):
  getdocument: Optional[Document]

@dataclass
class getdocumentArgs(RequestMixin):
  index: str
  id: str