from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from cs1120.stories.models import Story, StoryForm, UserForm
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	latest_story_list = Story.objects.all().order_by('-upvotes')[:20] # take the top 20 rated stories
	return render_to_response('stories/index.html', {'latest_story_list' : latest_story_list})

def detail(request, story_id):
	s = get_object_or_404(Story, pk=story_id)
	return render_to_response("stories/detail.html", {'story' :s})
	
def upvote(request, story_id):
	if request.user.is_authenticated():
		s = get_object_or_404(Story, pk=story_id)
		s.upvotes += 1
		s.save()
	return render_to_response("stories/vote.html", {'story_id' :story_id, 'type' : 'upvote', 'story':s})
	
def downvote(request, story_id):
	if request.user.is_authenticated():
		s = get_object_or_404(Story, pk=story_id)
		s.downvotes += 1
		s.save()
	return render_to_response("stories/vote.html", {'story_id' :story_id, 'type' : 'downvote', 'story' : s})
	
def newpost(request):
	if request.user.is_authenticated():
		s = StoryForm()
		return render_to_response('stories/addstory.html', {'story_form' : s})
	else:
		return HttpResponseRedirect("/posts/")

def addpost(request):
	if request.user.is_authenticated():
		s = StoryForm(request.POST)
		s.save()
		latest_story_list = Story.objects.all().order_by('-upvotes')[:20] 
	return render_to_response('stories/index.html', {'latest_story_list':latest_story_list}) 

def newuser(request):
	u = UserCreationForm()
	return render_to_response('stories/adduser.html', {'user_form' : u})

def adduser(request):
	u = UserCreationForm(data=request.POST)
	u.save()
	latest_story_list = Story.objects.all().order_by('-upvotes')[:20] 
	return render_to_response('stories/index.html', {'latest_story_list':latest_story_list}) 

