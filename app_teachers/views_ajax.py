from django.shortcuts import render, redirect
from .models import Lesson
from django.http import JsonResponse

def accept_lesson(request):
    lesson_id = request.GET.get('lesson_id', None)
    print('------------------------------')
    print("VERIFIED lesson (ID->",lesson_id,")")
    print('------------------------------')
    actual_lesson = Lesson.objects.get(pk=lesson_id)
    actual_lesson.is_verified = True
    actual_lesson.save()
    data = {'message' : "Elfogadva!"}
    return JsonResponse(data)

def reject_lesson(request):
    lesson_id = request.GET.get('lesson_id', None)
    print('------------------------------')
    print("REJECTED lesson (ID->",lesson_id,")")
    print('------------------------------')
    actual_lesson = Lesson.objects.get(pk=lesson_id)
    actual_lesson.is_rejected = True
    actual_lesson.save()
    data = {'message' : "Tanóra elutasítva!"}
    return JsonResponse(data)