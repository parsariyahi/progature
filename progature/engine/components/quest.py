class Quest:
    
    def __init__(self, name, is_complete=False):
        self.name = name
        self.is_complete = is_complete

    def __str__(self) -> str:
        string = f"quest name: {self.name}"
        return string