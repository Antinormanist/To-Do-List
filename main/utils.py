from .models import Note


def create_slug(user):
    task = Note.objects.filter(user=user)
    if not task:
        slug = f'{user}_task_1'
    else:
        # task = task[len(task) - 1]
        latest_num = int(task[len(task) - 1].slug.split('_')[-1])
        slug = f'{user}_task_{latest_num + 1}'
    return slug