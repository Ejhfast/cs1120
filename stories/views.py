from django.http import HttpResponse
from cs1120.stories.models import Story, StoryForm
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	latest_story_list = Story.objects.all().order_by('-rating')[:20] # take the top 20 rated stories
	return render_to_response('stories/index.html', {'latest_story_list':latest_story_list}) # loads index.html template with context of latest_story_list and renders the result

def detail(request, story_id):
	s = get_object_or_404(Story, pk=story_id)
	return render_to_response("stories/detail.html", {'story' :s})
	
def upvote(request, story_id):
	s = get_object_or_404(Story, pk=story_id)
	s.rating += 1
	s.save()
	return render_to_response("stories/vote.html", {'story_id' :story_id, 'type' : 'upvote', 'story':s})
	
def downvote(request, story_id):
	s = get_object_or_404(Story, pk=story_id)
	s.rating -= 1
	s.save()
	return render_to_response("stories/vote.html", {'story_id' :story_id, 'type' : 'downvote', 'story' : s})
	
def newpost(request):
	s = StoryForm()
	return render_to_response('stories/addstory.html', {'story_form' : s})

def addpost(request):
	s = StoryForm(request.POST)
	s.save()
	latest_story_list = Story.objects.all().order_by('-rating')[:20] # take the top 20 rated stories
	return render_to_response('stories/index.html', {'latest_story_list':latest_story_list}) # loads index.html template with context of latest_story_list and renders the result
	
