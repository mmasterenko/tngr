from .models import GeneralInfo, FlatPages


def general_info(req):
    try:
        fp = FlatPages.objects.order_by('-order', 'id').values('submenu', 'url')
        menu = {
            'home': fp.filter(menu='main'),
            'project': fp.filter(menu='project'),
            'about': fp.filter(menu='about'),
            'group': fp.filter(menu='t-group'),
        }
    except Exception:
        menu = {}
    return {'general_info': GeneralInfo.objects.first(), 'mainMenu': menu}
