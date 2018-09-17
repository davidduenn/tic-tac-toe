import redis
from time import sleep

r = redis.Redis(host="localhost")

for row in r.keys('*'):
	print(row + ' - ' + r.get(row))
