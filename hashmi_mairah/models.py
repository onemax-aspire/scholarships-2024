from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime

@dataclass(order=True)
class SeniorExecutive:
    frequency: int
    id: int = field(compare=False)
    name: str = field(compare=False)
    industry: str = field(compare=False)
    interests: List[str] = field(compare=False)

@dataclass
class AspiringProfessional:
    id: int
    name: str
    industry: str
    interests: List[str]
    activity: Dict[str, int]

@dataclass
class CoffeeChat:
    aspiring_professional_id: int
    senior_executive_id: int
    date: datetime
