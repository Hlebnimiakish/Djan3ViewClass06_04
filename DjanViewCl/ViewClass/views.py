from django.shortcuts import render
from django.views import View
from ViewClass.form import Someform
from django.http import HttpResponseRedirect
from django.urls import reverse

class FormView(View):
    def get(self, request):
        form = Someform()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        dict = request.POST.dict()
        for k in dict:
            print(f'{k}:{dict[k]}')
        return HttpResponseRedirect(reverse('formpageget'))
