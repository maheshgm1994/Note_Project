import datetime
from django.contrib.auth.decorators import login_required


from django.core.exceptions import ObjectDoesNotExist

from django.http import JsonResponse
from django.shortcuts import render, redirect,HttpResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.checks import messages
from .serializers import NoteSerializer
from django.contrib import messages
from rest_framework import status
from .forms import NoteForm

from .models import Notes


@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def notes(request):
    if request.method == "GET":
        # notes = Notes.objects.all().order_by('-added_on')
        notes = Notes.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    else:  # Post
        serializer = NoteSerializer(data=request.data)  # Convert JSON to Todo
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def note_details(request, id):
    try:
        note_detail = Notes.objects.get(user=request.user, id=id)
        # note_detail = Notes.objects.filter(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NoteSerializer(note_detail)
        return Response(serializer.data)
    elif request.method == 'PUT':  # when method is PUT then Update
        serializer = NoteSerializer(note_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in dataBase
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Bad request
    else:  # Delete
        note_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required
def addNote(request):
    if request.method == 'POST':
        note_name = request.POST.get('note_name')
        note_text = request.POST.get('note_text')
        # update_date = datetime.datetime.now()
        # note_img = request.FILES.get('note_img')
        # print("user:",request.user)
        try:
            Notes.objects.create(user=request.user, name=note_name, text=note_text)  # ,note_pic=note_img
        except Exception as ex:
            print(ex)
            return redirect("display")
        return redirect("display")
    return redirect("display")
    # elif request.method == "PUT":
    #     return redirect("display")


@login_required
def display(request):
    if request.method == "GET":
        displayNotes = Notes.objects.filter(user=request.user)
        return render(request, 'noteOperation/display.html', {'displayNotes': displayNotes})
    else:
        return redirect('display')
    return redirect('display')

@login_required
def searchText(request):
    if request.method == "POST":
        text = request.POST.get('text')
        if text !=None:
            searchResult = Notes.objects.filter(
                user=request.user,name__icontains=text) | Notes.objects.filter(
                user=request.user,text__icontains=text)
            return render(request, 'noteOperation/display.html', {'displayNotes': searchResult})
    return redirect('display')


@login_required
def editNote(request, id):
    if request.method == "GET":
        try:
            qs = Notes.objects.get(id=id)
            data = {'note_name': qs.name, 'note_text': qs.text, 'id':id}  # 'note_img': str(qs.note_pic)
            return JsonResponse(data)
        except Exception as ex:
            print("Error : ", ex)
            return redirect('display')
    return redirect('display')


def updateNote(request, id):
    print("updateNote working...")
    if request.method == "POST":
        note_id = id
        note_name = request.POST.get('note_name')
        note_text = request.POST.get('note_text')
        # note_pic = request.FILES.get('note_img')
        print(note_id, note_text, note_name)
        try:
            qs = Notes.objects.get(user=request.user,id=note_id)
            qs.name = note_name
            qs.text = note_text
            qs.updated_on=datetime.datetime.now()
            qs.save()
            return redirect('display')
        except Exception as ex:
            print("Error : ", ex)
            return redirect('display')
    return redirect('display')

@login_required
def deleteNote(request, id):
    try:
        exp = Notes.objects.get(id=id)
        exp.delete()
        return redirect("display")
    except Exception  as ex:
        return render(request, 'delete_expenditure.html', {'message': ex})

def home(request):
    return render(request, "noteOperation/home.html")

def service(request):
    return render(request, "noteOperation/service.html")


def contact(request):
    return render(request, "noteOperation/contact.html")


def about(request):
    return render(request, "noteOperation/about.html")

@login_required
def profile(request):
    js = {'name':'mahesh','age':25}
    return JsonResponse(js)

