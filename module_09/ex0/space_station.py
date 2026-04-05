from pydantic import BaseModel, Field, ValidationError
import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxigen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


if __name__ == "__main__":
    print("Space Station Data Validation\n")
    print("========================================")
    try:
        station1 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxigen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
        )
    except:
        ...
