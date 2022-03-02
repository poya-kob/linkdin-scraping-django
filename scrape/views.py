import datetime

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from linkedin_scraper import Person, actions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from .models import LinkedinUsers
from .serializers import LinkedinUsersSerializer, HyperLinkedinUsersSerializer


class ApiRequestLinkedin(APIView):
    # driver = webdriver.Chrome(executable_path="https://1drv.ms/u/s!AhcQ8FdkJdfZpgB9HvEYQGJkCbx2?e=IWoZeu")
    driver = webdriver.Chrome(executable_path="/home/poya/chromedriver")
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    def get(self, request):
        email = request.data.get('email', False)
        password = request.data.get('password', False)
        url = request.data.get('url', False)
        if email and password and url:
            got_user = LinkedinUsers.objects.filter(email=email).first() or False
            if got_user:
                actions.login(self.driver, email, password)
                person = Person(url, scrape=True, driver=self.driver)
                got_user.about = person.about
                got_user.experiences = person.experiences
                got_user.contacts = person.contacts
                got_user.save()
                serializer = LinkedinUsersSerializer(got_user)
                return Response(serializer.data)
            else:
                actions.login(self.driver, email, password)
                person = Person(url, scrape=True, driver=self.driver)
                created_user = LinkedinUsers.objects.create(name=person.name, about=person.about,
                                                            email=email, experiences=person.experiences,
                                                            contacts=person.contacts)
                serializer = LinkedinUsersSerializer(created_user)
                return Response(serializer.data)
        else:
            return Response({'message': 'email, password, url required'})


class LinkedinUsersList(ListAPIView):
    queryset = LinkedinUsers.objects.all()
    serializer_class = HyperLinkedinUsersSerializer


class LinkedinUsersDetail(RetrieveUpdateDestroyAPIView):
    queryset = LinkedinUsers.objects.all()
    serializer_class = HyperLinkedinUsersSerializer

    def delete(self, request, *args, **kwargs):
        with open('linkedin.log', 'a') as ln:
            ln.writelines(
                f"{request.user.username} has deleted record with id ({kwargs['pk']}) "
                f" at {datetime.datetime.now()}\n")
        return super().delete(request, *args, **kwargs)
