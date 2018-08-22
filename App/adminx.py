from App.models import *
import xadmin
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "论坛后台"
    site_header = 'XX论坛'
    site_footer = "XGF"


class userAdmin(object):
    list_display = [
        'uname',
        'uicon',
        'gender',
        'signature',
        'mobile',
        'email',
        'bgimg',
        ]


class TextTypeAdmin(object):
    list_display = ['name']

class ArticleAdmin(object):
    list_display = [
        'title',
        'A_type',
        'author',
        'add_time',
    ]


class CommentAdmin(object):
    list_display = [
        'belong_art',
        'belong_user',
        'pinglun',
        'add_time',
    ]


class Massage(object):
    list_display = [
        'name',
        'email',
        'massage',
        'add_time',
    ]

xadmin.site.register(User, userAdmin)
xadmin.site.register(TextType, TextTypeAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)

