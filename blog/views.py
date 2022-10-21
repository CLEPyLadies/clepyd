from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    """Placeholder"""
    return HttpResponse("Hello, world. You're at the posts index.")


@login_required
def post_new(request):
    """Create new post"""
