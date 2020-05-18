from django.shortcuts import render
from .models import Event, News, Gallary

# Create your views here.

def index(request):

    # event data starts here
    event_dates = Event.objects.all()[::-1][:5]
    data = {}
    month = {'01' : 'JAN', '02' : 'FEB' , '03' : 'MAR', '04' : 'APR', '05' : 'MAY' , '06' : 'JUN', '07' : 'JUL',
            '08' : 'AUG', '09' : 'SEP', '10' : 'OCT', '11' : 'NOV', '12' : 'DEC'}
    
    # print(event_dates)
    dates = []
    for date in event_dates:
        current_date = str(date.event_date)
        current_venue = date.venue
        start_time = date.start
        end_time = date.end

        # print(type(current_date))
        res = current_date.split('-')
        # print(res)
        # data['year'] = res[0]
        data['month'] = month[res[1]]
        data['date'] = res[2]
        data['venue'] = current_venue
        data['start'] = start_time
        data['end'] = end_time
        data['event'] = date.event_name
        dates.append(data)
        data = {}
        # print(date.event_date.split('-'))
        # print(dates)
    
    # event data ends here

    # news data starts here
    news_data = {}
    result_news = []

    news = News.objects.all()

    for data in news:
        news_data['title'] = data.title
        news_data['description'] = data.description
        news_data['detail'] = data.detail
        # print(data.title,data.description,data.detail)
        result_news.append(news_data)
        news_data = {}

    # print(result_news)

    return render(request,'index.html',{'dates' : dates, 'result_news' : result_news})


def gallery(request):
    images = Gallary.objects.all()
    for i in images:
        print(i)
    return render(request,'gallery.html',{'images' : images})

def allevent(request):
    event_dates = Event.objects.all()[::-1]
    data = {}
    month = {'01' : 'JAN', '02' : 'FEB' , '03' : 'MAR', '04' : 'APR', '05' : 'MAY' , '06' : 'JUN', '07' : 'JUL',
            '08' : 'AUG', '09' : 'SEP', '10' : 'OCT', '11' : 'NOV', '12' : 'DEC'}
    
    # print(event_dates)
    dates = []
    for date in event_dates:
        current_date = str(date.event_date)
        current_venue = date.venue
        start_time = date.start
        end_time = date.end

        # print(type(current_date))
        res = current_date.split('-')
        # print(res)
        # data['year'] = res[0]
        data['month'] = month[res[1]]
        data['date'] = res[2]
        data['venue'] = current_venue
        data['start'] = start_time
        data['end'] = end_time
        data['event'] = date.event_name
        dates.append(data)
        data = {}
    # print(dates)
    return render(request,'allEvent.html',{'dates' : dates})


