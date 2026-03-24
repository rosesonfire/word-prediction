import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

FILE_NAME = "assets/corpus/treasure-island.txt"  # Update this to run the code

db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
