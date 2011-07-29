from django.utils import simplejson
from slideshow.models import SlideshowPhoto
from django.http import HttpResponse
from django.shortcuts import render_to_response
from photologue.models import PhotoSize

def ajax_slideshow(request):
  ss_id = request.GET['id']
  mimetype = 'application/javascript'
  photos = SlideshowPhoto.objects.filter(slideshow=ss_id)
  photo_size = PhotoSize.objects.get(name='slideshow')
  return render_to_response('slideshow/slides.html', dict(photos=photos, width=photo_size.width, height=photo_size.height), mimetype=mimetype)
#  return HttpResponse(simplejson.dumps(list(photos)), mimetype)
