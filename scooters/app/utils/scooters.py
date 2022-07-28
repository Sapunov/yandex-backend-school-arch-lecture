import dataclasses
import typing as tp
import time
import asyncio

from app.context import AppContext
from app import storage
from app import dto
from app.utils import geocode


async def _enrich_address(
    scooters: tp.List[dto.Scooter], client: geocode.GeocoderClient
) -> None:
    futures = [client.get_address(scooter.location) for scooter in scooters]

    result = await asyncio.gather(*futures)

    for scooter, address in zip(scooters, result):
        scooter.address = address


@dataclasses.dataclass
class GetScootersParams:
    fetch_address: bool = False


async def get_scooters(
    context: AppContext, params: GetScootersParams
) -> tp.List[dto.Scooter]:
    scooters = [
        dto.Scooter.from_model(scooter)
        for scooter in await storage.get_scooters(context)
    ]

    if params.fetch_address:
        start = time.time()
        await _enrich_address(scooters, context.geocoder)
        finish = time.time()
        print(f'Elapsed time: {finish - start}')

    return scooters
