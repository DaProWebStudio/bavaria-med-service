from django.utils import timezone


def getting_info(request):
    domen = 'https://btk.kg'
    current_path = request.get_full_path()
    current_url = f'{domen}{current_path}'
    corrent_year = timezone.now().strftime('%Y')
    tel_number = {'format': '+996 (707) 36-67-41', 'href': '+996707366741'}
    mobile_number = {'format': '+996 (707) 36-67-41', 'href': '+996707366741'}
    email = 'bavariamed@gmail.com'
    return locals()