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
  deletedocumentbyid: Optional[DeleteDocument]

@dataclass
class deletedocumentbyidArgs(RequestMixin):
  index: str
  id: str