from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from .models import Cafe, Feedback
from django.db.models import Q
from rating.forms import CafeCreateForm, CafeUpdateForm, ReviewCreateForm
from django.contrib.auth.decorators import login_required


def home(request):
    context = {'cafe': Cafe.objects.all()}
    return render(request, 'rating/home.html', context)


def DetailCafe(request, cafe_slug):
    context = {}
    try:
        context["cafe"] = Cafe.objects.get(slug=cafe_slug)
        context["feedbacks"] = Feedback.objects.order_by('-date_posted')

    except Cafe.DoesNotExist:
        context["cafe"] = None
        context["feedbacks"] = Feedback.objects.order_by('-date_posted')

    return render(request, "rating/cafe_detail.html", context=context)


def ListCafe(request):
    return render(request, "rating/home.html",
                  context={"cafe": Cafe.objects.order_by('-date_posted')})

@login_required
def RegisterCafe(request):
    if request.method == "POST":
        form = CafeCreateForm(request.POST)
        if form.is_valid():
            cafe = form.save(commit=False)
            if "image" in request.FILES:
                cafe.image = request.FILES['image']
            cafe.author = request.user
            cafe.save()
            return redirect(reverse('cafe-detail', kwargs={'cafe_slug': cafe.slug}))
    else:
        form = CafeCreateForm()


    return render(request, "rating/cafe_form.html", context={"form": form})


def UpdateCafe(request, cafe_slug):
    cafe = Cafe.objects.get(slug=cafe_slug)
    if request.method == "POST":
        form = CafeUpdateForm(request.POST, instance=cafe)
        if form.is_valid():
            form.save(commit=False)
            if "image" in request.FILES:
                cafe.image = request.FILES['image']
            form.save()

            return redirect(reverse('rate-home'))
    else:
        form = CafeUpdateForm()


    return render(request, "rating/cafe_update.html", context={"form": form})


def DeleteCafe(request, cafe_slug):
    cafe = Cafe.objects.get(slug=cafe_slug)
    author = cafe.author

    if request.method == "POST" and request.user.is_authenticated and request.user == author:
        cafe.delete()
        return redirect(reverse('rate-home'))
    return render(request, 'rating/cafe_confirm_delete.html', context={'cafe': cafe, 'author': author})


def feedback(request):
    context = {'feedbacks': Feedback.objects.all()}
    return render(request, 'rating/cafe_detail.html', context)

@login_required
def WriteFeedback(request, cafe_slug):
    if request.method == "POST":
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.cafe = Cafe.objects.get(slug=cafe_slug)
            feedback.author = request.user
            feedback.save()
            return redirect(reverse('cafe-detail', kwargs={'cafe_slug': cafe_slug}))
    else:
        form = ReviewCreateForm()
    return render(request, 'rating/feedback_form.html', context={"form": form})


def about(request):
    return render(request, 'rating/about.html', {'title': 'about'})


def privacy(request):
    return render(request, 'rating/privacy.html', {'title': 'privacy'})


def terms(request):
    return render(request, 'rating/terms.html', {'title': 'terms'})


def contact(request):
    return render(request, 'rating/contact.html', {'title': 'contact'})


def faq(request):
    return render(request, 'rating/faq.html', {'title': 'faq'})

def search(request):

    if request.method == "GET":
        query = request.GET.get('search')
        submit_button = request.GET.get('submit')

        if query:
            cafes = Cafe.objects.all()

            keywords = query.split()

            for kw in keywords:

                # note: to add more, use Q((attribute)__icontains=kw) | \
                # where attribute is the attribute to search and | is
                # bitwise or. \ is just so i can write on the next line
                # without any errors.

                # check whether each attribute contains keyword.
                kwquery = Q(title__icontains=kw) | \
                          Q(address__icontains=kw) | \
                          Q(city__icontains=kw)
                cafes = cafes.filter(kwquery).distinct()

            context = {'cafes': cafes,
                       'submit_button': submit_button,
                       'feedbacks': Feedback.objects.all()}

            return render(request, 'rating/search.html', context)
        else:
            return render(request, 'rating/search.html')
    else:
        return render(request, 'rating/search.html')
