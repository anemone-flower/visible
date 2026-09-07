# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: GardenLog
import unittest
from datetime import date, timedelta

class TestGardenLog(unittest.TestCase):
    def test_add_plant(self):
        from gardenlog import GardenLog
        g = GardenLog()
        g.add_plant("Tomato", date.today())
        self.assertEqual(len(g.plants), 1)

    def test_add_plot(self):
        from gardenlog import GardenLog
        g = GardenLog()
        g.add_plot("Tomato", date.today(), "North")
        self.assertEqual(len(g.plots), 1)

    def test_add_irrigation(self):
        from gardenlog import GardenLog
        g = GardenLog()
        g.add_irrigation("Tomato", date.today(), 10)
        self.assertEqual(len(g.irrigations), 1)

    def test_add_task(self):
        from gardenlog import GardenLog
        g = GardenLog()
        g.add_task("Water plants", date.today(), "Watering")
        self.assertEqual(len(g.tasks), 1)

    def test_add_observation(self):
        from gardenlog import GardenLog
        g = GardenLog()
        g.add_observation("Tomato", date.today(), "Green sprout")
        self.assertEqual(len(g.observations), 1)

    def test_add_note(self):
        from gardenlog import GardenLog
        g = GardenLog()
        g.add_note("Plan new garden", date.today())
        self.assertEqual(len(g.notes), 1)

if __name__ == "__main__":
    unittest.main()
