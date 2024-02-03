from django.db import models

class Food(models.Model):
	food_id = models.CharField(max_length=50, null=True)
	name = models.CharField(max_length=50, null=True)
	stocks = models.IntegerField(blank=True)
	price = models.IntegerField(blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Movie(models.Model):
	movie_id = models.CharField(max_length=50, null=True)
	title = models.CharField(max_length=50, null=True)
	genre = models.CharField(max_length=50, null=True)
	description = models.TextField(blank=True)
	length = models.IntegerField(null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class TVShow(models.Model):
	tv_id = models.CharField(max_length=50, null=True)
	title = models.CharField(max_length=50, null=True)
	genre = models.CharField(max_length=50, null=True)
	season = models.CharField(max_length=50, null=True)
	episode = models.CharField(max_length=50, null=True)
	description = models.TextField(blank=True)
	length = models.IntegerField(null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	
PAYMENT_CHOICES = (
	("Gcash", "Gcash"), 
    ("Paymaya", "Paymaya"), 
    ("Credit Card", "Credit Card"), 
    ("Debit Credit", "Debit Card"), 
	)

DATE_CHOICES = (
	("1 Month", "1 Month"), 
    ("2 Months", "2 Months"), 
    ("3 Months", "3 Months"), 
    ("4 Months", "4 Months"),
    ("5 Months", "5 Months"), 
    ("6 Months", "6 Months"), 
    ("7 Months", "7 Months"), 
    ("8 Months", "8 Months"),
    ("9 Months", "9 Months"), 
    ("10 Months", "10 Months"), 
    ("11 Months", "11 Months"), 
    ("1 Year", "1 Year"), 
	)
	
class Subscription(models.Model):
	ID = models.IntegerField(null=True)
	name = models.CharField(max_length=50, null=True)
	email = models.EmailField(blank=True)
	phone = models.IntegerField(blank=True)
	date_subscription = models.DateTimeField(auto_now=True)
	payment = models.CharField(
		max_length = 20, 
        choices = PAYMENT_CHOICES, 
        default = '1'
        )
	date = models.CharField(
		max_length = 20, 
        choices = DATE_CHOICES, 
        default = '1'
        ) 

	def __str__(self):
		return self.name

class MovieStream(models.Model):
	name = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
	title = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
	stream_date = models.DateTimeField(auto_now_add=True)
	stream_time = models.DateTimeField(auto_now_add=True)

	def	__str__(self):
		return str(self.title)

class TVStream(models.Model):
	name = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
	title = models.ForeignKey(TVShow, on_delete=models.SET_NULL, null=True)
	stream_date = models.DateTimeField(auto_now_add=True)
	stream_time = models.DateTimeField(auto_now_add=True)
	
	def	__str__(self):
		return str(self.title)

class Feedback(models.Model):
	femails = models.EmailField(blank=True)
	feeds = models.CharField(max_length=250, null=True)

	def	__str__(self):
		return str(self.femails)