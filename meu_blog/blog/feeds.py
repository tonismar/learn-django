from django.contrib.syndication.feeds import Feed

from models import Artigo

class UltimosArtigos(Feed):
	title = 'Last articles from Alatazan\'s blog'
	link = '/'

	def items(self):
		return Artigo.objects.all()
