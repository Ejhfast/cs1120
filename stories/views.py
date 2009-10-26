from django.http import HttpResponse

def index(request):
	return HttpResponse("This will be a listing of all the stories.")
	
def detail(request):
	return HttpResponse("You are looking at story %s." % story_id)
	
def comments(request):
	return HttpResponse("This will be a listing of all the comments for stroy %s." % story_id)