from django.shortcuts import render, redirect
from . models import GameNumber, Sign, Dozen, Column
from . forms import GameNumberForm, NumberForm
from django.http import HttpResponse, JsonResponse


from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GameNumberSerializer, SignSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'numbers':               'api/numbers/',
        'signs'   :               'api/signs',
    }
    return Response(api_urls)

    
@api_view(['GET'])
def numbers(request):
    number = GameNumber.objects.all()
    serializer = GameNumberSerializer(number, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def signs(request):
    signs = Sign.objects.all()
    serializer = SignSerializer(signs, many=True)
    return Response(serializer.data)

@login_required
def add_numbers(request):
    number = GameNumber.objects.all()
    signs = Sign.objects.all()
    dozen = Dozen.objects.all()
    column = Column.objects.all()
    alllist = zip(signs, dozen, column)
    context = {
        'number': number,
        'signs': signs,
        'dozen': dozen,
        'column': column,
        'alllist': alllist
    }
    return render(request, 'abcd/index.html', context)

def save_number(request):
    
    
    if request.method != 'POST':
        messages.error(request, 'Invalid Methode')
        return redirect('add_number')
    else:
        number = request.POST.get('number')
        try:
            number_model = GameNumber(number=number)
            number_model.save()
            add_sign_A(int(number))
            add_dozen1(int(number))
            add_col1(int(number))
            add_sign_B(int(number))
            add_dozen2(int(number))
            add_col2(int(number))
            add_sign_C(int(number))
            add_dozen3(int(number))
            add_col3(int(number))
            add_sign_D(int(number))
            
            messages.success(request, 'Added Successfully')
            return redirect('add_number') 
        except:
            messages.error(request, 'Failed to add number')
            return redirect('add_number')




A = [1,3,5,7,9,12,14,16,18]
B = [2,4,6,8,10,11,13,15,17]
C = [19,21,23,25,27,30,32,34,36]
D = [20,22,24,26,28,29,31,33,35]



def add_sign_A(number):
    for i in A:
        if (i == number):
            sign = Sign.objects.create(sign='A')
            sign.save()

def add_sign_B(number):
    for i in B:
        if (i == number):
            sign = Sign.objects.create(sign='B')
            sign.save()

def add_sign_C(number):
    for i in C:
        if (i == number):
            sign = Sign.objects.create(sign='C')
            sign.save()

def add_sign_D(number):
    for i in D:
        if (i == number):
            sign = Sign.objects.create(sign='D')
            sign.save()

def add_sign_0(number):
    if (number == 0):
        sign = Sign.objects.create(sign=0)
        sign.save()


def del_number(request):
    number = GameNumber.objects.all()
    sign = Sign.objects.all()
    dozen = Dozen.objects.all()
    column = Column.objects.all()
    try:
        number.delete()
        sign.delete()
        dozen.delete()
        column.delete()
        messages.success(request, 'Reset Successful')
        return redirect('/')
    except:
        messages.error(request, 'Failed to Reset')
        return redirect('/')


Dozen1 = [1,2,3,4,5,6,7,8,9,10,11,12]
Dozen2 = [13,14,15,16,17,18,19,20,21,22,23,24]
Dozen3 = [25,26,27,28,29,30,31,32,33,34,35,36]

def add_dozen1(number):
    for i in Dozen1:
        if (i == number):
            dozen = Dozen.objects.create(dozen='1')
            dozen.save()

def add_dozen2(number):
    for i in Dozen2:
        if (i == number):
            dozen = Dozen.objects.create(dozen='2')
            dozen.save()

def add_dozen3(number):
    for i in Dozen3:
        if (i == number):
            dozen = Dozen.objects.create(dozen='3')
            dozen.save()


Col3 = [3,6,9,12,15,18,21,24,27,30,33,36]
Col2 = [2,5,8,11,14,17,20,23,26,29,32,35]
Col1 = [1,4,7,10,13,16,19,22,25,28,31,34]


def add_col1(number):
    for i in Col1:
        if (i == number):
            column = Column.objects.create(column='1')
            column.save()

def add_col2(number):
    for i in Col2:
        if (i == number):
            column = Column.objects.create(column='2')
            column.save()

def add_col3(number):
    for i in Col3:
        if (i == number):
            column = Column.objects.create(column='3')
            column.save()

def rol(request):
    return render(request, 'abcd/rol.html')

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    else:
        f = CustomUserCreationForm()

    return render(request, 'abcd/register.html', {'form': f})




