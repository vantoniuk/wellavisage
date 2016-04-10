from django.db import models
from django.contrib.auth.models import User
from cms.models.pluginmodel import CMSPlugin

class Picture(models.Model):
	pic_file = models.ImageField('choose a picture', upload_to='picture/%Y/%m/%d')
	date = models.DateTimeField('upload date', auto_now_add=True)
	author = models.ForeignKey(User)
	desc = models.TextField('picture description', blank=True)

	def file_name(self):
		return self.pic_file.name	

	def __unicode__(self):
		return self.file_name()

class Album(models.Model):
	name = models.CharField('album name', max_length = 100)
	description = models.TextField('album description', blank=True)
	author = models.ForeignKey(User)
	date = models.DateTimeField('created', auto_now_add=True)
	pictures = models.ManyToManyField(Picture, related_name='picture')	
	thumbnail = models.ForeignKey(Picture, related_name='thumbnail')

	def __unicode__(self):
		return self.name

class PictureConfig(CMSPlugin):
	page_size = models.PositiveSmallIntegerField(help_text = 'number of pictures displayed per each page', verbose_name = 'page size')	
	album = models.ForeignKey(Album, related_name='album')	


class CarouselConfig(CMSPlugin):
	name = models.CharField('carousel name', max_length = 100)
	height = models.PositiveSmallIntegerField(help_text = 'images height')	
	width = models.PositiveSmallIntegerField(help_text = 'images width')	
	interval = models.PositiveSmallIntegerField(help_text = 'change interval in seconds')	
	pictures_only = models.BooleanField(help_text = 'display only pictures without description', verbose_name = 'pictures only', default=True)
	album = models.ForeignKey(Album, related_name='carousel_album', help_text='The album with pictures that will be used in carousel')	
	aligment = models.CharField(
		'aligment', 
		max_length = 2, 
		choices=(('C', 'Center'), ('L', 'Left'), ('R', 'Right')),
		help_text='Aligment of the main picture in carousel'	
	)
	change_effect = models.CharField(
		'change effect', 
		max_length=4, 
		choices=(
			('S', 'Slide'), 
			('SE', 'Slide Exclusive (show only one picture at a time)'), 
			('FI', 'Fade In'), 
			('FO', 'Fade Out')
		),
		help_text='The type of effect that will be used in carousel to rotate the picture'
	)
	navigation = models.CharField(
		'navigation type', 
		max_length=4, 
		help_text='The type of navigation used in carousel to change the picture manually',
		choices=(
			('NA', 'None'), 
			('BF', 'Back and forward'), 
			('SC', 'Anchor type of navigation'), 
			('SCT', 'Anchor type of navigation with text description')
		)
	)
	pictures_only = models.BooleanField(help_text = 'display only pictures without description', verbose_name = 'pictures only', default=True)

