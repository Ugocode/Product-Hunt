from django.shortcuts import render, redirect
#add this to import abilities to authenticate users 
from django.contrib.auth.models import User 
from django.contrib import auth 

# Create your views here.
#creating the pages for that shows the accounts views properties 


def signup(requests):
	if requests.method == 'POST':
		#user wants to sign up and has filled the form 
		#To make sure the two passwords match we do: 
		#Also take note that the spellings of your username and password must be the same with what you have on the signup.html form page
		if requests.POST['Password1'] == requests.POST['Password2']:
			#after its confired we check if the username has been used before
			try:
				user = User.objects.get(username=requests.POST['Username'])
				return render(requests, 'accounts/signup.html', {'error': 'ERROR: This Username has already been taken'})

		# Now if there are no issues we say:
			except User.DoesNotExist:
				user = User.objects.create_user(requests.POST['Username'], password = requests.POST['Password1'])
				auth.login(requests, user)
				#then we redirect them to the homepage
				return redirect('home')

		#Now if the two passwords are not thesame it throws an error:
		if requests.POST['Password1'] != requests.POST['Password2']:
			return render(requests, 'accounts/signup.html', {'error2': 'ERROR: The Passwords Does Not Match'})

	else:

		#user wants to enter info 

		return render(requests, 'accounts/signup.html' )



def index(requests):
	#to chekc if this is a post request we say:
	
		
     return render(requests, 'accounts/index.html')



def login(requests):
	#to chekc if this is a post request we say:
	if requests.method == 'POST':
		#To make sure the user is in our database we do:
		user = auth.authenticate(username=requests.POST['Username'], password=requests.POST['Password'])
		#after it has gone through that line of code we now say:
		if user is not None:
			# that is user is found in the database:
			auth.login(requests, user)
			return redirect('home')

		else:
			return render(requests, 'accounts/login.html', {'error': 'Username or Password is incorrect'})

	else:
		return render(requests, 'accounts/login.html')


def logout(requests):
	if requests.method == 'POST':
		auth.logout(requests)
		return redirect('home')
	#TODO need to route to homepage
	# and dont forget to logout
	


