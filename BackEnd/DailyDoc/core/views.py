from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .CoreGemini import LLM_function

@permission_classes([IsAuthenticated]) 
class ChatView(APIView):
    def post(self, request):
        user_input = request.data.get("message")

        if not user_input:
            return Response({"error": "No input message provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            reply = LLM_function(user_input)
            return Response({"reply": reply}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
