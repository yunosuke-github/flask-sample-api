import dataclasses
from dataclasses_json import dataclass_json


@dataclass_json
@dataclasses.dataclass
class Item:

    id: int
    name: str
    price: int
