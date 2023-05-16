from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField

from django.db import models
from suppliers.models import Supplier
from utils import random
from utils.models.common_fields import Timestamp

from .category_model import Category
from .unit_model import Unit


class Product(Timestamp):
    """ Product model for storing product data🛢 """
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=4, unique=True, null=True, blank=True)
    product_model = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_description = RichTextField()
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.IntegerField(default=0)
    image = CloudinaryField('Product Images', null=True, blank=True)
    barcode = CloudinaryField('barcode/', blank=True, null=True)
    qrcode = CloudinaryField('qrcode/', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    out_of_stock = models.BooleanField(default=False)
    mfg_date = models.DateField(
        help_text='The MFG date is the date the product was manufactured, or the Manufacturing Date (MFG). It is not an expiration date.',
        null=True, blank=True,
    )
    exp_date = models.DateField(
        help_text='An expiration date is the last day that a consumable product such as food or medicine.',
        null=True, blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=[('out of stock', 'Out of Stock'), ('in stock', 'In Stock')],
        default='In stock'
    )

    hard_disk_size = models.CharField(
        verbose_name='Hard Disk Size',
        max_length=100,
        help_text='Example: 256 GB',
        null=True, blank=True,
    )
    screen_size = models.CharField(
        verbose_name='Screen Size',
        max_length=100,
        help_text='13.3 Inches, 15.6 Inches, etc.',
        null=True, blank=True,
    )
    operating_system = models.CharField(
        verbose_name='Operating System',
        max_length=10,
        help_text='Example: Windows, Mac, Linux, etc.',
        null=True, blank=True,
    )
    cpu_manufacturer = models.CharField(
        verbose_name='CPU Manufacturer',
        max_length=30,
        help_text='Apple, Intel, AMD, etc.',
        null=True, blank=True,
    )
    connectivity_technology = models.CharField(
        verbose_name='Connectivity Technology',
        max_length=40,
        help_text='Bluetooth, Wi-Fi, USB, Ethernet, etc.',
        null=True, blank=True,
    )
    uses_for_product = models.CharField(
        verbose_name='Specific Uses For Product',
        max_length=50,
        help_text='Personal, Gaming, Business, etc.',
        null=True, blank=True,
    )
    brand_name = models.CharField(
        verbose_name='Brand Name',
        max_length=50,
        help_text='Example: Apple, Samsung, Sony, LG, etc.',
        null=True, blank=True,
    )
    manufacturer = models.CharField(
        verbose_name='Manufacturer',
        max_length=50,
        help_text='Example: Apple, Samsung, LG, Sony, etc.',
        null=True, blank=True,
    )
    size = models.CharField(
        verbose_name='Size',
        max_length=10,
        help_text="The numeric or text version of the item's size. Example: Small, Medium, Large, X-Large, XX-Large, etc.",
        null=True, blank=True
    )
    weight = models.CharField(
        verbose_name='Weight',
        max_length=10,
        help_text="The numeric or text version of the item's weight. Example: 1.5 lbs, 2.5 lbs, etc.", null=True, blank=True,
    )
    height = models.CharField(
        verbose_name='Height',
        max_length=10,
        help_text="The numeric or text version of the item's height. Example: 1.5 inches, 2.5 inches, etc.",
        null=True, blank=True
    )
    color = models.CharField(
        verbose_name='Color',
        max_length=10,
        help_text='The color of the item. Example: Red, Blue, Green, etc.',
        null=True, blank=True
    )
    shape = models.CharField(
        verbose_name='Shape',
        max_length=10,
        help_text='The shape of the item. Example: Round, Square, Oval, etc.',
        null=True, blank=True
    )
    material_type = models.CharField(
        verbose_name='Material Type',
        max_length=10,
        help_text="what material is the product made out of? '\n Example: plastic, metal, wood, etc.", null=True, blank=True
    )
    count_sold = models.IntegerField(default=0)
    country = CountryField(blank_label='(select country)')
    recently_sold = models.DateTimeField(null=True, blank=True)
    recently_added = models.DateTimeField(null=True, blank=True)
    recently_viewed = models.DateTimeField(null=True, blank=True)
    recently_updated = models.DateTimeField(null=True, blank=True)
    supplier_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        """ override the save method for logical purposes """
        if self.in_stock != 0:
            self.status = 'in stock'
            self.out_of_stock = False
        else:
            self.status = 'out of stock'
            # if out of stock, set out_of_stock flag to True
            self.out_of_stock = True
        # Save the product with a random product code.
        self.product_code = random.unique_code(4)
        super(Product, self).save(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        # Only set user during the first save.
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.product_name}'
