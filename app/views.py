from django.shortcuts import render, redirect
from app.models import State, StateCapital, City 
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.html import escape
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from app.forms import CitySearchForm, CityCreate, EditCity, EditState
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def delete_city(request,pk):

    City.objects.get(pk=pk).delete()

    return redirect ('/city_list/')
 
@login_required
def delete_state(request,pk):

    State.objects.get(pk=pk).delete()

    return redirect ('/state_list/')

@login_required
def edit_state(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    form = EditState(request.POST or None, instance=state)

    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list')

    return render (request,'state_edit.html',context)


@login_required
def edit_city(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city

    form = EditCity(request.POST or None, instance=city)

    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/city_list')

    return render (request,'city_edit.html',context)




def create_city(request):
    context = {}

    form = CityCreate(request.GET)


    context['form'] = form
    if form.is_valid():
        form.save()

    return render(request,'create_city.html', context)



def city_search_post(request):

    context = {}

    form = CitySearchForm(request.POST)

    context['form'] = form

    print request.method

    if request.method == 'POST':
        if form.is_valid():
            city = form.cleaned_data.get('city','')
            state = form.cleaned_data.get('state','') 

            context['cities'] = City.objects.filter(name=city, state__name=state)


    return render(request, 'city_search_post.html', context)




def city_search(request):

    context = {}

    form = CitySearchForm(request.GET)
    
    if form.is_valid():

        state = form.cleaned_data.get('state', '')
        city = form.cleaned_data.get('city', '')


        cities = City.objects.filter( name=city, state__name=state)


        context['cities'] = cities
    context['form'] = form

    return render(request,'city_search.html', context)



class StateListView(ListView):
    model = State 
    template_name = "state_list.html"
    context_object_name = "states"

class StateDetailView(DetailView):
    model = StateCapital
    template_name = "state_detail.html"
    context_object_name= "state"

def capital_detail(request, pk):

    context = {}

    capital = StateCapital.objects.get(pk=pk)

    context['capital'] = capital

    return render(request,'capital_detail.html', context)

def capital_list(request):
    context = {}
    context['capital'] = StateCapital.objects.all()
    
    return render(request,'capital_list.html', context)

def city_detail(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city

    return render(request,'city_detail.html', context)

def city_list(request):
    get_city= request.GET.get('city','')
    get_state= request.GET.get('state',210)

    context = {} 
    # city = City.objects.filter(name__startswith=get_city)
    context['states'] = State.objects.all()
    if get_state == '-1':
        state = State.objects.all()
        context['cities'] = City.objects.filter(name__startswith=get_city)

    else:
        state = State.objects.get(pk=get_state)
        context['cities'] = City.objects.filter(state__pk=state.pk, name__startswith=get_city)
    # context['city']= city
    # context['state'] = State.objects.filter(state__pk=get_state)
    
    return render(request,'city_list.html', context)

def state_detail(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    return render(request,'state_detail.html', context)


def state_list(request):
    context = {}

    states = State.objects.all()
    context['states'] = states
    return render(request,'state_list.html',context)

def list(request):

    get_state = request.GET.get('state','')

    context={}


    states = State.objects.filter(name__startswith=get_state)

    print states
    # for state in states:
        
    context['states']= states
    return render(request,'base.html', context )

def detail_view(request, pk):
    state = State.objects.get(pk=pk)
    cities = state.city_set.all()

    context={}

    context['cities']= cities

    context['state'] = state

    return render(request,'detail.html',context)

    




      # search_from = request.GET.get('from', 0)
    # search_to = request.GET.get('to', 1000)
    
    # context ={}
    # statecapital_list=[]
    # context['statecapital_list']=statecapital_list
    
    # statecapitals = StateCapital.objects.all()
    # for statecapital in statecapitals:
    #     if statecapital.population>search_from and statecapital.population <search_to:
    #         statecapital_list.append(statecapital)












