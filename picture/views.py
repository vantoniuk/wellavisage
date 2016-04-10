from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.template import RequestContext, loader
from .models import Picture,Album
from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import get_object_or_404

def template(request):
    return render_to_response('picture/template.html')

def insert(request):
	if request.method == 'POST':
		form = PictureForm(request.POST, request.FILES)
		if form.is_valid():
			new_image = Picture(pic_file = request.FILES['pic_file'])    
			new_image.save()
			return JsonResponse({'result': True})
		else:
			return JsonResponse({'result': False})	
	else:
		return	JsonResponse({'result': False})	    

def list(request, album_id = 1, page_num = 1, per_page=25):
	if request.method == 'GET':
		album = get_object_or_404(Album, id=album_id)
		pictures = album.pictures.all()
		paginator = Paginator(pictures, per_page)
		pictures_for_page = paginator.page(page_num)

#render_to_response('picture/list.html', RequestContext(request, {'pictures': pictures_for_page,}))
		return JsonResponse({'result': True, 'data': map(pictureToDictionary, pictures_for_page)})
	else:
		return JsonResponse({'result': False})

def pictureToDictionary(picture):
	return {
		'id': picture.id,
		'url': settings.MEDIA_URL + picture.file_name(),
		'author': picture.author.id,
		'description': picture.desc,
		'date': picture.date,
	}
