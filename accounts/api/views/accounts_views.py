from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers.accounts_serializers import AccountSerializer
from accounts.models import Account


class AccountAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CreateAccount(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class UpdateAccount(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RetrieveAccount(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class DestroyAccount(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
