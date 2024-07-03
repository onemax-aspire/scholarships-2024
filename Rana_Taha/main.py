from classes import Person, AspiringProfessional, SeniorExecutive, Platform
import random
def solution(aspiring_professionals_per_industry,senior_executives_per_industry,interests_per_aspiring_professional,weeks_to_simulate,industries):

    platform = Platform(industries)
    
    if not industries:
        return []
    #construct aspiring professionals
    for i in range(len(industries) * aspiring_professionals_per_industry):
        industry = industries[i % len(industries)]
        interests = list(set(industries[(i + j) % len(industries)] for j in range(interests_per_aspiring_professional)))
        aspiring_professional = AspiringProfessional(f"AspiringProfessional{i}", industry, interests)
        platform.add_aspiring_professional(aspiring_professional)

    #construct senior executives
    for i in range(len(industries) * senior_executives_per_industry):
        industry = industries[i % len(industries)]
        years_of_experience = random.randint(5, 25)
        senior_executive = SeniorExecutive(f"SeniorExecutive{i}", industry, years_of_experience, 0)
        platform.add_professional(senior_executive)
    
    #shuffle for variation
    random.shuffle(platform.aspiring_professionals)
    random.shuffle(platform.professionals)

    all_coffee_chats = []
    #generate coffee chats
    for i in range(weeks_to_simulate):
        print(f"Week {i+1} Coffee Chats:")
        coffee_chats = platform.generate_coffee_chats()
        all_coffee_chats.append(coffee_chats)
    
    return all_coffee_chats
#simple test case, based on previous logic based on this by week 10 we will have no more valid coffee chats
if __name__ == "__main__":
    aspiring_professionals_per_industry = 3
    senior_executives_per_industry = 3
    interests_per_aspiring_professional = 3
    weeks_to_simulate = 10
    industries = ["Technology", "Healthcare", "Defense"]
    result = solution(aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries)