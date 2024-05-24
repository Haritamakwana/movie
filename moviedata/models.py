from django.db import models

citylist = [
    ("1", "ahmedabad"),
    ("2", "surat"),
    ("3", "baroda"),
    ("4", "bhavnagar"),
]

statelist = [
    ("1", "gujarat"),
    ("2", "maharashtra"),
    ("3", "goa"),
]
typelist = [
    ("1", "2-D"),
    ("2", "3-D"),
]

langlist = [
    ("1", "english"),
    ("2", "gujrati"),
    ("3", "hindi"),
]


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return self.name


class male_actor(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.name


class female_actor(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.name


class movie(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    actor = models.ForeignKey(male_actor, on_delete=models.CASCADE)
    actress = models.ForeignKey(female_actor, on_delete=models.CASCADE)
    movie_category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class multiplex(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    no_of_screens = models.IntegerField()
    city = models.CharField(max_length=20, choices=citylist)
    state = models.CharField(max_length=20, choices=statelist)
    website = models.URLField()

    def __str__(self):
        return self.name


class shows(models.Model):
    movie_name = models.ForeignKey(movie, on_delete=models.CASCADE)
    multiplex = models.ForeignKey(multiplex, on_delete=models.CASCADE)
    showtime = models.DateTimeField()
    seats = models.IntegerField()
    ticket_price = models.IntegerField()
    type = models.CharField(max_length=20, choices=typelist)
    language = models.CharField(max_length=20, choices=langlist)
