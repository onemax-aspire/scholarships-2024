import heapq
from collections import defaultdict
from datetime import datetime  # Import datetime module
from models import AspiringProfessional, SeniorExecutive, CoffeeChat

class CoffeeChatScheduler:
    def __init__(self, aspiring_professionals, senior_executives):
        self.aspiring_professionals = aspiring_professionals
        self.senior_executives = senior_executives
        self.history = defaultdict(list)  # Keeps track of past matches to avoid repetition
        self.executive_heap = [(se.frequency, se) for se in senior_executives]
        heapq.heapify(self.executive_heap)

    def match(self):
        weekly_matches = []
        
        for ap in self.aspiring_professionals:
            possible_matches = []
            for _, se in self.executive_heap:
                if se.industry == ap.industry or any(interest in se.interests for interest in ap.interests):
                    possible_matches.append(se)
            
            if possible_matches:
                possible_matches.sort(key=lambda se: se.frequency)
                selected_executive = possible_matches[0]
                weekly_matches.append(CoffeeChat(ap.id, selected_executive.id, datetime.now()))
                self.history[ap.id].append(selected_executive.id)
                selected_executive.frequency += 1
                heapq.heapify(self.executive_heap)
        
        return weekly_matches
