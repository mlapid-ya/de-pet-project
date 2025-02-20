from loguru import logger

from de_pet_project.shared_utils.redis_client import RedisClient

class RedisProducer(RedisClient):
    '''
    Redis producer
    '''

    def __init__(self, stream_name: str):
        super().__init__(stream_name)

    async def __ainit__(self) -> None:
        await super().__ainit__()

    async def produce_message(self, message: str) -> None:
        await self._redis_client.xadd(name=self.stream_name, fields={'message': message})

    async def close(self) -> None:
        await self._redis_client.flushall(asynchronous=True)
        await self._redis_client.aclose()
        logger.info(f"{self} is closed.")