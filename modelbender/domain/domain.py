class Domain:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    @classmethod
    def from_dict(cls, adict):
        return cls(
            code = adict['code'],
            name = adict['name']
        )

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
