from django.shortcuts import render

from .forms import CreateTask
from .models import Note
from .utils import create_slug

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
                    
                slug = create_slug(request.user)
                    
                Note.objects.create(
                    text=text,
                    name=name,
                    priority=priority,
                    task_class=task_class,
                    slug=slug,
                    user=request.user,
                )
        
    if request.method == 'GET' and request.GET.get('delete-task') == '1':
        tasks = Note.objects.filter(slug=request.GET['task-slug'])
        if tasks:
            Note.objects.get(slug=request.GET['task-slug']).delete()
    
    context = {
        'title': 'Main page',
    }
    if not request.user.is_anonymous:
        context['tasks'] = Note.objects.filter(user=request.user)
    return render(request, 'main/index.html', context)