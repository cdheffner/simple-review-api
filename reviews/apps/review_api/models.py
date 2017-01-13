from __future__ import unicode_literals
from django.db import models
import bcrypt
import uuid

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])')

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

class ReviewerManager(models.Manager):
	def create(self, rInfo):
		# check if email is in database already
		r = Reviewer.objects.filter(email=rInfo['email'])
		if r[0]:
			return {errors: ["Email already exists"]}
		else: 
			# validate new reviewer metadata
			errors = []
			if len(rInfo['first_name']) < 2:
				errors.append("First name must be more than 1 character long")
			if len(rInfo['last_name']) < 2:
				errors.append("Last name must be more than 1 character long")
			if not EMAIL_REGEX.match(rInfo['email']):
				errors.append("Email address is not valid")
			if not rInfo['password'] === rInfo['password_confirm']:
				errors.append("Password confirmation must match password")
			if not PW_REGEX.match(rInfo['password'])
				errors.append("Password must contain at least one number, one uppercase letter, and one lowercase letter")
			if len(rInfo['password']) < 8:
				errors.append("Password must be at least 8 characters long")
			# check errors
			if len(errors) > 0:
				return {errors: errors}
			else:
				# create new reviewer
				pwhash = bcrypt.hashpw(rInfo['password'], bcrypt.gensalt())
				newtoken = uuid.uuid4()
				newR = Reviewer(first_name=rInfo['first_name'], last_name=rInfo['last_name'], email=rInfo['email'], password=pwhash, token=newtoken)
				newR.save()
				return {token: newtoken}
	def retrieveToken(self, info):
		r = Reviewer.objects.filter(email=info['email'])
		if len(r) == 0:
			return {errors: ["Invalid password or email"]}
		else:
			r = r[0]
			pwhash = r['password']
			if bcrypt.hashpw(info['password'], pwhash) == pwhash:
				return {token: r['token']}
			else:
				return {errors: ["Invalid password or email"]}


class Reviewer(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=200)
	token = models.CharField(max_length=200)
	created_at = models.DateTimeField
	objects = ReviewerManager()

class Review(models.Model):
	ratings = models.PositiveSmallIntegerField()
	title = models.CharField(max_length=64)
	summary = models.TextField()
	ip_address = models.URLField()
	submitted_at = models.DateTimeField(auto_now_add = True)
	company = models.ForeignKey(Company)
	reviewer = models.ForeignKey(Reviewer)

