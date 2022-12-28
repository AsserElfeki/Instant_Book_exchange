from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from authentication.models import BookReader
from .serializers import StartTransaction


from rest_framework import generics, status

# View should save these books in serializer and get book_reder_receiver
# token
# book that wants to be received <pk>
# book that will be given <pk>
class StartTransactionView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StartTransaction

    def post(self, request, *args, **kwargs):
        user = request.data
        # serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # user_data = serializer.data
        return Response({"response": f"{user}"},status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        book_reader_initiator = BookReader.objects.get(user=self.request.user)
        serializer.save(book_reader_initiator=book_reader_initiator)
