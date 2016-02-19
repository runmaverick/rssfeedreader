import datetime
import feedparser
# Create your views here.

#from django.http import HttpResponse

'''def index(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/index.html', {'posts':posts})
'''
'''
def fetch_feeds(request):
	hindu_gen_feed = feedparser.parse('http://www.thehindu.com/news/national/andhra-pradesh/?service=rss')
	deccan_herald_feed = feedparser.parse('http://www.deccanherald.com/rss/delhi.rss')
	hbl_feed = feedparser.parse('http://www.thehindubusinessline.com/features/smartbuy/automobiles/?service=rss')
	hbl_bank_feed = feedparser.parse('http://www.thehindubusinessline.com/industry-and-economy/banking/?service=rss')
	hindu_carir_feed = feedparser.parse('http://www.thehindu.com/education/careers/?service=rss')
	hindu_argri_feed = feedparser.parse('http://www.thehindu.com/sci-tech/agriculture/?service=rss')
	hindu_cenima_feed = feedparser.parse('http://www.thehindu.com/arts/cinema/?service=rss')
'''
posts = []
def feed():
	posts.append (pull_feed('http://www.thehindu.com/news/national/andhra-pradesh/?service=rss', 3))
	posts.append (pull_feed('http://www.deccanherald.com/rss/delhi.rss', 3))
	#for d in posts:
	#	print d
	print posts[0]
	return {'posts':posts}



def pull_feed(feed_url, posts_to_show):
	feed = feedparser.parse(feed_url)

	for i in range(posts_to_show):
		pub_date = feed['entries'][i].updated_parsed
		published = datetime.date(pub_date[0], pub_date[1], pub_date[2] )
		posts.append({
			'title': feed['entries'][i].title,
			'summary': feed['entries'][i].summary,
			'link': feed['entries'][i].link,
			'date': published,
			})
		
	return 1

feed()