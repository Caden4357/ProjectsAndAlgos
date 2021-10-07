from django.db import models
from djchoices import ChoiceItem, DjangoChoices
import bcrypt 
import re 
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
#checking if email is proper email format 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"

        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"

        if len(postData['username']) < 4:
            errors["username"] = "User Name should be at least 4 characters"

        #checking for proper email format 
        if not EMAIL_REGEX.match(postData['email_address']):
            errors['email_address'] = "invalid email address"

        #checking for duplicate email address
        email_check = User.objects.filter(email_address = postData['email_address'])
        if email_check:
            errors['duplicate'] = "Email already registered to an account"

        username_check = User.objects.filter(username= postData['username'])
        if username_check:
            errors['duplicate'] = "Username already exists"
            
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"

        if postData['password'] != postData['pw_confirm']:
            errors['pw'] = "Passwords do not match"
        return errors

    def register(self, postData):
        #encrypting password with salt 
        pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        return User.objects.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            username = postData['username'],
            email_address = postData['email_address'],
            password = pw,
        )
    
    def authenticate(self, email_address, password):
        users = User.objects.filter(email_address=email_address)
        if users:
            user=users[0]
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return True
            else:
                return False

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# class ProfileManager(models.Manager):
#     def profile_manager(self, postData):
#         errors = {}
#         return errors
DEFAULT = 'images/blank-profile.jpg'
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    # using sorl.thumbnail with pillow to upload profile pics the the default is givin automatically when a user/profile are made 
    image = ImageField(upload_to='profiles', default=DEFAULT)
    # objects = ProfileManager()
    def __str__(self):
        return self.user.username

# the @receiver works like a satelite looking for signals of a user object being made everytime a user object is made it will automatically create a profile under that users username
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Create a new profile object when a new user is created 
    if created:
        Profile.objects.create(user=instance)

class StoryManager(models.Manager):
    def story_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be 2 or more characters"
        if len(postData['content']) < 10:
            errors['content'] = "Story must be 10 or more characters"
        return errors

class Story(models.Model):
    ACTION = 'action'
    COMEDY = 'comedy'
    SCIFI = 'sci-fi/fantasy'
    THRILLER = "thriller"
    HORROR = 'horror'
    DRAMA = 'drama'
    ROMANCE = 'romance'
    CHOICES = (
        (ACTION, 'action'),
        (COMEDY, 'comedy'),
        (SCIFI, "sci-fi/fantasy"),
        (THRILLER, 'mystery/thriller'),
        (HORROR, "horror"),
        (DRAMA, 'drama'),
        (ROMANCE, 'romance')
    )
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, choices=CHOICES, default=None)
    content = models.TextField(max_length=100000)
    writer_of_the_story = models.ForeignKey(User, related_name="author_of_the_story", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name='liked_stories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = StoryManager()
