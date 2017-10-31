from rest_framework import serializers
from . import models 


class ThreadSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Thread
		fields = ('id', 'title', 'description')

