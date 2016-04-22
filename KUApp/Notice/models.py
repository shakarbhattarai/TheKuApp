from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Notices(models.Model):
	sender_name=models.CharField(max_length=30)
	sender_department=models.CharField(max_length=30)
	post_on=models.DateTimeField()
	content=models.CharField(max_length=250)


class Target(models.Model):
	Departments=(
		   ('Computer Science','CS'),
		   ('Computer Engineering','CE'),
		   ('Civil Engineering','Civil'),
		   ('Electrical and Electronics Engineering','EE'),
		   ('Environment Engineering','ENE'),
		   ('Chemical Engineering','CHE'),
		   ('Mechanical Engineering','ME'),
		   ('Geomatics Engineering','GE'),
		   ('Biotechnology','BT'),
		   ('Pharmacy','BP'),
		   ('Environment Science','ES'),
		   ('Applied Physics','AP'),
		   ('Human Biology','HB'),
		   ('Law','Law')

		)
	Semesters=(
			('First','1st'),
			('Second','2nd'),
			('Third','3rd'),
			('Fourth','4th'),
			('Fifth','5th'),
			('Sixth','6th'),
			('Seventh','7th'),
			('Eighth','8th'),
			('Ninth','9th'),
			('Tenth','10th'),	


		)


	notice=models.ForeignKey(Notices)
	department=models.CharField(choices=Departments,max_length=20)
	semester=models.CharField(choices=Semesters,max_length=20)

