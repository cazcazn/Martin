from photologue.models import ImageModel
from django.contrib import admin
from django.db import models
from cms.models import CMSPlugin

class SlideshowGallery(CMSPlugin):
  title = models.CharField(max_length=100)
  
  def get_photos(self):
    return SlideshowPhoto.objects.filter(slideshow=self.pk)

class SlideshowPhoto(ImageModel):
  caption = models.CharField(max_length=100, blank=True)
  link = models.CharField(max_length=100, help_text="Either internal or external", blank=True)
  slideshow = models.ForeignKey(SlideshowGallery)

# admin.site.register(SlideshowImage, SlideshowImageAdmin)
