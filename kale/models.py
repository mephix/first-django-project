from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
        



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('Made available on this date') # The classes on offer will have to be renewed or updated regularly.
                                                                    # At least for the "What class do you want to do" question, we need to # track when the choice of a particular option was offered.
                                                                    #Adding this in made it go wrong, though.
                                                                    
    #def still_active(self): # Shows whether the choice was made available in the last four weeks.
     #   return self.pub_date >= timezone.now() - datetime.timedelta(days=28)
     # Kept in case I can work out what problem this caused.
                                                                    
    students = models.IntegerField(default=0) #Counts how many prospective students have picked this option - we'll need this to know when                                         # the minimum class size is reached.
    
    def __str__(self):
        return self.choice_text
        
