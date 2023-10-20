from order.models import Order
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class UpdateOrder(UpdateView):
    model = Order
    fields = '__all__'
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this order.")
        return obj
