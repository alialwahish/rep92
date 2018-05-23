from django.shortcuts import render,redirect
from .models import Users,Quotes
from django.contrib import messages



def index(request):
    return redirect('/main')

def main(request):
    return render(request,'applogReg/index.html')

def register(request):
    print ("registering user")
    if  Users.objects.register(request):
        print ('user created')
        
        messages.add_message(request,messages.INFO,"User Added")
        return redirect('/main')
    else:
        return redirect('/main')
    
def login(request):
    
    if(Users.objects.login(request)):
        print('back to view added the user')
        print(request.session['logged'])
        return redirect('/quotes')
    else:
        return redirect('/main')




def logout(request):
    request.session['logged']=""
    return redirect('/')

def quotes(request):
    id=request.session['logged']
    user=Users.objects.get(id=id)
    
    quotes=Quotes.objects.all()
    nonFav=[]
    for unfavQut in quotes:
        if unfavQut not in user.user_fav_quotes.all():
            nonFav.append(unfavQut)
    print(nonFav)

    return render(request,'applogReg/quotes.html',{'user':user , 'quotes':quotes ,'nonFav':nonFav})

def add_quote(request):
    Quotes.objects.add_quote(request)
        
    return redirect('/quotes')

def add_fav(request,id):
    Quotes.objects.add_fav(request,id)
    return redirect('/quotes')


def view_user(request,id):
    user=Users.objects.get(id=id)

    return render(request,'applogReg/viewUser.html',{'user':user})

def remove_fav_quote(request,id):
    Quotes.objects.remove_fav_quote(request,id)
    print("removed favorite quote")
    return redirect('/quotes')