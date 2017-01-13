from __future__ import unicode_literals

from django.db import models

class CompanyManager(models.Manager):
	def findOrCreate(self, cname):
		comp = Company.objects.filter(name=cname)
		if comp[0]:
			return comp[0]
		else:
			comp = Company(name=cname)
			comp.save()
			comp = Company.objects.filter(name=cname)
			return comp[0]

class Company(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	objects = CompanyManager()

class Reviewer(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=200)
	created_at = models.DateTimeField

class Review(models.Model):
	ratings = models.PositiveSmallIntegerField()
	title = models.CharField(max_length=64)
	summary = models.TextField()
	ip_address = models.URLField()
	submitted_at = models.DateTimeField(auto_now_add = True)
	company = models.ForeignKey(Company)
	reviewer = models.ForeignKey(Reviewer)

