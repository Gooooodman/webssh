# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    # import ipdb;ipdb.set_trace()
    return render(request, 'index.html')

