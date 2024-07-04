import unittest
from datetime import datetime
from models import AspiringProfessional, SeniorExecutive, CoffeeChat
from coffee_chat_scheduler import CoffeeChatScheduler

class TestCoffeeChatScheduler(unittest.TestCase):
    def setUp(self):
        self.aspiring_professionals = [
            AspiringProfessional(id=1, name="Alice", industry="Tech", interests=["AI", "ML"], activity={"AI": 5, "ML": 3}),
            AspiringProfessional(id=2, name="Bob", industry="Finance", interests=["Investment", "Fintech"], activity={"Investment": 4, "Fintech": 2})
        ]

        self.senior_executives = [
            SeniorExecutive(frequency=1, id=1, name="Mr. Smith", industry="Tech", interests=["AI"]),
            SeniorExecutive(frequency=0, id=2, name="Ms. Johnson", industry="Finance", interests=["Fintech"]),
            SeniorExecutive(frequency=2, id=3, name="Dr. Brown", industry="Health", interests=["ML"])
        ]
        self.scheduler = CoffeeChatScheduler(self.aspiring_professionals, self.senior_executives)

    def test_match(self):
        matches = self.scheduler.match()
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0].aspiring_professional_id, 1)
        self.assertEqual(matches[0].senior_executive_id, 1)
        self.assertEqual(matches[1].aspiring_professional_id, 2)
        self.assertEqual(matches[1].senior_executive_id, 2)

if __name__ == "__main__":
    unittest.main()
