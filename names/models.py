from django.db import models


class NameManager(models.Manager):
    def get_unused(self):
        """
        Returns all unused entities.
        """
        return self.filter(used=False)

    def get_used(self):
        """
        Returns all used entities.
        """
        return self.filter(used=True)

    def get_unused_random(self):
        """
        Returns one random unused name.
        """
        try:
            return self.get_unused().order_by('?').first()
        except:
            return None


class Name(models.Model):

    name = models.CharField(max_length=100, help_text="The name.")
    used = models.BooleanField(default=False, help_text="Check after the name is used.")

    objects = NameManager()

    def save(self):
        # capitalize using the .title() method ONLY if the user did not enter ANY capital letters
        if not self.pk:
            value = getattr(self, 'name')
            if (not any(x.isupper() for x in value)):
                setattr(self, 'name', value.title())
        super(Name, self).save()

    def __unicode__(self):
        return self.name
