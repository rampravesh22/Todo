from django.shortcuts import redirect, render
from home.models import *
# Create your views here.


def home_page(request):
    if request.method == "POST":
        # 'name_todo' is come from input name attribute it store the value "name_todo"
        todo = request.POST.get('name_todo')
        td = Todo(todo_name=todo)
        td.save()
        return redirect("/")

    td = Todo.objects.all()
    context = {"todo": td}

    return render(request, "home/home_page.html", context)


def delete_todo(request, id):
    try:
        todo_obj = Todo.objects.get(id=id)
        todo_obj.delete()
    except Exception as e:
        print(e)

    return redirect("/")


def update_todo(request):
    id = request.GET.get('id')
    try:
        todo_obj = Todo.objects.get(id=id)
        todo_obj.is_completed = not todo_obj.is_completed
        todo_obj.save()
    except Exception as e:
        print(e)

    return redirect("/")
