import redis
from django.conf import settings

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT , charset="utf-8", decode_responses=True, db=0)