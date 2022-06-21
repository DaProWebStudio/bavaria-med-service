from django.utils import timezone
from django.conf import settings
from service.models import Service, ServiceCarousel


def getting_info(request):
    domen = 'http://bavariamed.ru'
    current_path = request.get_full_path()
    current_url = f'{domen}{current_path}'
    corrent_year = timezone.now().strftime('%Y')
    tel_number = {'format': settings.TEL_NUMBER[0], 'href': settings.TEL_NUMBER[1]}
    mobile_number = {'format': settings.MOBILE_NUMBER[0], 'href': settings.MOBILE_NUMBER[1]}
    email = settings.EMAIL_HOST_USER
    carousels = ServiceCarousel.objects.all().values('title', 'descriptions', 'url')
    return locals()