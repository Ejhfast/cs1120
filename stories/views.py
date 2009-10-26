from django.http import HttpResponse
from cs1120.stories.models import Story

def index(request):
	latest_story_list = Story.objects.all().order_by('-rating')[:20] # take the top 20 rated stories
	output = ', '.join([s.body for s in latest_story_list])
	return HttpResponse(output)
	
def detail(request, story_id):
	return HttpResponse("You are looking at story %s." % story_id)
	
def comments(request, story_id):
	return HttpResponse("This will be a listing of all the comments for story %s." % story_id)