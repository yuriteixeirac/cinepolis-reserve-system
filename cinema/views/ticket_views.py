from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from redis import Redis
from cinema.models import Seat, Ticket, Session

redis = Redis()
RESERVATION_TIME = 600  # 10 minutes


@api_view(['POST'])
def purchase_ticket(request, session_id, seat_id):
    key = f'seat_lock:{session_id}:{seat_id}'
    user_id = str(request.user.id)

    reserved_seat = redis.get(key)

    if reserved_seat:
        if reserved_seat.decode() != user_id:   # type: ignore
            return Response({
                'error': 'Seat already reserved by another user.'
            }, status=409)
    
    with transaction.atomic():
        session = get_object_or_404(Session, pk=session_id)

        seat = Seat.objects.select_for_update().get(
            pk=seat_id,
        )

        if seat.room_id != session.room_id:     # type: ignore
            return Response({
                'Seat does not belong to this session.'
            }, status=400)

        if Ticket.objects.filter(session=session, seat=seat).exists():
            return Response({
                'error': 'Seat already sold.'
            }, status=409)

        Ticket.objects.create(
            user=request.user,
            session=session,
            seat=seat
        )
    
    if reserved_seat:
        if reserved_seat.decode() == user_id:   # type: ignore
            redis.delete(key)

    return Response({
        'success': 'Ticket bought successfully.'
    }, status=201)


@api_view(['POST'])
def reserve_ticket(request, session_id, seat_id):
    key = f'seat_lock:{session_id}:{seat_id}'
    user_id = str(request.user.id)

    session = get_object_or_404(Session, pk=session_id)    
    seat = get_object_or_404(Seat, pk=seat_id)

    if seat.room_id != session.room_id:     # type: ignore
        return Response({
            'Seat does not belong to this session.'
        }, status=400)

    if Ticket.objects.filter(session=session, seat=seat).exists():
        return Response({
            'error': 'Seat is already purchased.'
        }, status=409)

    success = redis.set(
        key, user_id, ex=RESERVATION_TIME, nx=True
    )

    if not success:
        reserved_seat = redis.get(key)
        reserved_user = reserved_seat.decode() if reserved_seat else None   # type: ignore

        if reserved_user == user_id:
            return Response({
                'error': 'You already reserved this seat.'
            }, status=409)
        
        return Response({
            'error': 'Seat already reserved.'
        }, status=409)

    return Response({
        'success': 'Reserved seat successfully.'
    }, status=201)
