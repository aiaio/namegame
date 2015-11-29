from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views import generic

from rest_framework import viewsets, generics

from names.models import Name
from names.forms import NameForm
from names.serializers import NameSerializer

MAX_NAMES = settings.MAX_NAMES

class NameDetail(generic.edit.UpdateView):
    """
    Render a random name from the Name table.
    """
    model = Name
    template_name = 'names/name_detail.html'
    success_url = reverse_lazy("play")
    fields = ('name','used',)

    def get_object(self):
        if self.request.POST.get('pk'):
            return Name.objects.get(pk=self.request.POST.get('pk'))
        else:
            return Name.objects.get_unused_random()
        
    def form_valid(self, form):
        if 'correct_count' in self.request.session:
            self.request.session['correct_count'] += 1
        else:
            # edge case where we went to /play before a visit to /ready at the start of a game
            # just set it to 1 correct
            self.request.session['correct_count'] = 1
        return super(NameDetail, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(NameDetail, self).get_context_data(**kwargs)
        if 'correct_count' in self.request.session:
            context['correct_count'] = self.request.session['correct_count']
        return context


class NameCreate(SuccessMessageMixin, generic.edit.CreateView):
    model = Name
    template_name = "names/name_form.html"
    form_class = NameForm
    success_url = reverse_lazy("home")
    success_message = "%(calculated_field)s added!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.name,
        )

    def form_valid(self, form):
        if 'added_count' in self.request.session:
            self.request.session['added_count'] += 1
        else:
            # first time, have not added any yet
            self.request.session['added_count'] = 1
        return super(NameCreate, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(NameCreate, self).get_context_data(**kwargs)
        if 'added_count' in self.request.session:
            context['added_count'] = self.request.session['added_count']
        else:
            context['added_count'] = 0
        context['max_names'] = MAX_NAMES
        return context


class Ready(generic.TemplateView):
    template_name = "names/ready.html"

    def get_context_data(self, **kwargs):
        context = super(Ready, self).get_context_data(**kwargs)
        if 'correct_count' in self.request.session:
            context['correct_count'] = self.request.session['correct_count']
            self.request.session['correct_count'] = 0
        return context


class NameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows names to be viewed or edited.
    """
    queryset = Name.objects.all().order_by('used')
    serializer_class = NameSerializer


#class RandomNameViewSet(gerics..ReadOnlyModelViewSet):
class RandomNameView(generics.RetrieveAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer

    def get_queryset(self):
        return Name.objects.get_unused_random()
