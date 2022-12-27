from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from authentication.models import BookReader
from .serializers import StartTransaction


from rest_framework import generics, status

# Post will expect 2 books to be given here.
# View should save these books in serializer and get book_reder_receiver
class StartTransactionView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StartTransaction

    def perform_create(self, serializer):
        book_reader_initiator = BookReader.objects.get(user=self.request.user)
        serializer.save(book_reader_initiator=book_reader_initiator)
