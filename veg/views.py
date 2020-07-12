from django.shortcuts import render, redirect
from django.http import HttpResponse
from veg.models import Vendor, Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
def shop(request):
    return render(request, 'veg/shop.html')

def about(request):
    return render(request, 'veg/about.html')

def signup(request):
    return render(request, 'veg/signup.html')


def pincode(request):
    if request.method=='POST':
        search = request.POST['pininput']
        if search:
            match = Vendor.objects.filter(Q(vendor_zip__icontains=search))
            if match:
                params = {'ven_nm' : match}
                return render(request, 'veg/vendor.html', params)
            else:
                messages.error(request, "Sorry ! No Vendors are available for this Pincode.")
                return render(request, 'veg/shop.html')

    return render(request, 'veg/403.html')
    

def customersignup(request):
    if request.method == 'POST':
        cusFirstname = request.POST['cusFirstname']
        cusLastname = request.POST['cusLastname'] 
        cusUsername = request.POST['cusUsername']
        cusContact = request.POST['cusContact']
        cusEmail = request.POST['cusEmail']
        cusPassword = request.POST['cusPassword']
        cusPassword2 = request.POST['cusPassword2']
        cusAddress = request.POST['cusAddress']
        cusCity = request.POST['cusCity']
        cusState = request.POST['cusState']
        cusZip = request.POST['cusZip']


        duplicate = User.objects.filter(Q(username__icontains=cusUsername))
        if duplicate:
            messages.error(request, "Username already exist !")
            return redirect('signup')
        
        if not cusUsername.isalnum():
            messages.error(request, "Username should only contain Letters & Numbers !")
            return redirect('signup')

        if len(cusPassword) < 6:
            messages.error(request, "Password must be atleast 6 characters.")
            return redirect('signup')

        if not cusContact.isnumeric():
            messages.error(request, "Contact must be Numeric and equal to 10 digits !")
            return redirect('signup')

        if not len(cusContact)==10:
            messages.error(request, "Contact must be Numeric and equal to 10 digits !")
            return redirect('signup')

        if not cusPassword==cusPassword2:
            messages.error(request, "Passwords Not Matching")
            return redirect('signup')

        if not cusZip.isnumeric():
            messages.error(request, "Zip must be Numeric and equal to 6 digits !")
            return redirect('signup')

        if not len(cusZip)==6:
            messages.error(request, "Zip must be Numeric and equal to 6 digits !")
            return redirect('signup')



        myuser = User.objects.create_user(cusUsername, cusEmail, cusPassword)
        myuser.first_name = cusFirstname
        myuser.last_name = cusLastname
        myuser.save()

        customer = Customer(customer_firstname=cusFirstname, customer_lastname=cusLastname,
        customer_username=cusUsername, customer_contact=cusContact,customer_email=cusEmail, customer_address=cusAddress,
        customer_city=cusCity, customer_state=cusState, customer_zip=cusZip)
        customer.save()
        
        
        messages.success(request, 'User Created Successfully !')
        return redirect('signup')   

    elif not request.method == 'POST':
        return render(request, 'veg/403.html')

    else:
        messages.error(request, 'Error !')
        return redirect('signup')
    


def vendorsignup(request):
    if request.method == 'POST':
        venFirstname = request.POST['venFirstname']
        venLastname = request.POST['venLastname'] 
        venUsername = request.POST['venUsername']
        venContact = request.POST['venContact']
        venEmail = request.POST['venEmail']
        venPassword = request.POST['venPassword']
        venPassword2 = request.POST['venPassword2']
        venAddress = request.POST['venAddress']
        venCity = request.POST['venCity']
        venState = request.POST['venState']
        venZip = request.POST['venZip']


        duplicate = User.objects.filter(Q(username__icontains=venUsername))
        if duplicate:
            messages.error(request, "Username already exist !")
            return redirect('signup')

        if not venUsername.isalnum():
            messages.error(request, "Username should only contain Letters & Numbers !")
            return redirect('signup')

        if len(venPassword) < 6:
            messages.error(request, "Password must be atleast 6 characters.")
            return redirect('signup')

        if not venContact.isnumeric():
            messages.error(request, "Contact must be Numeric and equal to 10 digits !")
            return redirect('signup')

        if not len(venContact)==10:
            messages.error(request, "Contact must be Numeric and equal to 10 digits !")
            return redirect('signup')

        if not venPassword==venPassword2:
            messages.error(request, "Passwords Not Matching")
            return redirect('signup')

        if not venZip.isnumeric():
            messages.error(request, "Zip must be Numeric and equal to 6 digits !")
            return redirect('signup')

        if not len(venZip)==6:
            messages.error(request, "Zip must be Numeric and equal to 6 digits !")
            return redirect('signup')

        myuser = User.objects.create_user(venUsername, venEmail, venPassword)
        myuser.first_name = venFirstname
        myuser.last_name = venLastname
        myuser.save()

        vendor = Vendor(vendor_firstname=venFirstname, vendor_lastname=venLastname,
        vendor_username=venUsername, vendor_contact=venContact,vendor_email=venEmail, vendor_address=venAddress,
        vendor_city=venCity, vendor_state=venState, vendor_zip=venZip)
        vendor.save()

        messages.success(request, 'User Created Successfully !')
        return redirect('signup') 

    elif not request.method == 'POST':
        return render(request, 'veg/403.html')  

    else:
        messages.error(request, 'Error!')
        return redirect('signup')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']


        user = authenticate(username=loginusername, password=loginpassword)


        if loginusername:
            match = Vendor.objects.filter(Q(vendor_username__icontains=loginusername))
            if match:
                if user is not None:
                    login(request, user)

                    user_name = request.user.username
                    ven_data = Vendor.objects.get(vendor_username = user_name)

                    params = {'ven_nm' : match, 'ven' : ven_data}
                    return render(request, 'veg/ven_catalogue.html', params)

                else:
                    messages.error(request, 'Invalid Credentials ! Please try again...')
                    return redirect('shop')

            else:
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfully Logged In !')
                    return render(request, 'veg/pincode.html')

                else:
                    messages.error(request, 'Invalid Credentials ! Please try again...')
                    return redirect('shop')


    return render(request, 'veg/403.html')

def handlelogout(request):
    logout(request)
    return redirect('shop')


def update_catalogue(request):
    if request.method == 'POST':

        user_name = request.user.username
        post = Vendor.objects.get(vendor_username=user_name)


        vendor_contact = request.POST['vendor_contact']
        apple = request.POST['apple']
        banana = request.POST['banana']
        broccoli = request.POST['broccoli']
        cabbage = request.POST['cabbage']
        capsicum = request.POST['capsicum']
        carrot = request.POST['carrot']
        cauliflower = request.POST['cauliflower']
        chilly = request.POST['chilly']
        coriander = request.POST['coriander']
        cucumber = request.POST['cucumber']
        garlic = request.POST['garlic']
        ginger = request.POST['ginger']
        grapes = request.POST['grapes']
        guava = request.POST['guava']
        jackfruit = request.POST['jackfruit']
        lemon = request.POST['lemon']
        lychee = request.POST['lychee']
        mango = request.POST['mango']
        mushroom = request.POST['mushroom']
        onion = request.POST['onion']
        orange = request.POST['orange']
        papaya = request.POST['papaya']
        pear = request.POST['pear']
        pea = request.POST['pea']
        pineapple = request.POST['pineapple']
        pomegranate = request.POST['pomegranate']
        potato = request.POST['potato']
        pumpkin = request.POST['pumpkin']
        scallion = request.POST['scallion']
        spinach = request.POST['spinach']
        tomato = request.POST['tomato']
        turnip = request.POST['turnip']
        watermelon = request.POST['watermelon']

        post.vendor_contact = vendor_contact
        post.apple = apple
        post.banana = banana
        post.broccoli = broccoli
        post.cabbage = cabbage
        post.capsicum = capsicum
        post.carrot = carrot
        post.cauliflower = cauliflower
        post.chilly = chilly
        post.coriander = coriander
        post.cucumber = cucumber
        post.garlic = garlic
        post.ginger = ginger
        post.grapes = grapes
        post.guava = guava
        post.jackfruit = jackfruit
        post.lemon = lemon
        post.lychee = lychee
        post.mango = mango
        post.mushroom = mushroom
        post.onion = onion
        post.orange = orange
        post.papaya = papaya
        post.pear = pear
        post.pea = pea
        post.pineapple = pineapple
        post.pomegranate = pomegranate
        post.potato = potato
        post.pumpkin = pumpkin
        post.scallion = scallion
        post.spinach = spinach
        post.tomato = tomato
        post.turnip = turnip
        post.watermelon = watermelon

        post.save()

        messages.success(request, 'Catalogue Updated Successfully !')    
        return redirect('shop') 
    return render(request, 'veg/403.html')
            

def ven_to_cata(request):
    if request.method == 'POST':
        ven_n = request.POST.get('ven_name')
        ven_val = Vendor.objects.get(vendor_username = ven_n)
        param = {'ven' : ven_val}
        return render(request, 'veg/cus_catalogue.html', param)
    return render(request, 'veg/403.html')


    