from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .form import NewForm
from .commentForm import CommentForm
from .models import Category,Receipe,Comment,Bookmark

def homepage(request):
	return render(request,'main/homepg.html',None)

def register(request):
	if request.method == 'POST':
		form = NewForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Congratulations!!You have been registered.')
			login(request, user)
			return redirect("main:homepage")
		else:
			for err in form.errors.values():
				messages.error(request,f'{err}')
			return render(request,"main/register.html",{'form':form})


	form  = NewForm
	return render(request,"main/register.html",{'form':form})

def logoutform(request):
	logout(request)
	messages.success(request,f'Successfully loggedout!!')
	return redirect("main:homepage")

def loginform(request):
	if request.method == 'POST':
		form = AuthenticationForm(request = request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username,password = password)
			if user is not None:
				messages.success(request,'Successfully logged in!!')
				login(request,user)
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.Try again!!!")
		else:
				messages.error(request,"Invalid username or password.Try again!!!")

	form = AuthenticationForm()
	return render(request,"main/login.html",{'form':form})

def categories(request):
	if request.method=='GET':
		return render(request,'main/categories.html',{'categories':Category.objects.all})

def single_slug(request,single_slug):
	#Slug matching for category
	categories = [r.category_slug for r in Category.objects.all()]
	if single_slug in categories:
		matching = Receipe.objects.filter(category_title__category_slug=single_slug)
		return render(request,"main/receipes.html",{"receipes":matching})

	#Slug matching for receipe

	receipe = [r.receipe_slug for r in Receipe.objects.all()]
	if single_slug in receipe:
		matching = Receipe.objects.get(receipe_slug=single_slug)
		new_comment = None
		accepted_comments = Comment.objects.filter(title__receipe_slug = single_slug,active = True)
		if request.method=='POST':
			#Dealing with bookmarks
			r = matching
			u = request.user
			if request.POST.get('action')=="0" and u.is_authenticated:
				Bookmark.objects.filter(user = u,receipe = r).delete()

			elif request.POST.get('action')=="1":
				if not Bookmark.objects.filter(user = u,receipe = r):
					adding = Bookmark.objects.create(user = u,receipe = r)
			#Dealing with comment section
			elif request.POST.get('action')=='comment-section':
				form = CommentForm(data = request.POST)
				if form.is_valid():
					new_comment = form.save(commit = False)
					new_comment.title = matching
					new_comment.save()

		form = CommentForm()
		if request.user.is_authenticated:
			bookmarkornot = Bookmark.objects.filter(user = request.user,receipe = matching,bookmark_or_not = True)
		else:
			bookmarkornot = None
		return render(request,"main/receipe_content.html",{'content':matching,'comments':accepted_comments,'form':form,'newcomment':new_comment,'bookmark':bookmarkornot})	
	return HttpResponse(f"{single_slug} not found!!")

def account(request,username):
	u = request.user
	if request.method == 'POST':
		r = request.POST.get("favourite")
		for x in Receipe.objects.all():
			if x.title ==r:
				receipe_object = x
		Bookmark.objects.filter(user = u,receipe = receipe_object).delete()

	return render(request,"main/bookmarks.html",{'bookmarks':Bookmark.objects.filter(user = u)})







