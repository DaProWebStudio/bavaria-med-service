from django.utils import timezone
from service.models import ServiceCarousel


def getting_info(request):
    domen = 'http://bavariamed.ru'
    current_path = request.get_full_path()
    current_url = f'{domen}{current_path}'
    corrent_year = timezone.now().strftime('%Y')
    tel_number = {'format': '+996 (707) 36-67-44', 'href': '+996707366744'}
    mobile_number = {'format': '+996 (707) 36-67-45', 'href': '+996707366745'}
    email = 'bavariamed@gmail.com'
    carousels = ServiceCarousel.objects.all().values('title', 'descriptions', 'url')
    return locals()