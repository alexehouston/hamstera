from django.shortcuts import render
from .models import Hamster

hamsters = [
    {'name': 'Hamtaro ハム太郎', 'gender': 'male', 'birthday': 'August 6th', 'height': '8.6cm'},
    {'name': 'Bijou リボンちゃん', 'gender': 'female', 'birthday': 'July 10th', 'height': '7.5cm'},
    {'name': 'Sparkle くるりんちゃん', 'gender': 'female', 'birthday': 'February 9th', 'height': 'Secret'},
    {'name': 'Oxnard こうしくん', 'gender': 'male', 'birthday': 'May 3rd', 'height': '10cm'},
    {'name': 'Harmony エンジェルちゃん', 'gender': 'female', 'birthday': 'April 5th', 'height': '8.6cm'},
    {'name': 'Boss タイショーくん', 'gender': 'male', 'birthday': 'September 21st', 'height': '12cm'},
    {'name': 'Broski サーファーくん', 'gender': 'male', 'birthday': 'February 18th', 'height': '8.5cm'},
    {'name': 'Cappy かぶるくん', 'gender': 'male', 'birthday': 'August 16th', 'height': '7.7cm'},
    {'name': 'Jingle トンガリくん', 'gender': 'male', 'birthday': 'December 12th', 'height': '8.5cm'},
    {'name': 'Dexter めがねくん', 'gender': 'male', 'birthday': 'October 11th', 'height': '8.7cm'},
    {'name': 'Maxwell のっぽくん', 'gender': 'male', 'birthday': 'November 5th', 'height': '10.5cm'},
    {'name': 'Pashmina マフラーちゃん', 'gender': 'female', 'birthday': 'September 16th', 'height': '7.3cm'},
    {'name': 'Penelope ちび丸ちゃん', 'gender': 'female', 'birthday': 'March 3rd', 'height': '6.2cm'},
    {'name': 'Snoozer ねてるくん', 'gender': 'male', 'birthday': 'January 14th', 'height': '8.5cm'},
    {'name': 'Panda パンダくん', 'gender': 'male', 'birthday': 'April 18th', 'height': '8.8cm'},
    {'name': 'Sandy トラハムちゃん', 'gender': 'female', 'birthday': 'June 6th', 'height': '7.5cm'},
    {'name': 'Stan トラハムくん', 'gender': 'male', 'birthday': 'June 6th', 'height': '7.5cm'},
    {'name': 'Howdy まいどくん', 'gender': 'male', 'birthday': 'February 18th', 'height': '8.5cm'},
    {'name': 'Lapis ラピスちゃん', 'gender': 'female', 'birthday': 'July 9th', 'height': '8.5cm'},
    {'name': 'Lazuli ラズリーちゃん', 'gender': 'female', 'birthday': 'September 7th', 'height': 'Secret'},
    {'name': 'Pepper じゃじゃハムちゃん', 'gender': 'female', 'birthday': 'January 1st', 'height': 'Secret'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def hamster_index(request):
    return render(request, 'hamsters/index.html', {'hamsters': hamsters})

def hamsters_detail(request, hamster_id):
    hamster = Hamster.objects.get(id=hamster_id)
    return render(request, 'hamsters/detail.html', {'hamster': hamster})
