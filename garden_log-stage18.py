# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: GardenLog
class Tag:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Tag name must be a non-empty string")
        self.name = name.strip()

    @property
    def id(self):
        return hash(self.name) & 0xFFFFFFFF

    def __repr__(self):
        return f"Tag({self.name!r})"

class TagManager:
    _tags = {}

    @classmethod
    def add(cls, name):
        tag = Tag(name)
        cls._tags[tag.id] = tag
        return tag

    @classmethod
    def remove(cls, name):
        tag = Tag(name)
        if tag.id not in cls._tags:
            raise ValueError(f"Tag {name!r} does not exist")
        del cls._tags[tag.id]

    @classmethod
    def exists(cls, name):
        return Tag(name).id in cls._tags

    @classmethod
    def get(cls, name):
        tag = Tag(name)
        return cls._tags.get(tag.id)

    @classmethod
    def list_all(cls):
        return list(cls._tags.values())

TagManager._tags = {}
