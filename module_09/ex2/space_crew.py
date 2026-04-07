from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validator(self):
        errors = []
        if not self.mission_id.startswith("M"):
            errors.append('Mission ID must start with "M"')
        experienced = 0
        leadership = 0
        inactive = 0
        for member in self.crew:
            if member.years_experience >= 5:
                experienced += 1
            if member.rank.value == "commander" or \
                    member.rank.value == "captain":
                leadership += 1
            if not member.is_active:
                inactive += 1
        if leadership == 0:
            errors.append("Must have at least one Commander or Captain")
        if self.duration_days > 365 and experienced < (len(self.crew)/2):
            errors.append("Long missions need experienced crew (5+ years)")
        if inactive != 0:
            errors.append("All crew members must be active")
        if errors:
            raise ValueError("\n".join(errors))
        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=46,
                    specialization="Mission Command",
                    years_experience=18,
                    is_active=True
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=57,
                    specialization="Navigation",
                    years_experience=26,
                    is_active=True
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=39,
                    specialization="Engineering",
                    years_experience=14,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission1.mission_name}")
        print(f"ID: {mission1.mission_id}")
        print(f"Destination: {mission1.destination}")
        print(f"Duration: {mission1.duration_days} days")
        print(f"Budget: ${mission1.budget_millions}M")
        print(f"Crew size: {len(mission1.crew)}")
        print("Crew members:")
        for member in mission1.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")
    except ValidationError as e:
        for error in e.errors():
            if "Value error" in error['msg']:
                noise, msg = error['msg'].split(", ")
                error['msg'] = msg
            print(f"{error['msg']}")

    print("\n=========================================")
    print("Expected validation error:")
    try:
        mission2 = SpaceMission(
            mission_id="M2030_PHM",
            mission_name="Project Hail Mary",
            destination="Tau Ceti",
            launch_date=datetime.now(),
            duration_days=3650,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Olesya Ilyukhina",
                    rank=Rank.LIEUTENANT,
                    age=46,
                    specialization="Mission Command",
                    years_experience=18,
                    is_active=True
                ),
                CrewMember(
                    member_id="C002",
                    name="Yao",
                    rank=Rank.LIEUTENANT,
                    age=57,
                    specialization="Navigation",
                    years_experience=26,
                    is_active=True
                ),
                CrewMember(
                    member_id="C003",
                    name="Rylan Grace",
                    rank=Rank.CADET,
                    age=39,
                    specialization="Science",
                    years_experience=0,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission2.mission_name}")
        print(f"ID: {mission2.mission_id}")
        print(f"Destination: {mission2.destination}")
        print(f"Duration: {mission2.duration_days} days")
        print(f"Budget: ${mission2.budget_millions}M")
        print(f"Crew size: {len(mission2.crew)}")
        print("Crew members:")
        for member in mission2.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")
    except ValidationError as e:
        for error in e.errors():
            if "Value error" in error['msg']:
                noise, msg = error['msg'].split(", ")
                error['msg'] = msg
            print(f"{error['msg']}")
