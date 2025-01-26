from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
    # work with database
    # transform data
    # data pass
    # http response/ Json Response

def home(request):
    return HttpResponse("Welcome to the Task Managment system");

def contact(request):
    return HttpResponse("<h1 style='color:red'>Contact Us <br> This is contact page to contact us.</h1>");

def show_task(request):
    return HttpResponse("This is our Show Task Page");

def show_specific_task(request,id):
    print ("id",id);
    print ("id type",type(id));
    return HttpResponse(f"This is our Show Specific Task Page and the id is: {id}");
    

# def about(request):
#     return HttpResponse(request);

# def contact(request):
#     return HttpResponse(request);

# def dashboard(request):
#     return HttpResponse(request);   

# def task(request):
#     return HttpResponse(request);

# def create_task(request):
#     return HttpResponse(request);

# def update_task(request, id):
#     return HttpResponse(request);

# def delete_task(request, id):
#     return HttpResponse(request);

# def task_details(request, id):
#     return HttpResponse(request);

# def task_history(request, id):
#     return HttpResponse(request);

# def task_comments(request, id):
#     return HttpResponse(request);

# def task_files(request, id):
#     return HttpResponse(request);


