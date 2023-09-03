from redis import StrictRedis
DATABASE_URL=${{Postgres.DATABASE_URL}}
CACHE_HOST=${{Redis.REDISHOST}}
PRISMA_DB=${{Postgres.DATABASE_URL}}?connection_limit=100
db = StrictRedis(decode_responses=True)
