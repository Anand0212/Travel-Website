from django.contrib import admin
from .models import EventFull, Enroll, Payment
# Register your models here.

admin.site.register(EventFull)
admin.site.register(Enroll)
admin.site.register(Payment)

class PaymentAdmin(admin.ModelAdmin):
    list_display=['user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'paid']