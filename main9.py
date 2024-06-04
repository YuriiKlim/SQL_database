import redis


r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

r.set('user:name', 'Alice')
name = r.get('user:name')
# print(name)

r.set('user:age', 7)
age = r.get('user:age')
# print(age)
# print(type(age))

r.incr('user:age', 3)
age = r.get('user:age')
# print(age)
# print(type(age))

r.geoadd('cities', (30.1455, 50.4566, 'Ternopil'))
r.geoadd('cities', (60.1455, 70.4566, 'London'))

pos = r.geopos('cities', 'Ternopil', 'London')
# print(pos)
# print(type(pos))

dist = r.geodist('cities', 'Ternopil', 'London', 'km')
# print(dist)
# print(type(dist))

r.rpush('items', 1, 2, 3)
items = r.lrange('items', 0, -1)
# print(items, type(items))
r.delete('items')

r.sadd('items', 1, 2, 3)
items = r.smembers('items')
print(items, type(items))
r.delete('items')

r.hset('items', 'name', 'Alice')
r.hset('items', 'age', 12)