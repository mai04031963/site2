from django.http import HttpResponse


def index(request):
    return HttpResponse('Здравствуйте! Приветствуем вас на новом сайте ООО "Бозон"!')
