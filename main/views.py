from django.shortcuts import render

from .forms import CreateTask
from .models import Note

# Create your views here.
def index(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            text = request.GET.get('text')
            name = request.GET.get('name')
            priority = request.GET.get('priorities')
            if text and name and priority:
                name = name[:12]
                if priority == 'common':
                    task_class = 'priority-e'
                elif priority == 'medium':
                    task_class = 'priority-m'
                else:
                    task_class = 'priority-h'
                    
                Note.objects.create(
                    text=text,
                    name=name,
                    priority=priority,
                    task_class=task_class,
                    user=request.user
                )
        
    
    
    context = {
        'title': 'Main page',
    }
    if not request.user.is_anonymous:
        context['tasks'] = Note.objects.filter(user=request.user)
    return render(request, 'main/index.html', context)