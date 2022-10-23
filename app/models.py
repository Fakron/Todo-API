from django.db import models

# Create your models here.
status_choice = (
        ("PENDING","Pending"),
        ("COMPLETED","Completed"),
        ("DELETED","Deleted"),
    )

color_choice = (
    ("BLACK","Black"),
    ("BLUE","Blue"),
    ("RED","Red"),
    ("YELLOW","Yellow"),
    ("GREEN","Green"),
)

class Todoapp(models.Model):
    title  = models.CharField(max_length = 125)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length = 25,choices = status_choice,default ="PENDING")
    deadline = models.DateTimeField(null=True,blank=True)
    color = models.CharField(max_length = 15,choices = color_choice,default = "BLACK")
    is_important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,blank=True)

    

        

