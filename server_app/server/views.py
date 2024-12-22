from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .models import Note
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddNoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:

            data = request.data
            title = data.get('title')
            note = data.get('content')
            user = request.user
            if not title or not note:
                return Response({"error": "Title and content are required"}, status=status.HTTP_400_BAD_REQUEST)

            # Save the note to the database
            Note.objects.create(title=title, note=note, user=user)
            return Response({"message": "Note added successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserDataView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this

    def get(self, request):
        user = request.user  # Get the authenticated user
        return Response({
            'id': user.id,
            'username': user.username
        })