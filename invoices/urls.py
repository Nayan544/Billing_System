from django.urls import path
from .views import create_invoice, invoice_detail, InvoiceListView, edit_invoice, invoiceDeleteView, invoice_pdf_view, add_payment


urlpatterns = [
    path('create/', create_invoice, name='invoice-create'),
    path('detail/<int:pk>/', invoice_detail, name='invoice-detail'),
    path('', InvoiceListView.as_view(), name='invoice-list'),
    path('edit/<int:pk>/', edit_invoice, name='invoice-edit'),
    path('delete/<int:pk>/', invoiceDeleteView.as_view(), name='invoice-delete'),
    path('pdf/<int:pk>/', invoice_pdf_view, name='invoice-pdf'),
    path('add-payment/<int:pk>/', add_payment, name='invoice-add-payment'),
]