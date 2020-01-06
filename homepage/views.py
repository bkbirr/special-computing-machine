from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


    #def home(request):
     #   return render(request,"homepage/minipo/index-5.html")

