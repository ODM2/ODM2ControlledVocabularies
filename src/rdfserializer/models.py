from django.db import models

# Create your models here.


class Namespace(models.Model):
    alias = models.CharField(primary_key=True, max_length=128)
    reference = models.URLField(max_length=255)

    def __unicode__(self):
        return self.alias

    class Meta:
        db_table = 'namespaces'


class Node(models.Model):
    node_id = models.AutoField(primary_key=True, db_column='nodeId')
    namespace = models.ForeignKey(Namespace, to_field='alias')
    name = models.CharField(max_length=255)

    @property
    def complete_name(self):
        return self.namespace.alias + ':' + self.name

    def __unicode__(self):
        return self.complete_name

    class Meta:
        db_table = 'nodes'


class FieldRelation(models.Model):
    field_id = models.AutoField(primary_key=True, db_column='fieldId')
    node = models.ForeignKey(Node, to_field='node_id', db_column='nodeId')
    field_name = models.CharField(max_length=255, db_column='fieldName')

    def __unicode__(self):
        return self.node.complete_name + "->" + self.field_name

    class Meta:
        db_table = 'fieldsrelations'


class Scheme(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    description = models.TextField()
    uri = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'schemes'

