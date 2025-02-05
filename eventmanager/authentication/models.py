from django.db import models
from django.contrib.auth.models import AbstractUser
from colorfield.fields import ColorField


role_choices = (
      (0, 'admin'),
      (1, 'manager'),
      (2, 'customer'),
      (3, 'volleymanager'),
      (4, 'volleycoach'),
      (5, 'volleyplayer'),
      
    )


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=role_choices, default=2)    
    can_create_user = models.BooleanField(default=False)
    
    def __str__(self):
        if self.first_name and self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        return self.email

    class Meta:
        verbose_name = 'Utente'
        verbose_name_plural = 'Utenti'


class Customer(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.role = 2
    def __str__(self):
        if self.first_name and self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        return self.email

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clienti'


class Manager(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.role = 1

    def __str__(self):
        if self.first_name and self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        return self.email

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Manager'


class ThemeConfig(models.Model):
    name = models.CharField(default='default', max_length=64)
    user = models.ForeignKey('authentication.User', default=None, on_delete=models.SET_DEFAULT, blank=True, null=True)
    navbar = ColorField(default='#2D5B6B')
    header = ColorField(default='#52494C')
    sidebar = ColorField(default='#8F4731')
    background = ColorField(default='#FDF5F1')
    hover = ColorField(default='#ffffff')
    post_background = ColorField(default='#ffffff')
    post_footer = ColorField(default='#ffffff')
    card_header = ColorField(default='#7B7D2A')
    card_body = ColorField(default='#ffffff')
    profile_image = models.ImageField(upload_to='profile_images/', default='/logo.png')
    cover_image = models.ImageField(upload_to='cover_images/', default='/logo.png')
    
    

    def __str__(self):
        return f'{self.user} {self.name}'
    
    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temi'

"""
class GymConfig(models.Model):
    name = models.CharField(default='default', max_length=64)
    gym = models.ForeignKey('reservation.Gym', default=None, on_delete=models.SET_DEFAULT)
    width_field = models.IntegerField(default=400)
    height_field = models.IntegerField(default=200)
    width_space = models.IntegerField(default=1200)
    height_space = models.IntegerField(default=600)
    seat_radius = models.IntegerField(default=60)

    top_field = models.IntegerField(default=100)
    left_field = models.IntegerField(default=100)


    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Configurazione palestra'
        verbose_name_plural = 'Configurazioni palestre'
"""