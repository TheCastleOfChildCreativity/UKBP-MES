from django.db import models


class Stages(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Details(models.Model):
    name = models.CharField(max_length=255)
    type = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    stages = models.ManyToManyField(Stages)


class Work_pieces(models.Model):
    detail = models.ForeignKey(Details, on_delete=models.PROTECT)
    current_stage = models.ForeignKey(Stages, on_delete=models.PROTECT)
    status = models.CharField(max_length=255)


class History_operation(models.Model):
    work_piece = models.ForeignKey(Work_pieces, on_delete=models.PROTECT)
    stage = models.ForeignKey(Stages, on_delete=models.PROTECT)
