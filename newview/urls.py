
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView, TemplateView
from newview.views import diff_home_view, DiffViewNew

urlpatterns = [
    # url(r'^$', TemplateView.as_view(
    #     template_name='newview/Home.html'),
    #     name='HomePage'),
    url(r'^$',
        diff_home_view.as_view(
        template_name='newview/Home1.html'),
        name="HomePage"),
    url(r'^diffview/$', TemplateView.as_view(
        template_name='newview/index2.html'),
        name='diff_view'),
    url(r'^diff_view_new/$', DiffViewNew.as_view(
        template_name='newview/index2.html'),
        name='diff_view_new'),
    #url(r'^diff_view/$',
    #    ImageCompareView.as_view(
    #        template_name='dissector/imagecompare.html'),
    #    name="image_comparison"),
]
