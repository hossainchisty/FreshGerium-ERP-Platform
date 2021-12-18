from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from products.models import Category


class UpdateCategory(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('category_list')
