from django.shortcuts import render, redirect
import requests
from .models import dataset


def index(request):
    questions1 = ['Gender', 'Age',
                 'What is your monthly allowance and/or salary?',
                 'You are studying (or what you would like to study in the future OR what you studied)...',
                 'Hobbies and interests',
                 'You are more... ',
                 'Favourite music genre? ',
                 'Favourite movie genre? ',
                 'What gift would you love to receive the most out of these options?'

                 ]


    return render(request, 'questions/questions.html',questions1 )