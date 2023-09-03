from redis import StrictRedis
import os

# استخدم المتغير CACHE_HOST للحصول على عنوان خادم Redis من المتغيرات البيئية
cache_host = os.environ.get("CACHE_HOST")

# قم بتكوين اتصال قاعدة البيانات Redis باستخدام المتغير CACHE_HOST
db = StrictRedis(host=cache_host, decode_responses=True)
