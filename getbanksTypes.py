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

    @classmethod
    def from_json(cls, jsn,values):
        final = {}
        for i in jsn:
            if i in values:
                final[i] = jsn[i]

        return cls(**final)
        # return cls(**final)

    def to_json(self):
        return json.dumps(asdict(self))


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
class innerHit(RequestMixin):
  _index: Optional[int]
  _type: Optional[str]
  _score: Optional[int]
  _source: Optional[Source]

@dataclass
class Hit(RequestMixin):
  max_score: Optional[int]
  hits: Optional[List[innerHit]]


@dataclass
class Output(RequestMixin):
  took: Optional[int]
  timed_out: Optional[bool]
  hits: Optional[Hit]



@dataclass
class Query(RequestMixin):
  getbanks: Optional[Output]


# @dataclass
# class getbanksArgs(RequestMixin):
