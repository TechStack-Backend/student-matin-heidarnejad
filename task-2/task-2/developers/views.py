from django.http import Http404
from django.shortcuts import render

developers = [
    {
        "username": "hassan",
        "first_name": "Hassan",
        "last_name": "Kabittan",
        "skills": ["Python", "Django", "Vue.js"],
    },
    {
        "username": "sara",
        "first_name": "Sara",
        "last_name": "Ahmadi",
        "skills": ["JavaScript", "React", "CSS"],
    },
    {
        "username": "ali",
        "first_name": "Ali",
        "last_name": "Rezayi",
        "skills": ["Java", "Spring Boot", "SQL"],
    },
]


def developers_list(request):

    return render(request, "developers_list.html", {"developers": developers})

def developer_cv(request, username):

    dev = next((d for d in developers if d["username"] == username), None)
    if not dev:

        raise Http404("Developer not found")

    full_name = f'{dev["first_name"]} {dev["last_name"]}'
    ctx = {"dev": dev, "full_name": full_name}
    return render(request, "developer_cv.html", ctx)
from django.shortcuts import render


