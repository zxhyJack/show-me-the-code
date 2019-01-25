# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中

import redis
from coupon_01 import generate_verification


def get_connection():
    # 连接池
    pool = redis.ConnectionPool(
        host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r


def get_member(r):
    return r.smembers('keys')


def add_member(r, value):
    for key in keys:
        r.sadd('keys', key)


if __name__ == '__main__':
    keys = generate_verification(200, 10)
    r = get_connection()
    add_member(r, keys)
    result = get_member(r)
    print(result)
