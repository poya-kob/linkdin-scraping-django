import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login


class LoginUsersView(APIView):
    def post(self, request):
        username = request.data.get('username', False)
        password = request.data.get('password', False)
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                with open('linkedin.log', 'a') as ln:
                    ln.writelines(f'{user.username} -- at  {datetime.datetime.now()}\n')
                return redirect(reverse('users_list'))

        return Response({'message': 'username or password incorrect'})
