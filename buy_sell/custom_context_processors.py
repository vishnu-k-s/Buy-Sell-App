from notifications_app.models import BroadcastNotification
from .models import Product
def notifications(request):
    allnotifications = BroadcastNotification.objects.all()
    return {'notifications': allnotifications}