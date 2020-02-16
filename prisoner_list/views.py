from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Prisoner
from django.template import loader
from django.shortcuts import redirect


def index(request):
    prisoner_list = Prisoner.objects.order_by("code")
    template = loader.get_template("prisoners.html")
    context = {
        "prisoner_list": prisoner_list
    }
    return HttpResponse(template.render(context, request))


def delete(request, prisoner_id):
    Prisoner.objects.get(pk=prisoner_id).delete()
    return redirect('/prisoner-list')


def add_prisoner(request):
    data = request.POST
    code = data.get('code', '')
    if not is_int(code):
        return HttpResponse("El código no es un número")
    else:
        code = int(code)
    if user_exists(code):
        return HttpResponse("El usuario ya existe")
    name = data.get('name', '')
    date = data.get('date', '')
    gender = data.get('gender', '')
    race = data.get('race', '')
    Prisoner.objects.create(
        code=code, name=name, birth_date=date, gender=gender, race=race
    ).save()
    return redirect('/prisoner-list')


def user_exists(prisoner_id):
    prisoner = Prisoner.objects.get(pk=prisoner_id)
    return prisoner is not None


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
