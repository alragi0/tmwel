import os
from redis import StrictRedis

# استخدم المتغيرات البيئية بدلاً من البنية التي قدمتها
DATABASE_URL = os.environ.get('Postgres.DATABASE_URL')
CACHE_HOST = os.environ.get('Redis.REDISHOST')
PRISMA_DB = f'{DATABASE_URL}?connection_limit=100'

# قم بإنشاء اتصال بقاعدة البيانات Redis باستخدام المتغيرات البيئية
db = StrictRedis(decode_responses=True)
