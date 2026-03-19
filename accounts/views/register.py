from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import RegisterSerializer, UserSerializer



class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer


    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.create(
                username=serializer.validated_data.get('username'), 
                email=serializer.validated_data.get('email')
            )
            user.set_password(serializer.validated_data.get('password'))
            user.save()
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=400)

        return Response(UserSerializer(user).data, status=201)
