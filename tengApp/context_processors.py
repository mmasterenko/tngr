from .models import GeneralInfo


def general_info(req):
    info = GeneralInfo.objects.first()
    try:
        info = {
            'address': info.address,
            'phone': info.phone,
            'email': info.email,
            'text': info.footerText
        }
    except AttributeError:
        info = {}
    return {'general_info': info}
