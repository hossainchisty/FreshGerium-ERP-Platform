from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from expense.models import Expense


class DeleteExpense(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense_item')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this expense.")
        return obj
