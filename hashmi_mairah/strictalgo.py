from datetime import datetime
from models import AspiringProfessional, SeniorExecutive, CoffeeChat
from coffee_chat_scheduler import CoffeeChatScheduler

def read_test_case(file_path="testcase.txt"):
    aspiring_professionals = []
    senior_executives = []

    with open(file_path, "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            name = lines[i].strip()
            industry = lines[i+1].strip()
            interests = lines[i+2].strip().split(',')
            ap = AspiringProfessional(id=i, name=name, industry=industry, interests=interests, activity={})
            aspiring_professionals.append(ap)
    
    # Dummy senior executives for demonstration
    senior_executives = [
        SeniorExecutive(frequency=1, id=1, name="Mr. Smith", industry="Tech", interests=["AI"]),
        SeniorExecutive(frequency=0, id=2, name="Ms. Johnson", industry="Finance", interests=["Fintech"]),
        SeniorExecutive(frequency=2, id=3, name="Dr. Brown", industry="Health", interests=["ML"])
    ]

    return aspiring_professionals, senior_executives

if __name__ == "__main__":
    aspiring_professionals, senior_executives = read_test_case()
    scheduler = CoffeeChatScheduler(aspiring_professionals, senior_executives)
    weekly_matches = scheduler.match()
    for match in weekly_matches:
        print(f"Coffee chat scheduled: {match.aspiring_professional_id} with {match.senior_executive_id} on {match.date}")
