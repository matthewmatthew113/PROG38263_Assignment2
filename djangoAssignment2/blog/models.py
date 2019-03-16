#Import Various Django Libraries such as timezones
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

#Model for posts in blog
class Post(models.Model):
	#100 character-limit field for title
    title = models.CharField(max_length=100)
    #Textfield for content of post
    content = models.TextField()
    #Sets the date of posting to the currect timezone date
    date_posted = models.DateTimeField(default=timezone.now)
    #Sets the author of said posting to the designated user and is required, deleting said variable will result in the entire entry being deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	
    def __str__(self):
        return self.title
		
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})