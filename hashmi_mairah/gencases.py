import random

def generate_test_case():
    professionals = ["Alice", "Bob", "Charlie", "David"]
    industries = ["Tech", "Finance", "Health", "Education"]
    interests = ["AI", "ML", "Fintech", "Investment", "Cybersecurity"]

    with open("testcase.txt", "w") as file:
        for pro in professionals:
            industry = random.choice(industries)
            user_interests = random.sample(interests, 3)
            file.write(f"{pro}\n{industry}\n{','.join(user_interests)}\n")

if __name__ == "__main__":
    generate_test_case()