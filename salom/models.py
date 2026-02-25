from django.db import models

class TestUchun(models.Model):
    name = models. CharField (max_length=255)

    def _str__(self) :
        return self.name