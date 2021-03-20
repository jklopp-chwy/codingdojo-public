from django.db import models, IntegrityError
import bcrypt


# Create your models here.
class RegisterManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors["passwords"] = "Passwords should match"
        ##checks to see if the email address has already been used
        form_email_address = postData['email_address']
        if Register.objects.filter(email_address = form_email_address).first():
            errors["email_address"] = "Email address is already registered"
        return errors

    def login_validator(self, postData):
        login_errors = {}
        ##is user in database?
        returning_user = postData['email_address']
        existing_user = Register.objects.filter(email_address = returning_user).first()
        ##if user exists:
        if existing_user:
            #if user exists, but password is incorrect
            if existing_user.password != postData['password']:
                login_errors["password_check"] = "Password is invalid"
        #if user does not exist:
        else:
            login_errors["user_check"] = "User is invalid"
        return login_errors



class Register(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address= models.CharField(max_length=45)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegisterManager()

class Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(Register, related_name="user_messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(Register, related_name="user_comments", on_delete=models.CASCADE)
    wall_message = models.ForeignKey(Message, related_name="post_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)