from django.shortcuts import render, redirect
from .models import Project, Skill, Message
from .forms import MessageForm

# Create your views here.
def homePage(request):
    projects = Project.objects.filter(is_active=True)
    skills = Skill.objects.filter(is_active=True)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"projects": projects, "skills": skills}
    return render(request, 'base/home.html', context)

def inboxPage(request):
    messages = Message.objects.all()
    unread = Message.objects.filter(is_read=False).count()

    context = {"messages": messages, "unread": unread}
    return render(request, 'base/inbox.html', context)

def inboxMessage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()

    context = {"message": message}
    return render(request, 'base/inbox-message.html', context)