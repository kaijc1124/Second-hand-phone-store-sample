from mysite.models import phone_shopped2
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

def payment_notification(sender, **kwargs):

    ipn_obj=sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        order_id=ipn_obj.invoice.split("-")[-1]
        print(order_id)

        order=phone_shopped2.objects.filter(User_account=order_id,paid="No")
        for o in order:
            o.paid="Yes"
            o.save()

valid_ipn_received.connect(payment_notification)