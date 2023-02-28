from django.urls import path
from views import IndexView

urlpatterns = [

    path("home/", NomeDaView.as_view(), name ="index"),

]
