from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from search.forms import SearchForm


def search_view(request):
    form = SearchForm(request.GET) if request.GET else SearchForm()

    if form.is_valid():
        return redirect('search:flights')

    return render(request, 'search/search.html', {'form': form})


class Search(TemplateView):
    form_class = SearchForm
    template_name = 'search/search.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['form'] = SearchForm(self.request.GET) if self.request.GET else SearchForm()
        return ctx

    def get(self, request, *args, **kwargs):
        print(request.GET, request.content_params)
        form = SearchForm(request.GET)

        if form.is_valid():
            return redirect('search:flights', )
        return super().get(request, *args, **kwargs)


class FlightsView(FormView):
    form_class = SearchForm
    template_name = 'search/results.html'
    success_url = reverse_lazy('search:flights')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)