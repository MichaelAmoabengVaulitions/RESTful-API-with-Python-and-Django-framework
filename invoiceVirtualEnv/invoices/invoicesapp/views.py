from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from invoicesapp.models import Invoice
from invoicesapp.serializers import InvoiceSerializer

#Use the decorator to specify which methods the invoice_list function is going to handle
@api_view(['GET', 'POST',])
#Function to return a list of invoices
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many = True)
        return Response(serializer.data)
    #Handling a post request
    elif request.method == 'POST':
        serializer = InvoiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)




#Get a single invoice details
#Modifying this function to handle a put and delete request
@api_view(['GET', 'PUT', 'DELETE'])
def invoice_detail(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except InvoiceDoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
    #Handling a put request
    elif request.method == 'PUT':
        serializer = InvoiceSerializer(invoice, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)

    #Handling a delete request
    elif request.method == 'DELETE':
        invoice.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
