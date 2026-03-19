from celery import shared_task
from redis import Redis


redis = Redis()

@shared_task
def expire_reservation_fallback(session_id, seat_id, user_id):
    key = f'seat_lock:{session_id}:{seat_id}'
    current = redis.get(key)

    if current and current.decode() == str(user_id):    # type: ignore
        redis.delete(key)
