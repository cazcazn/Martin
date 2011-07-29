from cms.plugin_base import CMSPluginBase
from django.contrib import admin
from cms.plugin_pool import plugin_pool
from models import SlideshowGallery, SlideshowPhoto
from django.utils.translation import ugettext as _

class SlideshowPhotoInline(admin.TabularInline):
  model = SlideshowPhoto
  exclude = ("crop_from", "effect",)

class SlideshowPlugin(CMSPluginBase):
  model = SlideshowGallery
  name = _("Slideshow")
  render_template = "slideshow/slideshow.html"
  inlines = (SlideshowPhotoInline,)

  def render(self, context, instance, placeholder):
    context['instance'] = instance
    return context

plugin_pool.register_plugin(SlideshowPlugin)
