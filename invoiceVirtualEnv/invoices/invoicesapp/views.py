
from rest_framework.decorators import api_view
from rest_framework.response import Response
from invoicesapp.models import Invoice
from invoicesapp.serializers import InvoiceSerializer

#Use the decorator to specify which methods the invoice_list function is going to handle
@api_view(['GET']) 
#Function to return a list of invoices
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many = True)
        return Response(serializer.data)
