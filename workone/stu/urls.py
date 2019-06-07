from django.conf.urls import url

from stu import views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^showall/$',views.showall_view),
    url(r'^getstu/$',views.getstu_view)

]