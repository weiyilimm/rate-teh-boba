from django.shortcuts import render
from .models import Cafe, Feedback
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



def home(request):
    context = {'cafe': Cafe.objects.all()}
    return render(request,'rating/home.html',context)

class CafeListView(ListView):
    model = Cafe
    template_name = 'rating/home.html'
    context_object_name = 'cafe'
    ordering = ['-date_posted']


class CafeDetailView(DetailView):
    model = Cafe


class CafeCreateView(LoginRequiredMixin, CreateView):
    model = Cafe
    fields = ['title', 'address', 'city','phone','email', 'content' , 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CafeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cafe
    fields = ['title', 'address', 'city','phone','email', 'content' , 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cafe = self.get_object()
        if self.request.user == cafe.author:
            return True
        return False


class CafeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cafe
    success_url = '/'

    def test_func(self):
        cafe = self.get_object()
        if self.request.user == cafe.author:
            return True
        return False

def feedback(request):
    context = {'feedbacks': Feedback.objects.all()}
    return render(request,'rating/cafe_detail.html',context)

class FeedbackListView(ListView):
    model = Feedback
    template_name = 'cafe_detail.html'
    context_object_name = 'feedbacks'
    ordering = ['-date_posted']

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['comment']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request,'rating/about.html',{'title':'about'})

def privacy(request):
    return render(request,'rating/privacy.html',{'title':'privacy'})

def terms(request):
    return render(request,'rating/terms.html',{'title':'terms'})

def contact(request):
    return render(request,'rating/contact.html',{'title':'contact'})
