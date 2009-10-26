from django.http import HttpResponse
from cs1120.stories.models import Story
from django.shortcuts import render_to_response

def index(request):
	latest_story_list = Story.objects.all().order_by('-rating')[:20] # take the top 20 rated stories
	return render_to_response('stories/index.html', {'latest_story_list':latest_story_list}) # loads index.html template with context of latest_story_list and renders the result

def detail(request, story_id):
	return HttpResponse("You are looking at story %s." % story_id)
	
def comments(request, story_id):
	return HttpResponse("This will be a listing of all the comments for story %s." % story_id)