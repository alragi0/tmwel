import sys,os

os.system("redis-cli")
from redis import StrictRedis

db = StrictRedis(decode_responses=True)
