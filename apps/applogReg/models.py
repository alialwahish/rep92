from django.db import models
from django.db import models
from django.contrib import messages
from django.contrib.messages import get_messages
import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-copyZ0-9._-]+\.[a-zA-Z]+$')
from passlib.hash import sha256_crypt





class userManager(models.Manager):
    def register(self,request):
        if len(request.POST["name"]) < 3:
            messages.add_message( request, messages.ERROR, "Name Can't be less than 3 characters!" )
        if len(request.POST["alias"]) < 1:
            messages.add_message( request, messages.ERROR, "Email Can't be less than 3 characters!" )
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.add_message(request,messages.ERROR,"please use valid Email address")

        if len(request.POST["password"]) < 8:
            messages.add_message( request, messages.ERROR, "Password must be between 8-32 characters!" )
        if request.POST["password"] != request.POST["confirm_password"]:
            messages.add_message( request, messages.ERROR, "Password and Password Confirmation must match!" )

        today=datetime.date.today()
        if(request.POST["dob"] > str(today)):
            messages.add_message( request, messages.ERROR, "Date of birth Can't in the future!" )
       
        if len(request.POST["dob"]) < 1:
            messages.add_message( request, messages.ERROR, "Date of birth Can't be Empty!" )


        if Users.objects.filter(email=request.POST["email"]).count() > 0:
            messages.add_message( request, messages.ERROR, "A user with this email already exists!" )

        if len( get_messages(request) ) > 0:
            return False
        else:
            Users.objects.create(
            name = request.POST["name"],alias=request.POST["alias"],email = request.POST["email"],password = sha256_crypt.hash(request.POST['password']),dob=request.POST['dob'])

            return True

    def login(self,request):
        print('login user')
        try:
            print(request.POST['email'])
            
            user = Users.objects.get(email=request.POST['email'])
            print(user.email)
                       
            if sha256_crypt.verify(request.POST['password'], user.password):
                request.session['logged']=user.id

                print("Password match")
          
                return True
            else:
                
                messages.add_message( request, messages.ERROR, "Wrong Password!" )
                return False        
        
        except:
            messages.add_message( request, messages.ERROR, "User doesn't exist!" )
            return False



class Users(models.Model):
    name = models.CharField(max_length =255)
    alias=models.CharField(max_length =255)
    email = models.CharField(max_length =255)
    password = models.CharField(max_length =255)
    dob=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=userManager()



class qoutesManager(models.Manager):
    def add_quote(self,request):
        
        if len(request.POST["quoted_by"]) < 3:
            messages.add_message( request, messages.ERROR, "Name Can't be less than 3 characters!" )
        if len(request.POST["content"]) < 10:
            messages.add_message( request, messages.ERROR, "Message Can't be less than 10 characters!" )

        else:
            id=request.session['logged']
            user=Users.objects.get(id=id)
            Quotes.objects.create(user=user,content=request.POST["content"],
            quoted_by=request.POST["quoted_by"]        
            )
    
    
    def add_fav(self,request,quote_id):
        id=request.session['logged']
        user=Users.objects.get(id=id)
        user.save()
        print(quote_id,"the user :",user.name)
        quote=Quotes.objects.get(id=quote_id)

        quote.user_fav_quotes.add(user)

        quote.save()
        


        return True
    def remove_fav_quote(self,request,quote_id):
        id=request.session['logged']
        user=Users.objects.get(id=id)
        user.save()
        print(quote_id,"the user :",user.name)

        print("removing user from favorite quotes")
        print (user.user_fav_quotes.all())
        fav_quote=user.user_fav_quotes.get(id=quote_id)
        print(fav_quote.content)
        fav_quote.delete()
        fav_quote.save()
        
        return True
            


class Quotes(models.Model):
    user=models.ForeignKey(Users,on_delete=False,related_name='quotes')
    user_fav_quotes=models.ManyToManyField(Users,related_name='user_fav_quotes')
    quoted_by=models.CharField(max_length=255)
    content=models.TextField()
    objects=qoutesManager()
    

    

    

