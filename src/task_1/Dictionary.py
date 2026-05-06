class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def newentry(self, key:str, value:str) -> None:
        self.dictionary[key] = value

    def look(self, key:str) -> str:
        return self.dictionary.get(key, f"Can't find entry for {key}")