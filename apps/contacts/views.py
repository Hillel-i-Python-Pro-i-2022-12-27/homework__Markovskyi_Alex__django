from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from apps.contacts.models import Contact


# Create your views here.
class ContactListView(ListView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "username",
        "name",
        "birthdate",
        "sex",
        "ssn",
        "company",
        "job",
        "mail",
        "telephone",
        "address",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_class")


class ContactDetailView(DetailView):
    model = Contact
    fields = (
        "pk",
        "username",
        "name",
        "birthdate",
        "sex",
        "ssn",
        "company",
        "job",
        "mail",
        "telephone",
        "address",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_class")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "username",
        "name",
        "birthdate",
        "sex",
        "ssn",
        "company",
        "job",
        "mail",
        "telephone",
        "address",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_class")


class ContactDeleteView(DeleteView):
    model = Contact
    fields = (
        "pk",
        "username",
        "name",
        "birthdate",
        "sex",
        "ssn",
        "company",
        "job",
        "mail",
        "telephone",
        "address",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_class")
