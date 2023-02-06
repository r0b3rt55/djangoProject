from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from trainer.filers import TrainerFilter
from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer

# Create your views here.


class TrainerCreateView(CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('home')


class TrainerListView(ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'trainers'

    def get_queryset(self):
        return Trainer.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super(TrainerListView, self).get_context_data(**kwargs)
        # all_trainers = Trainer.objects.all() # pe baza unui query am putut trimite date in pagina html
        # data['trainers'] = all_trainers
        # print(data)

        all_trainers = Trainer.objects.filter(active=True)
        myFilter = TrainerFilter(self.request.GET, queryset=all_trainers)
        data['trainers'] = myFilter.qs
        data['filters'] = myFilter.form

        return data


class TrainerUpdateView(UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm

    def get_success_url(self):  # redirectionare catre o alta pagina sau aceeasi pagina, in special daca aveti pk. Daca un user este autentificat puteti sa redirectionati catre o alta pagina in functie de grupul de care care apartine
        return reverse('update-trainer', args=[str(self.object.id)])

class TrainerDeleteView(DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')

class TainerDetailView(DetailView):
    template_name = 'trainer/details_trainer.html'
    model = Trainer

def delete_trainer_modal(request, pk):
    Trainer.objects.filter(id=pk).delete()
    # Student.objects.filter(id=pk).update(active=False)
    return redirect('list-of-trainers')