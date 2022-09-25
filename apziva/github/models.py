from pyexpat import model
from django.db import models
from django.utils.translation import gettext as _

class Person(models.Model):
    name = models.CharField(_("name"), max_length=50, null=False, db_index=True)
    skills = models.CharField(_("skills"), max_length=100, null=False, db_index=True)

    def __str__(self):
        return self.name