from django.db import models
from django.utils.translation import gettext_lazy as _
from app_category.models import Specialization


# file will be uploaded to MEDIA_ROOT/uploads
class Get_referral(models.Model):
    name = models.CharField(_('Имя'), max_length=55, blank=False)
    email = models.EmailField(_('email'), blank=False)
    choice_of_specialty = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    file1 = models.FileField(upload_to='uploads/', blank=True)
    file2 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    file3 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    file4 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    file5 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = _('запрос')
        verbose_name_plural = _('запросы')

