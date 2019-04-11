from modelbender.domain import domain as d


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [d.Domain.from_dict(i) for i in self.data]

    
