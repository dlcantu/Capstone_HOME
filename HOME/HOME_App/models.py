from django.db import models

class Client(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    clientNotes = models.TextField(max_length=500)

    def __str__(self):
        return self.lastName

class Goals(models.Model):
    selectClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    dateCreated = models.DateField(null=True)
    goalEndDate = models.DateField(null=True)
    goalNotes = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.selectClient}, {self.dateCreated}"