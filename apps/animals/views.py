from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.animals.models import Animal


# Create your views here.
def list_animals(request):
    return render(
        request=request,
        template_name="animals/animal_list.html",
        context={
            "object_list": Animal.objects.all(),
        },
    )


class AnimalListView(ListView):
    model = Animal
    # queryset = Animal.objects.all().order_by('-modified_at')


class AnimalCreateView(CreateView):
    model = Animal
    fields = (
        "name",
        "age",
        "is_auto_generated",
    )
    success_url = reverse_lazy("animals:list_by_class")


class AnimalUpdateView(UpdateView):
    model = Animal
    fields = (
        "name",
        "age",
        "is_auto_generated",
    )
    success_url = reverse_lazy("animals:list_by_class")


class AnimalDeleteView(DeleteView):
    model = Animal
    fields = (
        "name",
        "age",
        "is_auto_generated",
    )
    success_url = reverse_lazy("animals:list_by_class")
