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

@dataclass
class ArgInput(RequestMixin):
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
class Shard(RequestMixin):
  total: Optional[int]
  successful: Optional[int]
  failed: Optional[int]

@dataclass
class DeleteDocument(RequestMixin):
  _index: Optional[str]
  _type: Optional[str]
  _id: Optional[str]
  _version: Optional[str]
  result: Optional[str]
  _shards: Optional[Shard]
  _seq_no: Optional[int]
  _primary_term: Optional[int]


@dataclass
class Mutation(RequestMixin):
  createdocument: Optional[DeleteDocument]
  deletedocumentbyid: Optional[DeleteDocument]
  updatedocumentfield: Optional[DeleteDocument]

@dataclass
class updatedocumentfieldArgs(RequestMixin):
  index: str
  id: str
  fields: Optional[ArgInput]
