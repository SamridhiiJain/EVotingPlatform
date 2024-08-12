from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

#voter login register and profile 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        aadhar_no =  request.POST.get('aadhar_no')
        voterID_no =  request.POST.get('voterID_no')
        
        if not username:
            messages.error(request, 'Username is required')
            return redirect('login')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('login')
        if not aadhar_no:
            messages.error(request, 'Aadhar number is required')
            return redirect('login')
        if not voterID_no:
            messages.error(request, 'Voter ID number is required')
            return redirect('login')
        user = authenticate(request, username=username, password=password, aadhar_no=aadhar_no, voterID_no=voterID_no)
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        if not user.groups.exists(): # Check if user has a group
            messages.error(request, '!Contact your administrator')
            return redirect('login')
        groups = user.groups.all()   # Get the first group name
        if len(groups)>0 and groups[0].name == 'voter':
            messages.error(request, 'You are not authorized to login!')
        login(request, user)
        return redirect('voter')
    
    return render(request, 'accounts/login_voter.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        aadhar_no = request.POST.get('aadhar_no')
        voterID_no = request.POST.get('voterID_no')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        
        if not first_name:
            messages.error(request, 'First Name is required')
            return redirect('register')
        if not last_name:
            messages.error(request, 'Last Name is required')
            return redirect('register')
        if not username:
            messages.error(request, 'Username is required')
            return redirect('register')
        if not aadhar_no:
            messages.error(request, 'Aadhar number is required')
            return redirect('register')
        if not voterID_no:
            messages.error(request, 'Voter ID number is required')
            return redirect('register')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('register')
        if not cpassword:
            messages.error(request, 'Confirm Password is required')
            return redirect('register')
        if not email:
            messages.error(request, 'Email is required')
            return redirect('register')
        
        if password != cpassword:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        if User.objects.filter(aadhar_no=aadhar_no).exists():
            messages.error(request, 'already registered')
            return redirect('register')
        if User.objects.filter(voterID_no=voterID_no).exists():
            messages.error(request, 'already registered')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username is already Taken')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is taken')
            return redirect('register')
        user = User(first_name=first_name, last_name=last_name,aadhar_no=aadhar_no,voterID_no=voterID_no, username=username, email=email)
        user.set_password(password)
        user.save()

        group = Group.objects.get(name='Voter')
        user.groups.add(group)

        messages.success(request, 'Account created successfully')

        return redirect('login')

    return render(request, 'accounts/register_voter.html')

def voter_view(request):
    return render(request, 'accounts/voter.html')

#candidate login register and profile

def clogin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        aadhar_no =  request.POST.get('aadhar_no')
        voterID_no =  request.POST.get('voterID_no')
        
        if not username:
            messages.error(request, 'Username is required')
            return redirect('candidate_login')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('candidate_login')
        if not aadhar_no:
            messages.error(request, 'Aadhar number is required')
            return redirect('candidate_login')
        if not voterID_no:
            messages.error(request, 'Voter ID number is required')
            return redirect('candidate_login')
        user = authenticate(request, username=username, password=password, aadhar_no=aadhar_no, voterID_no=voterID_no)
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('candidate_login')
        if not user.groups.exists():                    # Check if user has a group
            messages.error(request, '!Contact your administrator')
            return redirect('candidate_login')
        groups = user.groups.all()       # Get the first group name
        if len(groups)>0 and groups[0].name == 'candidate':
            messages.error(request, 'You are not authorized to login!')
            return redirect('candidate_login')
    
    return render(request, 'accounts/login_candidate.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        aadhar_no = request.POST.get('aadhar_no')
        voterID_no = request.POST.get('voterID_no')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        
        if not first_name:
            messages.error(request, 'First Name is required')
            return redirect('candidate_register')
        if not last_name:
            messages.error(request, 'Last Name is required')
            return redirect('candidate_register')
        if not username:
            messages.error(request, 'Username is required')
            return redirect('candidate_register')
        if not aadhar_no:
            messages.error(request, 'Aadhar number is required')
            return redirect('candidate_register')
        if not voterID_no:
            messages.error(request, 'Voter ID number is required')
            return redirect('candidate_register')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('candidate_register')
        if not cpassword:
            messages.error(request, 'Confirm Password is required')
            return redirect('candidate_register')
        if not email:
            messages.error(request, 'Email is required')
            return redirect('candidate_register')
        
        if password != cpassword:
            messages.error(request, 'Passwords do not match')
            return redirect('candidate_register')
        if User.objects.filter(aadhar_no=aadhar_no).exists():
            messages.error(request, 'already registered')
            return redirect('candidate_register')
        if User.objects.filter(voterID_no=voterID_no).exists():
            messages.error(request, 'already registered')
            return redirect('candidate_register')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username is already Taken')
            return redirect('candidate_register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is taken')
            return redirect('candidate_register')
        user = User(first_name=first_name, last_name=last_name,aadhar_no=aadhar_no,voterID_no=voterID_no, username=username, email=email)

        user.set_password(password)
        user.save()
        group = Group.objects.get(name='candidate')
        user.groups.add(group)
        messages.success(request, 'Account created successfully')
        return redirect('candidate_login')

    return render(request, 'accounts/register_candidate.html')

def candidate_view(request):
    return render(request, 'accounts/candidate.html')


#party login register dashboard 

def plogin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        party_registration_no =  request.POST.get('party_registration_no')
        
        if not username:
            messages.error(request, 'Username is required')
            return redirect('party_login')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('party_login')
        if not party_registration_no:
            messages.error(request, 'party registration number is required')
            return redirect('party_login')
        user = authenticate(request, username=username, password=password, party_registration_no=party_registration_no, )
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('party_login')
        if not user.groups.exists():                    # Check if user has a group
            messages.error(request, '!Contact your administrator')
            return redirect('party_login')
        groups = user.groups.all()       # Get the first group name
        if len(groups)>0 and groups[0].name == 'party':
            messages.error(request, 'You are not authorized to login!')
            return redirect('party_login')
    
    return render(request, 'accounts/login_party.html')

def pregister_view(request):
    if request.method == 'POST':
        party_name = request.POST.get('party_name')
        username = request.POST.get('username')
        party_registration_no = request.POST.get('party_registration_no')
        
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        
        if not party_name:
            messages.error(request, 'party Name is required')
            return redirect('party_register')

        if not username:
            messages.error(request, 'Username is required')
            return redirect('party_register')
        if not party_registration_no:
            messages.error(request, 'party registration number is required')
            return redirect('party_register')
    
        if not password:
            messages.error(request, 'Password is required')
            return redirect('party_register')
        if not cpassword:
            messages.error(request, 'Confirm Password is required')
            return redirect('party_register')
        if not email:
            messages.error(request, 'Email is required')
            return redirect('party_register')
        
        if password != cpassword:
            messages.error(request, 'Passwords do not match')
            return redirect('party_register')
        if User.objects.filter(party_registration_no=party_registration_no).exists():
            messages.error(request, 'already registered')
            return redirect('party_register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username is already Taken')
            return redirect('party_register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is taken')
            return redirect('party_register')
        user = User(party_name=party_name,party_registration_no=party_registration_no, username=username, email=email)

        user.set_password(password)
        user.save()
        group = Group.objects.get(name='party')
        user.groups.add(group)
        messages.success(request, 'Account created successfully')
        return redirect('party_login')

    return render(request, 'accounts/register_party.html')

def party_view(request):
    return render(request, 'accounts/party.html')




#logout view
def logout_view(request):
    return redirect('index')