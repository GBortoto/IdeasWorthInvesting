from iwi_real.models import Thread
from iwi_real.serializers import ThreadSerializer

from rest_framework import generics


class ThreadList(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class ThreadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
