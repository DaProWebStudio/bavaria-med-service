from django.utils.text import slugify
import transliterate


def translit_slug(name):
	world = ''
	for i in name.lower():
		if i == 'ң':
			world += 'н'
		elif i == 'ү':
			world += 'у'
		elif i == 'ө':
			world += 'о'
		else:
			world += i
			
	try:
		slug = transliterate.translit(world, reversed=True)
	except:
		slug = world
	new_slug = slugify(slug, allow_unicode=True)
	return new_slug