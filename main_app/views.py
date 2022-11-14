from django.shortcuts import render

hamsters = [
    {'name': 'Hamtaro', 'gender': 'male', 'birthday': 'August 6th', 'height': '8.6cm'},
    {'name': 'Bijou', 'gender': 'female', 'birthday': 'July 10th', 'height': '7.5cm'},
    {'name': 'Sparkle', 'gender': 'female', 'birthday': 'February 9th', 'height': 'Secret'},
    {'name': 'Oxnard', 'gender': 'male', 'birthday': 'May 3rd', 'height': '10cm'},
    {'name': 'Harmony', 'gender': 'female', 'birthday': 'April 5th', 'height': '8.6cm'},
    {'name': 'Boss', 'gender': 'male', 'birthday': 'September 21st', 'height': '12cm'},
    {'name': 'Broski', 'gender': 'male', 'birthday': 'February 18th', 'height': '8.5cm'},
    {'name': 'Cappy', 'gender': 'male', 'birthday': 'August 16th', 'height': '7.7cm'},
    {'name': 'Jingle', 'gender': 'male', 'birthday': 'December 12th', 'height': '8.5cm'},
    {'name': 'Dexter', 'gender': 'male', 'birthday': 'October 11th', 'height': '8.7cm'},
    {'name': 'Maxwell', 'gender': 'male', 'birthday': 'November 5th', 'height': '10.5cm'},
    {'name': 'Pashmina', 'gender': 'female', 'birthday': 'September 16th', 'height': '7.3cm'},
    {'name': 'Penelope', 'gender': 'female', 'birthday': 'March 3rd', 'height': '6.2cm'},
    {'name': 'Snoozer', 'gender': 'male', 'birthday': 'January 14th', 'height': '8.5cm'},
    {'name': 'Panda', 'gender': 'male', 'birthday': 'April 18th', 'height': '8.8cm'},
    {'name': 'Sandy', 'gender': 'female', 'birthday': 'June 6th', 'height': '7.5cm'},
    {'name': 'Stan', 'gender': 'male', 'birthday': 'June 6th', 'height': '7.5cm'},
    {'name': 'Howdy', 'gender': 'male', 'birthday': 'February 18th', 'height': '8.5cm'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def hamster_index(request):
    return render(request, 'hamsters/index.html', {
        'hamsters': hamsters
    })
