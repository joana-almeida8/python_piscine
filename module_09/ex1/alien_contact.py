from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validator(self):
        errors = []
        if self.contact_id[:2] != "AC":
            errors.append("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            errors.append("Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC and \
                self.witness_count < 3:
            errors.append("Telepathic contact requires at least "
                          "3 witnesses")
        if self.signal_strength <= 7.0 and not self.message_received:
            errors.append("Strong signals (> 7.0) should include "
                          "received messages")
        if errors:
            raise ValueError("\n".join(errors))
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        contact1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
        print("Valid contact report:")
        print(f"ID: {contact1.contact_id}")
        print(f"Type: {contact1.contact_type.value}")
        print(f"Location: {contact1.location}")
        print(f"Signal: {contact1.signal_strength}/10")
        print(f"Duration: {contact1.duration_minutes} minutes")
        print(f"Witnesses: {contact1.witness_count}")
        if contact1.message_received:
            print(f"Message: '{contact1.message_received}'")
        else:
            print("No message received")
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")

    print("\n======================================")
    print("Expected validation error:")
    try:
        contact2 = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            contact_type=ContactType.TELEPATHIC,
            location="Stonehenge, UK",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Alpha Centauri",
            is_verified=True,
        )
        print("Valid contact report:")
        print(f"ID: {contact2.contact_id}")
        print(f"Type: {contact2.contact_type.value}")
        print(f"Location: {contact2.location}")
        print(f"Signal: {contact2.signal_strength}/10")
        print(f"Duration: {contact2.duration_minutes} minutes")
        print(f"Witnesses: {contact2.witness_count}")
        if contact2.message_received:
            print(f"Message: '{contact2.message_received}'")
        else:
            print("No message received")
    except ValidationError as e:
        for error in e.errors():
            if "Value error" in error['msg']:
                noise, msg = error['msg'].split(", ")
                error['msg'] = msg
            print(f"{error['msg']}")
