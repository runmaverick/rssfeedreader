from django.shortcuts import render
from . models import Post
import datetime
from django.utils import timezone
import feedparser
import html2text
# Create your views here.

from django.http import HttpResponse

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
title = []
summary = []
link = []
published = []

def pull_feed(feed_url, posts_to_show):
	feed = feedparser.parse(feed_url)
	#if len(feed['entries']) < posts_to_show:
    #	posts_to_show = len(feed['entries'])
	for i in range(posts_to_show):
		pub_date = feed['entries'][i].updated_parsed
		published.append( datetime.date(pub_date[0], pub_date[1], pub_date[2] ) )
		apnd_title = feed['entries'][i].title
		title.append(apnd_title)
		apnd_summary = feed['entries'][i].summary
		apnd_summary = apnd_summary
		summary.append(apnd_summary)

		link.append(feed['entries'][i].link)
		'''posts.append({
			'title': feed['entries'][i].title,
			'summary': feed['entries'][i].summary,
			'link': feed['entries'][i].link,
			'date': published
			}) '''

	return 0
#@render_to('blog:index.html')
def feed(request):
	pull_feed('http://www.thehindu.com/news/national/andhra-pradesh/?service=rss', 3)
	pull_feed('http://www.thehindu.com/news/cities/Hyderabad/?service=rss', 3)
	# pull sports feed
	pull_feed('http://sports.espn.go.com/espn/rss/news',4)
	return render(request, 'blog/index.html', {'title': title, 'summary': summary, 'link': link})
	'''
	title1 = posts[0]['title']
	summary1 = posts[0]['summary']
	link1 = posts[0]['link']
	#date1 = posts[0]['date']
	title2 = posts[1]['title']
	summary2 = posts[1]['summary']
	link2 = posts[1]['link']
	
	title3 = posts[2]['title']
	summary3 = posts[2]['summary']
	link3 = posts[2]['link']
	
	title4 = posts[3]['title']
	summary4 = posts[3]['summary']
	link4 = posts[3]['link']
	
	title5 = posts[4]['title']
	summary5 = posts[4]['summary']
	link5 = posts[4]['link']

	title6 = posts[5]['title']
	summary6 = posts[5]['summary']
	link6 = posts[5]['link']

	return render(request, 'blog/index.html', {'title1': title1, 'summary1': summary1, 'link1':link1, 
											   'title2': title2, 'summary2': summary2, 'link2':link2,
											   'title3': title3, 'summary3': summary3, 'link3':link3,
											   'title4': title4, 'summary4': summary4, 'link4':link4,
											   'title5': title5, 'summary5': summary5, 'link5':link5,
											   'title6': title6, 'summary6': summary6, 'link6':link6
											  })
    '''









