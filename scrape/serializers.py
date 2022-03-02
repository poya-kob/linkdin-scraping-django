import datetime

from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import LinkedinUsers


class LinkedinUsersSerializer(ModelSerializer):
    class Meta:
        model = LinkedinUsers
        fields = "__all__"


class HyperLinkedinUsersSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LinkedinUsers
        fields = "__all__"
        extra_kwargs = {
            'url': {'view_name': 'users_detail', 'lookup_field': 'pk'}}

    def update(self, instance, validated_data):
        ins = super().update(instance, validated_data)
        with open('linkedin.log', 'a') as ln:
            ln.writelines(
                f"{self.context['request'].user.username} -- updated record with id ({ins.id}) "
                f" at {datetime.datetime.now()}\n")
        return ins
