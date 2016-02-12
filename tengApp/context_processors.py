from .models import GeneralInfo, Settings, FlatPages


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
        fp = FlatPages.objects.order_by('-order', 'id').values('submenu', 'url')
        menu = {
            'home': fp.filter(menu='main'),
            'project': fp.filter(menu='project'),
            'about': fp.filter(menu='about'),
            'group': fp.filter(menu='t-group'),
        }
    except AttributeError:
        info = {}
        menu = {}
    return {'general_info': info, 'mainMenu': menu}
