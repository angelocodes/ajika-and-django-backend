from django.db import models

# Create your models here.
# model => python class
# a model represents a database table
# attrs of the model/python class are the fields of the table

class JobPosting(models.Model):
    #by default django creates an id field as primary key
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()


# makemigrations => create instructions telling django how the db has changed
# migrate => apply the migration file to the database ie apply the above changes


# model manager => objects => interface to interact with the db using python code
# JobPosting.objects.all() => get all job postings
# JobPosting.objects.create(title="Software Engineer", description="...", company="ABC Corp", salary=60000)
# JobPosting.objects.filter(company="ABC Corp") => get all job postings for company ABC Corp