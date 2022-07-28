from __future__ import annotations

import typing as tp

import dataclasses

from app import models


@dataclasses.dataclass
class Location:
    lat: float
    lon: float


@dataclasses.dataclass
class Scooter(models.Scooter):
    address: tp.Optional[str] = None

    @classmethod
    def from_model(cls, scooter: models.Scooter) -> Scooter:
        return cls(id=scooter.id, location=scooter.location, user=scooter.user)
