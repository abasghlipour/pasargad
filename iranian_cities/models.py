from django.db import models
from django.utils.translation import gettext_lazy as _


class Ostan(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    amar_code = models.IntegerField(_('Amar Code'))

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = _('Ostan')
        verbose_name_plural = _('Ostans')
        ordering = ('id',)


class Shahrestan(models.Model):
    ostan = models.ForeignKey(
        Ostan,
        verbose_name=_('Ostan'),
        related_name='shahrestans',
        on_delete=models.CASCADE
    )
    name = models.CharField(_('Name'), max_length=255)
    amar_code = models.IntegerField(_('Amar Code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Shahrestan')
        verbose_name_plural = _('Shahrestans')
        ordering = ('id',)


class Shahr(models.Model):
    ostan = models.ForeignKey(
        Ostan,
        verbose_name=_('Ostan'),
        related_name='shahrs',
        on_delete=models.CASCADE
    )
    shahrestan = models.ForeignKey(
        Shahrestan,
        verbose_name=_('Shahrestan'),
        related_name='shahrs',
        on_delete=models.CASCADE
    )
    
    name = models.CharField(_('Name'), max_length=255)
    amar_code = models.BigIntegerField(_('Amar Code'))
    shahr_type = models.BigIntegerField(_('Shahr Type'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Shahr')
        verbose_name_plural = _('Shahrs')
        ordering = ('id',)


