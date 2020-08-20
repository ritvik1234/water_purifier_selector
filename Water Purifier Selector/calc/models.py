from django.db import models

# Create your models here.
#pip install pillow for Image field
class Destination(models.Model):  #Yeh isko model mei convert krne ke liye
    id: int #id ki toh zarurat bhi nhi hai ab, kyuki dbms mei apne aap id bn jati hai
    quality = models.CharField(max_length=100)
    bacteria =  models.CharField(max_length=100)    #Specify the folder name . You have to specify the path.Here you have to specify kaha upload krni hai image
    electricity = models.CharField(max_length=100) #DOnt have to specify the size
    budget = models.CharField(max_length=100)
    purifier = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')

#You have to migrate your model to the database
