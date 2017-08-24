from .models import Album, Song
from django.shortcuts import render, get_object_or_404
import hashlib
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def jab(request):
    return HttpResponse("<h1>This is Jab!</h1>")

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}
    print(context)
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album,'mine' : ['me secretly passed!',123]})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        tmp=request.POST['song']
        print(tmp)
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message':'You didnt selected',
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

def add_new_album(request):

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='music/static/images/')

        artist = request.POST.get('artist').strip()
        album_title = request.POST.get('album_title').strip()
        genre = request.POST.get('genre').strip()
        album_logo = hashlib.md5(artist.encode('utf-8')+'+'.encode('utf-8')+album_title.encode('utf-8')).hexdigest()
        filename = fs.save(album_logo+'.jpg', myfile)
        test = request.POST.get('test').strip()
        insert_data = Album(artist=artist, album_title=album_title, genre=genre, album_logo=album_logo, test=test)
        insert_data.save()
        return render(request, 'music/add_new_album.html')
    else:
        return render(request, 'music/add_new_album.html')


def add_new_song(request):
    all_albums = Album.objects.all()
    all_albums = {'all_albums' : all_albums}
    print(all_albums)

    if request.method == 'POST':

        file_type = request.POST.get('file_type').strip()
        song_title = request.POST.get('song_title').strip()
        mine_albums = get_object_or_404(Album, pk=request.POST.get('album'))
        is_favorite = request.POST.get('is_favorite')
        if is_favorite is None:
            is_favorite = False
        print(is_favorite)
        print("###")
        insert_data = Song(file_type=file_type, song_title=song_title, album=mine_albums, is_favorite=is_favorite)
        insert_data.save()
        return render(request, 'music/add_new_song.html', all_albums)
    if request.method == 'GET':
        return render(request, 'music/add_new_song.html', all_albums)

