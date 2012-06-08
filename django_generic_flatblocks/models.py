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
    display_fields = JSONField(_('fields display in template'))

    def __unicode__(self):
        return self.slug

class GenericFlatblockList(models.Model):
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    content_type = models.ForeignKey(ContentType)
    display_fields = JSONField(_('fields display in template'))
    query_args = JSONField(_('custom query args'))

    def __unicode__(self):
        return self.slug

    def model(self):
        return self.content_type.model_classe()

    @property
    def object_list(self):
        model = self.content_type.model_classe()
        return model.objects.filter(self.query_args.to_python())

    @property
    def serialize(self):
        return serializers.serialize("python", (self.object_list,),fields=self.display_fields.to_python())

