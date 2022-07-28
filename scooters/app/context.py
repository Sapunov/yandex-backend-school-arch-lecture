import typing as tp

import asyncpg

from app.utils import secrets
from app.utils import geocode


class AppContext:
    def __init__(self, *, secrets_dir: str):
        self.secrets: secrets.SecretsReader = secrets.SecretsReader(
            secrets_dir
        )
        self.db: tp.Optional[asyncpg.Pool] = None
        self.geocoder = geocode.GeocoderClient(
            self.secrets.get('ya_geocoder_api_key')
        )

    async def on_startup(self, app=None):
        self.db = await asyncpg.create_pool(self.secrets.get('postgres_dsn'))

    async def on_shutdown(self, app=None):
        if self.db:
            await self.db.close()
