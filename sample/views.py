from django.shortcuts import render
# Create your views here.
from .models import Movies_list, Movies_pics, Director
from .forms import Movies_form, Movie_pic_form

movies_list = {
        "movies" : [
            
        ]
    }

def show_movies (request) :

    items = Movies_list.objects.order_by('-year').values()
    
    visit = int(request.COOKIES.get('visits', 0))

    visit += 1

    for mov in items :
        single_pic = Movies_pics.objects.get(id = mov['movie_picture_id'])
        single_dir = Director.objects.get(id = mov['directed_by_id'])
        mov['movie_pic'] = single_pic.photo
        mov['director'] = single_dir.director_name
    

    response = render(request, 'index.html', {'movies_list' : items, 'visit' : visit})

    response.set_cookie('visits', visit)

    return response

def movie_pic_page (request) :
    movie_pics = Movies_pics.objects.all()
    print(movie_pics)
    return render(request, 'movie_pic.html', { 'movie_pics' : movie_pics })

def create_page (request) :

    if request.POST :
        item = {
            'title' : request.POST.get('title'),
            'year' : request.POST.get('year')
        }

        movies_db = Movies_list(title = item['title'], year = item['year'])

        movies_db.save()
    return render(request, 'create.html')

def custome_create (request) :
    if request.POST :
        frm = Movies_form(request.POST)
        if frm.is_valid() :
            frm.save()
    frm = Movies_form()

    return render(request, 'custome_create.html', {'frm' : frm})

def delete_movie (request, pk) :
    inst = Movies_list.objects.get(pk = pk)
    inst.delete()

    items = Movies_list.objects.all().values()
    movies_list['movies'] = items
    return render(request, 'index.html', movies_list)

def edit_movie (request, pk) :
    inst = Movies_list.objects.get(pk = pk)

    if request.POST :
        title = request.POST.get('title')
        year = request.POST.get('year')

        inst.title = title
        inst.year = year

        inst.save()

    inst = Movies_list.objects.get(pk = pk) 
    frm = Movies_form(instance=inst)

    return render(request, 'edit_page.html', { 'frm' : frm })

def upload_movie_pic (request) :
    if request.method == "POST" :
        frm = Movie_pic_form(request.POST, request.FILES)
        if frm.is_valid() :
            frm.save()
    frm = Movie_pic_form()
    return render(request, 'upload_photo.html', {'frm' : frm})