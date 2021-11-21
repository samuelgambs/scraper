from django.db import models

class PartiesInvolved(models.Model):
    """
    PartiesInvolved model
    """
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Process(models.Model):
    process_number = models.CharField(max_length=100)
    process_class = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    judge = models.CharField(max_length=100)

    parties_involved = models.ManyToManyField(PartiesInvolved, through='PartiesInvolvedProcess' ,blank=True, related_name='parties_involved')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PartiesInvolvedProcess(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    parties_involved = models.ForeignKey(PartiesInvolved, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Processes and Parties Involved"
