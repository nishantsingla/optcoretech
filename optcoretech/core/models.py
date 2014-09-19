from datetime import time
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Price(models.Model):
	current_time = models.TimeField(_('Current Time'), default=time(23,0,0))
