from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PictureConfig,CarouselConfig,Picture
from django.utils.translation import ugettext_lazy as _

class PictureAppPlugin(CMSPluginBase):
    model = PictureConfig
    render_template = "picture_plugin.html"
    cache = False
    name = _("Gallery")

    def render(self, context, instance, placeholder):
    	context['picture_config'] = instance
    	return context


class CarouselPlugin(CMSPluginBase):
    model = CarouselConfig
    render_template = "carousel_plugin.html"
    cache = False
    name = _("Carousel")

    def render(self, context, instance, placeholder):
    	context['carousel_config'] = instance
    	context['pictures'] = instance.album.pictures.all()
    	return context    	

plugin_pool.register_plugin(PictureAppPlugin)
plugin_pool.register_plugin(CarouselPlugin)