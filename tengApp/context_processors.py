from .models import GeneralInfo, Settings


def general_info(req):
    info = GeneralInfo.objects.first()
    try:
        info = {
            'address': info.address,
            'phone': info.phone,
            'email': info.email,
            'text': info.footerText,
            'logo': info.logo
        }
    except AttributeError:
        info = {}
    return {'general_info': info, 'settings': Settings.objects.first()}
