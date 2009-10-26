from django.http import HttpResponse
from cs1120.stories.models import Story
from django.template import Context, loader

def index(request):
	latest_story_list = Story.objects.all().order_by('-rating')[:20] # take the top 20 rated stories
	output = ', '.join([s.body for s in latest_story_list])	# seperate each story by a comma
	template = loader.get_template('stories/index.html')	# load html template for display
	context = Context({	
		'latest_story_list' : latest_story_list,			# create new context with the 20 stories
	})
	
	
	return HttpResponse(template.render(context))	# render the context (list of stories) in the template
	
def detail(request, story_id):
	return HttpResponse("You are looking at story %s." % story_id)
	
def comments(request, story_id):
	return HttpResponse("This will be a listing of all the comments for story %s." % story_id)