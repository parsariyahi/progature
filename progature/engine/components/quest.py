class Quest:
    
    def __init__(self, index: int, name, is_complete=False):
        self.index = index
        self.name = name
        self.is_complete = is_complete

    def __str__(self) -> str:
        string = f"{self.index}.{self.name}:{self.is_complete}"
        return string

    def __eq__(self, other) -> bool:
        if isinstance(other, Quest):
            return self.name == other.name

        raise TypeError("Type Error Quest")