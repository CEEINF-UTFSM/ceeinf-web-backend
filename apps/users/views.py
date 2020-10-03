# import de third party
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# import de framework
from django.contrib.auth import authenticate, login

# import de mi proyecto
from .serializers import UserLoginSerializer


class UserView(APIView):

    def post(self, request):
        user_data = request.data
        serializer = UserLoginSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.data
        user = authenticate(request, **valid_data)
        if user is not None:
            login(request, user)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
