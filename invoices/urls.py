from django.urls import path
from .views import create_invoice, invoice_detail, InvoiceListView, edit_invoice, add_payment, invoiceDeleteView


urlpatterns = [
    path('create/', create_invoice, name='invoice-create'),
    path('detail/<int:pk>/', invoice_detail, name='invoice-detail'),
    path('', InvoiceListView.as_view(), name='invoice-list'),
    path('edit/<int:pk>/', edit_invoice, name='invoice-edit'),
    path('delete/<int:pk>/', invoiceDeleteView.as_view(), name='invoice-delete'),
    path('add-payment/<int:pk>/', add_payment, name='invoice-add-payment'),
]