from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemFormSet, InvoicePaymentForm
from django.views.generic import ListView, DeleteView
from django.forms import inlineformset_factory
from django.urls import reverse_lazy

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            invoice = form.save()
            items = formset.save(commit=False)
            for item in items:
                item.invoice = invoice
                item.save()
            return redirect('invoice-detail', invoice.id)
    else:
        form = InvoiceForm()
        formset = InvoiceItemFormSet()
    return render(request, 'invoices/invoice_form.html', {'form': form, 'formset': formset})

def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoices/invoice_detail.html', {'invoice': invoice})


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoices/invoice_list.html'
    context_object_name = 'invoices'
    ordering = ['-date']


class invoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoices/invoice_delete.html'
    success_url = reverse_lazy('invoice-list')


def add_payment(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoicePaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.invoice = invoice
            payment.save()
            return redirect('invoice-detail', pk=invoice.pk)
    else:
        form = InvoicePaymentForm()
    return render(request, 'invoices/add_payment.html', {'form': form, 'invoice': invoice})


def edit_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    InvoiceItemFormSet = inlineformset_factory(
        Invoice, InvoiceItem,
        fields=['product', 'quantity'],
        extra=0,  # no extra blank forms
        can_delete=True
    )

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        formset = InvoiceItemFormSet(request.POST, instance=invoice)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('invoice-detail', pk=invoice.pk)
    else:
        form = InvoiceForm(instance=invoice)
        formset = InvoiceItemFormSet(instance=invoice)

    return render(request, 'invoices/invoice_edit.html', {
        'form': form,
        'formset': formset,
        'invoice': invoice,
    })
