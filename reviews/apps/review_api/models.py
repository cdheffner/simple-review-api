from __future__ import unicode_literals
from django.db import models
import bcrypt
import uuid
import re
import pprint

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])')
RATING_REGEX = re.compile(r'^[1-5]$')

class CompanyManager(models.Manager):
	def findOrCreate(self, cname):
		comp = Company.objects.filter(name=cname)
		if len(comp) > 0:
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
		# validate new reviewer metadata
		errors = []
		
		if not 'first_name' in rInfo:
			errors.append("First name is required")
		elif len(rInfo['first_name']) < 2:
			errors.append("First name must be more than 1 character long")
		
		if not 'last_name' in rInfo:
			errors.append("Last name is required")
		elif len(rInfo['last_name']) < 2:
			errors.append("Last name must be more than 1 character long")

		if not 'email' in rInfo:
			errors.append("Email is required")
		elif not EMAIL_REGEX.match(rInfo['email']):
			errors.append("Email address is not valid")
		else: 
			r = Reviewer.objects.filter(email=rInfo['email'])
			if len(r) > 0:
				return {'errors': ["Email already exists"]}
		
		if not 'password' in rInfo:
			errors.append("Password is required")
		elif not 'password_confirm' in rInfo:
			errors.append("Password confirmation is required")
		elif not rInfo['password'] == rInfo['password_confirm']:
			errors.append("Password confirmation must match password")
		elif not PW_REGEX.match(rInfo['password']):
			errors.append("Password must contain at least one number, one uppercase letter, and one lowercase letter")
		elif len(rInfo['password']) < 8:
			errors.append("Password must be at least 8 characters long")

		# check errors
		if len(errors) > 0:
			return {'errors': errors}
		else:
			# create new reviewer
			pwhash = bcrypt.hashpw(rInfo['password'].encode('utf-8'), bcrypt.gensalt())
			newtoken = uuid.uuid4()
			newR = Reviewer(first_name=rInfo['first_name'], last_name=rInfo['last_name'], email=rInfo['email'], password=pwhash, token=newtoken)
			newR.save()
			return {'token': newtoken}
	def retrieveToken(self, info):
		r = Reviewer.objects.filter(email=info['email'])
		if len(r) == 0:
			return {'errors': ["Invalid password or email"]}
		else:
			r = r[0]
			pwhash = r.password
			if bcrypt.hashpw(info['password'].encode('utf-8'), pwhash.encode('utf-8')) == pwhash:
				return {'token': r.token}
			else:
				return {'errors': ["Invalid password or email"]}
	def authenticate(self, rToken):
		r = Reviewer.objects.filter(token=rToken)
		if len(r) == 0:
			return {'errors': ["Invalid token"]}
		else:
			return r[0]

class Reviewer(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=200)
	token = models.CharField(max_length=200)
	created_at = models.DateTimeField
	objects = ReviewerManager()


class ReviewManager(models.Manager):
	def create(self, review):
		# Validations
		errors = []
		if not RATING_REGEX.match(str(review['rating'])):
			errors.append("Rating must be from 1 to 5")
		if len(review['title']) > 64:
			errors.append("Title must be less than 64 characters long")
		if len(review['summary']) > 10000:
			errors.append("Summary must be less than 10,000 characters long")
		if len(errors) > 0:
			return {'errors': errors}
		else:
			# Create new review
			rev = Review(rating=int(review['rating']), title=review['title'], summary=review['summary'], ip_address=review['ip_address'], company=review['company'], reviewer=review['reviewer'])
			rev.save()
			return {'success': True}
	def retrieve(self, reviewer):
		reviews = Review.objects.filter(reviewer=reviewer)
		return {'reviews': reviews}

class Review(models.Model):
	rating = models.PositiveSmallIntegerField()
	title = models.CharField(max_length=64)
	summary = models.TextField()
	ip_address = models.URLField()
	submitted_at = models.DateTimeField(auto_now_add = True)
	company = models.ForeignKey(Company)
	reviewer = models.ForeignKey(Reviewer)
	objects = ReviewManager()
