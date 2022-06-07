from typing import Any


def getting_info(request: Any) -> dict[str, Any]:
    domen = 'https://btk.kg'
    curren_path = request.get_full_path()
    curren_url = f'{domen}{curren_path}'
    tel_number = {'format': '+996 (707) 36-67-49', 'href': '+996707366749'}
    mobile_number = {'format': '+996 (707) 36-67-49', 'href': '+996707366749'}
    email = 'bavariamed@gmail.com'
    return locals()