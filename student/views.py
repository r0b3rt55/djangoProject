from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.filters import StudentFilter
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student
from trainer.models import Trainer


# CreateView- adaugarea si salvarea datelor in tabela respectiva pe baza unui formular generat in interfata


class StudentCreateView(CreateView):
    template_name = 'student/create_student.html'  # calea catre pagina .html unde va fi afisat formularul
    model = Student
    form_class = StudentForm
    permission_required = 'student.add_student'
    #success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_student = form.save(commit=False)
            new_student.first_name = new_student.first_name.title()
            new_student.save()

        return redirect('list-of-students')


# ListView - randam/afisam date dintr-o tabela

class StudentListView(ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'students' # Student.objects.all()

    # def get_queryset(self):
    #     return Student.objects.filter(active=False)

# UpdateView- actualizam datele unei inregistrari salvate in tablea pe baza unui formular

    def get_queryset(self):
        return Student.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super(StudentListView, self).get_context_data(**kwargs)
        # all_trainers = Trainer.objects.all() # pe baza unui query am putut trimite date in pagina html
        # data['trainers'] = all_trainers
        # print(data)

        all_students = Student.objects.filter(active=True)
        myFilter = StudentFilter(self.request.GET, queryset=all_students)
        data['students'] = myFilter.qs
        data['filters'] = myFilter.form

        return data

class StudentUpdateView(UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    #success_url = reverse_lazy('list-of-students')  # daca folosesti def get_success_url nu mai folosim variabila success_url care

    def get_success_url(self):  # redirectionare catre o alta pagina sau aceeasi pagina, in special daca aveti pk. Daca un user este autentificat puteti sa redirectionati catre o alta pagina in functie de grupul de care care apartine
        return reverse('update-student', args=[str(self.object.id)])


class StudentDeleteView(DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')


class StudentDetailView(DetailView):
    template_name = 'student/details_student.html'
    model = Student

def delete_student_modal(request, pk):
    Student.objects.filter(id=pk).delete()
    # Student.objects.filter(id=pk).update(active=False)
    return redirect('list-of-students')

def search(request):
    get_value = request.GET.get('search')
    students = Student.objects.filter(Q(first_name__icontains=get_value) | Q(email__icontains=get_value))

    return render(request, 'home/search_form.html', {'all_students': students})