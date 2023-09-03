import sys,os

os.system("pkg install redis")
from redis import StrictRedis

db = StrictRedis(decode_responses=True)
