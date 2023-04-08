import dataclasses
from dataclasses_json import dataclass_json


@dataclass_json
@dataclasses.dataclass
class User:

    id: int
    name: str
