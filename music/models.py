from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# class Album(models.Model):
#     #user = models.ForeignKey(User, default=1,on_delete = models.CASCADE)

#     artist = models.CharField(max_length=250)
#     album_title = models.CharField(max_length=500)
#     genre = models.CharField(max_length=100)
#     album_logo = models.FileField()
#     is_favorite = models.BooleanField(default=False)

#     def __str__(self):
#         return self.album_title + ' - ' + self.artist


class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    song_image = models.ImageField(upload_to='media/images/')
    audio_file = models.FileField(upload_to='media/songs/')
    favourite = models.ManyToManyField(
        User, related_name='favourite', blank=True)

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('song_detail', args=[self.id])
#   artist = models.CharField(max_length=250)
#     album_title = models.CharField(max_length=500)
#     genre = models.CharField(max_length=100)
#     album_logo = models.FileField()
#     is_favorite = models.BooleanField(default=False)

#     def __str__(self):
#         return self.album_title + ' - ' + self.artist


# class Song(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     song_title = models.CharField(max_length=250)
#     song_image = models.ImageField(upload_to = 'media/images/')
#     audio_file = models.FileField(upload_to = 'media/songs/')
#     favourite = models.ManyToManyField(User, related_name = 'favourite', blank=True) 

#     def __str__(self):
#         return self.song_title

#     def get_absolute_url(self):
#         return reverse('song_detail', args=[self.id])


