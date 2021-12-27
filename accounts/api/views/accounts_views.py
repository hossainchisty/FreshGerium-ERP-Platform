from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers.accounts_serializers import AccountSerializer
from accounts.models.account_models import Account


class AccountAPIView(generics.ListAPIView):
    '''
    ♻API endpoint that allows accounts to be viewed.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CreateAccount(generics.CreateAPIView):
    '''
    ♻API endpoint that allows accounts to be created.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class UpdateAccount(generics.UpdateAPIView):
    '''
    ♻API endpoint that allows accounts to be updated.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RetrieveAccount(generics.RetrieveAPIView):
    '''
    ♻API endpoint that allows accounts to be retrieved.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class DestroyAccount(generics.DestroyAPIView):
    '''
    ♻API endpoint that allows accounts to be deleted.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
