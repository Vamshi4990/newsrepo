from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')
def movies_info(request):
    head_msg = 'Movies information'
    sub_msg1 = 'Tillu movie was nice....'
    sub_msg2 = 'OG will coming soon.....'
    sub_msg3 = 'planning for ashiq-3 with prabhas & sunnyleone...'
    type = 'movies'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_info(request):
    head_msg = 'Sports information'
    sub_msg1 = 'Yesterday mumbai won with 6 wickets'
    sub_msg2 = 'Today chennai vs lsg match'
    sub_msg3 = 'kabaddi matches are starts soon'
    type = 'sports'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def political_info(request):
    head_msg = 'political information'
    sub_msg1 = 'telangana cm revanth reddy'
    sub_msg2 = 'upcoming cm for AP ???'
    sub_msg3 = 'try to partcipate in elections'
    type = 'political'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
