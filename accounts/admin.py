from django.contrib import admin
from .models import *

admin.site.site_header = "Tuffy's Library Administration"
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(IssueOrder)
admin.site.register(ReturnOrder)

