from django.shortcuts import render
from django.views.generic import FormView, TemplateView, UpdateView, View
import json
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt, csrf_protect


class HomeView(TemplateView):
    template_name = ''

    def get(self, request, *args, **kwargs):
        return render("Welcome to Enoch International")
