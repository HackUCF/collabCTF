from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'collabCTF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'collabCTF.views.home'),
    url(r'^reports$', 'collabCTF.views.reports'),
    url(r'^ctftools$', 'collabCTF.views.ctftools'),
    url(r'^ctfoverview$', 'collabCTF.views.ctfoverview'),
    url(r'^ctfchallenge$', 'collabCTF.views.ctfchallenge'),
    url(r'^ctf/(?P<ctf_slug>[\w\d_\-]+)/', 'competition.views.view_ctf')
)
