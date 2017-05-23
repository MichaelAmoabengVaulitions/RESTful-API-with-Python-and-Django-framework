#Importing the necessary dependencies
from django.conf.urls import url
from invoicesapp import views

urlpatterns = [
    url(r'^invoices/$', views.invoice_list)
]
