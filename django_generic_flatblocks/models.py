from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django_generic_flatblocks.fields import JSONField
from django.core import serializers

class GenericFlatblock(models.Model):
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    exclude_fields = JSONField(_('fields display in template'),blank=True,null=True)

    def __unicode__(self):
        return self.slug

class GenericFlatblockList(models.Model):
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    content_type = models.ForeignKey(ContentType)
    exclude_fields = JSONField(_('fields not display in template'),blank=True,null=True)
    query_args = JSONField(_('custom query args'),blank=True,null=True)

    def __unicode__(self):
        return self.slug

    def model(self):
        return self.content_type.model_class()

    @property
    def object_list(self):
        model = self.content_type.model_class()
        if self.query_args:
            return model.objects.filter(self.query_args)
        return model.objects.all()


    @property
    def serialize(self):
        fields = [u.name for u in self.model()._meta.fields if u.name not in self.exclude_fields]
        return serializers.serialize("python", (self.object_list),fields=fields)

