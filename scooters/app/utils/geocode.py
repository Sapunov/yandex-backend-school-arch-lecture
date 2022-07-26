import typing as tp

import aiohttp

from app import dto


class GeocoderClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = 'https://geocode-maps.yandex.ru',
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url

    async def get_address(self, location: dto.Location) -> tp.Optional[str]:
        async with aiohttp.ClientSession(self.base_url) as session:
            async with session.get(
                '/1.x/',
                params={
                    'format': 'json',
                    'geocode': f'{location.lat},{location.lon}',
                    'apikey': self.api_key,
                },
            ) as response:
                if response.status != 200:
                    return None

                data = await response.json()

                member = data['response']['GeoObjectCollection'][
                    'featureMember'
                ]

                if not member:
                    return None

                return member[0]['GeoObject']['metaDataProperty'][
                    'GeocoderMetaData'
                ]['text']
