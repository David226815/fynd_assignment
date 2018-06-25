from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
import json


@csrf_protect
def home(request):
	
	return render(request, 'home.html')


def read_json():
	j = []
	with open('imdb.json') as f:
		movie_data = json.loads(f.read())

	for data in movie_data:
		j = []
		for i in data['genre']:
			j.append(str(i))
		data['genre'] = j

	return movie_data #render(request, 'read_json.html', context=content)


@csrf_protect
def all_movies(request):
	data = read_json()

	content = {
		'movies_obj': data,
	}
	return render(request, 'view_movies.html', context=content)


@csrf_protect
def signup(request):
	"""
	Sign up new user from modal
	"""
	# user_name = request.POST.get('usrname1', None)
	# user_pass = request.POST.get('psw1', None)
	# user_mail = user_name
	# fname = request.POST.get('f_name', None)
	# mname = request.POST.get('m_name', None)
	# lname = request.POST.get('l_name', None)
	# mobile_number = request.POST.get('mobileno', None)
	# address = request.POST.get('addr', None)
	# x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	# if x_forwarded_for:
	# 	ip = x_forwarded_for.split(',')[0]
	# else:
	# 	ip = request.META.get('REMOTE_ADDR')
	# curr_u = request.user.id
	# sessionid = request.session.session_key
	# date_time = datetime.now()
	# """
	# One email id per user
	# ----------------------
	# Check if the email id already exists.
	# If the email id exists then send email to that account
	# """
	# check = checkuserexisits(user_mail)
	# if check is not None:
	# 	content = {
	# 		'first_name': fname,
	# 	}
	# 	page = "EMAIL-ALREADY-EXISTS"
	# 	datascience = {
	# 		"ip": ip,
	# 		"page": page,
	# 		"course": constants.EXAMINATION_TYPE_NONE,
	# 		"user_id": curr_u,
	# 		"datetime": date_time,
	# 		"session_id": sessionid,
	# 		"student_user_type": constants.STUDENT_FUNNEL_REGISTERED_ACTIVE,
	# 	}
    #
	# 	m_db.Analytics.insert(datascience)
    #
	# 	return render(request, 'email_already_exists.html', content)
	# else:
	# 	"""
	# 	Create new user object
	# 	"""
	# 	user = User.objects.create_user(username =sanitize_html(user_name),
	# 									email =sanitize_html(user_mail),
	# 									password =user_pass,
	# 									first_name=sanitize_all(fname),
	# 									last_name=sanitize_all(lname))
    #
	# 	user.save()
    #
	# 	entry_student = create_or_return_student_user(user, mobile_number, mname, address)
    #
	# 	user = auth.authenticate(username=sanitize_html(user_name), password=user_pass)
	# 	auth.login(request, user)
    #
	# 	page = "VALIDATE-EMAIL"
    #
	# 	datascience = {
	# 		"ip": ip,
	# 		"page": page,
	# 		"course": constants.EXAMINATION_TYPE_NONE,
	# 		"user_id": curr_u,
	# 		"datetime": date_time,
	# 		"session_id": sessionid,
	# 		"student_user_type": constants.STUDENT_FUNNEL_REGISTERED_INACTIVE,
	# 	}
    #
	# 	m_db.Analytics.insert(datascience)

	return HttpResponseRedirect('/validate-email/')

