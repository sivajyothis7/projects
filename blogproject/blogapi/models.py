from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

#orm query for creating a resource
#modelname.objects.create(field1=value1,field2=value2...)

#orm query for fetching all objects
#qs=modelsname.objects.all()

#detailview of a specific object
#qs=modelname.objects.get(id=)

#update
#qs=modelname.objects.get(id=)
#qs.content
#qs.save()
#filter
#qs=modelname.objects.filter(band="4g")

#mobile=Mobiles.objects.filter(price__lt=32000)   #lt=lessthan  #lte essthan or =
#mobile=Mobiles.objects.filter(price__gt=32000)   #gt=greaterthan #gte= greaterthan or =

#qs=Mobiles.objects.filter(band="5g").count()
# qs=Mobiles.objects.filter(price__lt=25000,band="5g")


class Blogs(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=150)
    author=models.CharField(max_length=50)
    liked_by=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Mobiles(models.Model):
    name=models.CharField(max_length=100,unique=True)
    price=models.PositiveIntegerField(default=5000)
    band=models.CharField(max_length=100,default="4g")
    display=models.CharField(max_length=150)
    processor=models.CharField(max_length=120)

    def __str__(self):
        return self.name
    def average_rating(self):
        reviews=self.reviews_set.all()
        if reviews:
            rating=[rv.rating for rv in reviews]
            total=sum(rating)
            return total/len(reviews)
        else:
            return 0
    def total_reviews(self):
        return self.reviews_set.all().count()



#qs=Mobiles.objects.filter(band="5g").count()
# qs=Mobiles.objects.filter(price__lt=25000,band="5g")

#qs==>python==>json==>client

class Reviews(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Mobiles,on_delete=models.CASCADE)
    review=models.CharField(max_length=100)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    date=models.DateField(auto_now_add=True)

    class Meta:
        unique_together=("author","product")

    def __str__(self):
        return self.review

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Mobiles,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("incart","incart"),
        ("order_placed","order_placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=100,choices=options,default="incart")

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Mobiles,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("order-placed","order-placed"),
        ("dispatched","dispatched"),
        ("Intransit","Intransit"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=100,choices=options,default="order-placed")