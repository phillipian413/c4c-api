import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class AbstractModel(models.Model):

    uuid = models.UUIDField(
        _("UUID"),
        default=uuid.uuid4(),
        unique=True,
        editable=False,
        db_index=True
    )
    created_at = models.DateTimeField(_("Created At") ,auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(_("Updated At") ,auto_now=False, auto_now_add=False)

    class Meta:
        abstract = True
        ordering = ["-created_at"]