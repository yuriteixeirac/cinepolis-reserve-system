from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User


@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({
            'error': 'All fields are mandatory.'
        }, status=400)

    try:
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=400)

    return Response({
        'id': user.pk,
        'username': user.username,
        'email': user.email
    }, status=201)
