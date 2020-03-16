from django.shortcuts import render, redirect
from .models import Predmet, Comment

def main(request):
    predmets = Predmet.objects.all()
    return render(request, 'main.html', {'predmets' : predmets})

def by_id(request, id):
    predmet = Predmet.objects.get(id=id)
    comments = Comment.objects.filter(predmet=predmet)
    if request.method == 'GET':
        return render(request, 'by_id.html', {'predmet' : predmet, 'comments' : comments})
    elif request.method == 'POST':
        author = request.POST['author']
        text = request.POST['text']
        comment = Comment(predmet=predmet, author=author, text=text)
        comment.save()
        return redirect('/')