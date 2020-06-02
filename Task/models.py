from django.db import models


class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    des = models.TextField()

    def __str__(self):
        return self.title
