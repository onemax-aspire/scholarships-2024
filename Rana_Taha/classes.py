import heapq
import random
import copy
class Person:
    def __init__(self, name: str, industry: str):
        self.name = name
        self.industry = industry

    def __repr__(self):
        return f"{self.name} ({self.industry})"

class AspiringProfessional(Person):
    def __init__(self, name: str, industry: str, interests: list[str]):
        super().__init__(name, industry)
        self.interests = interests 
        self.professionals_met = set()
    def __repr__(self):
        return f"AspiringProfessional: {self.name} ({self.industry}) - Interests: {', '.join(self.interests)}"

class SeniorExecutive(Person):
    def __init__(self, name: str, industry: str, years_of_experience: int, appearance_count: int = 0):
        super().__init__(name, industry)
        self.years_of_experience = years_of_experience 
        self.appearance_count = appearance_count  

    def __repr__(self):
        return f"SeniorExecutive: {self.name} ({self.industry}) - YOE: {self.years_of_experience}, Appearances: {self.appearance_count}"
    def __lt__(self, other):
        return self.appearance_count < other.appearance_count

class Platform:
    def __init__(self, industries):
        self.industries = industries
        self.professionals = []
        self.aspiring_professionals = []
        self.industry_heaps = {}
        self.create_industry_heaps()

    def create_industry_heaps(self):
        for industry in self.industries:
            self.industry_heaps[industry] = []
    def add_professional(self, professional):
        self.professionals.append(professional)
        self.add_to_industry_heap(professional.industry,professional)
        
    def add_to_industry_heap(self, industry, professional):
        if industry in self.industry_heaps:
            print(professional)
            print(self.industry_heaps[industry])
            heapq.heappush(self.industry_heaps[industry], professional)

    def add_aspiring_professional(self, aspiring_professional):
        self.aspiring_professionals.append(aspiring_professional)
    def get_min_from_industry_heap(self, industry):
        if industry in self.industry_heaps and self.industry_heaps[industry]:
            return self.industry_heaps[industry][0]
        else:
            return None
    def add_professional_to_aspiring_professional(self, aspiring_professional, professional):
        aspiring_professional.professionals_met.add(professional)

    def find_coffee_chats(self, aspiring_professional):
        potential_industries = aspiring_professional.interests[:]
        random.shuffle(potential_industries)
        while potential_industries:
            potential_industry = potential_industries.pop()
            professional = self.find_valid_professional_for_industry(aspiring_professional, potential_industry)
            if professional is not None:
                professional.appearance_count += 1
                self.rebalance_heap(professional.industry)
                self.add_professional_to_aspiring_professional(aspiring_professional,professional)
                return professional
        return False

    def find_valid_professional_for_industry(self, aspiring_professional, industry):
        potential_options = self.industry_heaps[industry]
        temp_heap = []
        found_professional = None

        while potential_options:
            potential_professional = heapq.heappop(potential_options)
            if potential_professional not in aspiring_professional.professionals_met:
                found_professional = potential_professional
                break
            else:
                temp_heap.append(potential_professional)

        for professional in temp_heap:
            heapq.heappush(potential_options, professional)
        if found_professional:
            heapq.heappush(potential_options,found_professional)

        return found_professional
    def rebalance_heap(self,industry):
        heapq.heapify(self.industry_heaps[industry])
    def generate_coffee_chats(self):
        aspiring_professionals = self.aspiring_professionals
        random.shuffle(aspiring_professionals)
        coffee_chats = []


        for aspiring_professional in aspiring_professionals:
            coffeechat = self.find_coffee_chats(aspiring_professional)
            if coffeechat:
                coffee_chats.append((aspiring_professional.name, coffeechat.name, coffeechat.industry))
                print(f"{aspiring_professional.name} meets with {coffeechat.name} from industry {coffeechat.industry}")

            else:
                print(f"No Valid Coffee Chat found for {aspiring_professional.name}")
            

        return coffee_chats

 



