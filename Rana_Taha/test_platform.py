import pytest

from main import Platform, AspiringProfessional, SeniorExecutive, solution

industries = ["Technology", "Healthcare", "Defense", "Government", "Medicine", "Education", "Finance", "Entertainment", "Retail", "Transportation"]
def test_no_industries():
    aspiring_professionals_per_industry = 1
    senior_executives_per_industry = 1
    interests_per_aspiring_professional = 1
    weeks_to_simulate = 5
    industries = []
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
    assert result == [] 
def test_no_professionals():
    aspiring_professionals_per_industry = 1
    senior_executives_per_industry = 0
    interests_per_aspiring_professional = 1
    weeks_to_simulate = 5
    industries = ["Technology"]
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
    assert all(len(week) == 0 for week in result)  

def test_no_aspiring_professionals():
    aspiring_professionals_per_industry = 0
    senior_executives_per_industry = 1
    interests_per_aspiring_professional = 1
    weeks_to_simulate = 5
    industries = ["Technology"]
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
    assert all(len(week) == 0 for week in result) 

def test_no_interests():
    aspiring_professionals_per_industry = 1
    senior_executives_per_industry = 1
    interests_per_aspiring_professional = 0
    weeks_to_simulate = 5
    industries = ["Technology"]
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
    assert all(len(week) == 0 for week in result)  

def test_one_professional_per_industry():
    aspiring_professionals_per_industry = 1
    senior_executives_per_industry = 1
    interests_per_aspiring_professional = 1
    weeks_to_simulate = 5
    industries = ["Technology"]
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
    print(result)
    assert len(result[0]) == 1 
    assert all(len(week) == 0 for week in result[1:])  

def test_one_professional_per_industry_2_interests():
    aspiring_professionals_per_industry = 5
    senior_executives_per_industry = 1
    interests_per_aspiring_professional = 2
    weeks_to_simulate = 5
    industries = ["Technology","Healthcare"]
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
    max_amount_coffee_chats = senior_executives_per_industry*interests_per_aspiring_professional
    print("hello")
    print("this is result", result)
    assert all(len(week) == aspiring_professionals_per_industry*len(industries) for week in result[:max_amount_coffee_chats])
    assert all(len(week) == 0 for week in result[max_amount_coffee_chats:])   

def test_multiple_professionals_per_industry_and_one_interest():
    aspiring_professionals_per_industry = 2
    senior_executives_per_industry = 2
    interests_per_aspiring_professional = 1
    weeks_to_simulate = 5
    industries = ["Technology", "Healthcare"]
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
    max_amount_coffee_chats = senior_executives_per_industry*interests_per_aspiring_professional

    assert all(len(week) == aspiring_professionals_per_industry*len(industries) for week in result[:max_amount_coffee_chats])
    assert all(len(week) == 0 for week in result[max_amount_coffee_chats:])  

def test_multiple_interests_per_professional():
    aspiring_professionals_per_industry = 1
    senior_executives_per_industry = 1
    interests_per_aspiring_professional = 2
    weeks_to_simulate = 5
    industries = ["Technology", "Healthcare"]
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
    max_amount_coffee_chats = senior_executives_per_industry*interests_per_aspiring_professional

    assert all(len(week) == aspiring_professionals_per_industry*len(industries) for week in result[:max_amount_coffee_chats])
    assert all(len(week) == 0 for week in result[max_amount_coffee_chats:])  


def test_many_coffee_chats():
    aspiring_professionals_per_industry = 10
    senior_executives_per_industry = 10
    interests_per_aspiring_professional = 10
    weeks_to_simulate = 100
    industries = ["Technology", "Healthcare", "Defense", "Government", "Medicine", "Education", "Finance", "Entertainment", "Retail", "Transportation"]
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
    
    assert all(len(week) == 100 for week in result)

# def test_many_coffee_chats_maximum():
#     aspiring_professionals_per_industry = 10000
#     senior_executives_per_industry = 1000
#     interests_per_aspiring_professional = 5
#     weeks_to_simulate = 5001
#     industries = ["Technology", "Healthcare", "Defense", "Government", "Medicine", "Education", "Finance", "Entertainment", "Retail", "Transportation"]

#     result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)
#     max_amount_coffee_chats = senior_executives_per_industry*interests_per_aspiring_professional
#     assert all(len(week) == 10000 for week in result[:max_amount_coffee_chats])
#     #only 5000 weeks can be simulated with these parameters, last week must have none
#     assert(len(result[-1]) == 0)
if __name__ == "__main__":
    pytest.main()