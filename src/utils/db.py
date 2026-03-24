from typing import List, cast

import redis

from src.config import REDIS_DB, REDIS_HOST, REDIS_PORT


class DB(redis.Redis):
    def __init__(self):
        super().__init__(
            host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True
        )

        # Clear redis
        self.flushdb()

    def zget(self, name: str, position: int) -> str | None:
        response = cast(List[str], self.zrevrange(name, position, position))

        return response[0] if response else None


db = DB()
