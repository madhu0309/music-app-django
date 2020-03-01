from django import template

from music.models import Favorite

register = template.Library()


@register.simple_tag(name='is_favorited')
def is_favorited(song, user):
    favorited = Favorite.objects.filter(user=user, song=song)
    if favorited:
        return 'remove'
    else:
        return 'make'