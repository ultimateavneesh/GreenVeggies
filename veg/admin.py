from django.contrib import admin

# Register your models here.
from .models import Vendor, Customer

admin.site.register(Customer)



class VendorDetails(admin.ModelAdmin):
    fieldsets = (
        ("Personal Details", {
            "fields": (
                'vendor_firstname','vendor_lastname','vendor_username','vendor_contact',
                'vendor_email','vendor_address','vendor_city','vendor_state','vendor_zip'
            ),
        }),

        ("Products Prices", {
            "fields": (
                'apple','banana','broccoli','cabbage','capsicum','carrot','cauliflower',
                'chilly','coriander','cucumber','garlic','ginger','grapes','guava','jackfruit',
                'lemon','lychee','mango','mushroom','onion','orange','papaya','pear','pea',
                'pineapple','pomegranate','potato','pumpkin','scallion','spinach','tomato',
                'turnip','watermelon'
            ),
        }),
    )
admin.site.register(Vendor,VendorDetails)