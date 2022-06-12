from dataclasses import dataclass

@dataclass
class NewResponse:
    statusOk:   bool
    message:    str
    data:       object

    def parse(self) -> object:
        return {
            'statusOk': self.statusOk,
            'message': self.message,
            'data': self.data
        }