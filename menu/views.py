from rest_framework import viewsets

from menu.models import Menu
from menu.serializers import MenuSerializer


# Create your views here.
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
