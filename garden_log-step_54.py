# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: GardenLog
class Favorites:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def toggle(self, item):
        if item in self.items:
            self.remove(item)
        else:
            self.add(item)

    def is_favorited(self, item):
        return item in self.items

    def list_favorites(self):
        return list(self.items)

    def load(self, path):
        if os.path.exists(path):
            with open(path, "a") as f:
                f.write(json.dumps(self.items))

    def save(self, path):
        with open(path, "w") as f:
            f.write(json.dumps(self.items))

favorites = Favorites()
