from __future__ import unicode_literals
## inherit attributes from Django's User class
from django.contrib.auth.models import User
from django.db import models

## sub-class model 'UserAccount' inheriting from django's User model class
class UserAccount( User ):
    ## the super-class already has name , email , password
    ## the extra data we are adding is the telephone number
    phoneNumber = models.IntegerField()
    ## python equivalent of Java's .toString() method
    def __str__( self ) :
        toReturn = 'email = ' + self.email
        return toReturn

## article model
class Article( models.Model ) :
    articleType     = models.CharField( max_length = 100 )
    author          = models.CharField( max_length = 1000 )
    headline        = models.CharField( max_length = 1000 )
    body            = models.CharField( max_length = 1000000000000 )
    publicationDate = models.DateField()

    ## python equivalent of Java's .toString() method
    def __str__( self ) :
        ## build + return string representation
        toReturn = 'Type = ' + self.articleType + ", "
        toReturn = toReturn + 'Headline = ' + self.headline
        return toReturn

## comment model
class Comment( models.Model ) :
    username        = models.ForeignKey( UserAccount )
    articleID       = models.ForeignKey( Article )
    post            = models.CharField( max_length = 10000 )
    publicationDate = models.DateField()
    email           = models.CharField( max_length = 254 )

    ## python equivalent of Java's .toString() method
    def __str__( self ) :
        ## build + return string representation
        toReturn = 'Username = ' + self.email + ", "
        toReturn = toReturn + 'Publication Date = ' + str( self.publicationDate )
        return toReturn

## like model
class Like( models.Model ) :
    typeOfLike = models.CharField( max_length = 10 )
    userID     = models.ForeignKey( UserAccount )
    articleID  = models.ForeignKey( Article )

    ## python equivalent of Java's .toString() method
    def __str__( self ) :
        ## return string representation
        return 'Type = ' + self.typeOfLike
