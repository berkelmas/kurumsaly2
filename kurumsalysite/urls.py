from django.urls import path
from .views import index, about, services, process, faq, contact, articledetay, articles, muvekkil

from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name="index"),
    path('hakkimizda/', about, name="about"),
    path('hizmetlerimiz/', services, name="services"),
    path('surec/', process, name="process"),
    path('sorular/', faq, name="faq"),
    path('iletisim/', contact, name="contact"),
    path('makaledetay/<slug:makaleslug>', articledetay, name="articledetail"),
    path('makaleler/', articles, name="articles"),
    path('muvekkil/', muvekkil, name="muvekkil"),
    path('sitemap.xml/', TemplateView.as_view(template_name='kurumsalysite/sitemap.xml', content_type='text/plain'), name="sitemap" ),
    path('robots.txt/', TemplateView.as_view(template_name='kurumsalysite/robots.txt', content_type='text/plain'))
]