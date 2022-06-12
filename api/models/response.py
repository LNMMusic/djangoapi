from dataclasses import dataclass

@dataclass
class NewResponse:
    statusOk:   bool
    message:    str
    data:       object