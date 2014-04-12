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
    url(r'^ctftools$', 'collabCTF.views.ctf_tools'),
    url(r'^ctfoverview$', 'collabCTF.views.ctfoverview'),
    url(r'^ctfchallenge$', 'collabCTF.views.ctfchallenge'),
    url(r'^about', 'collabCTF.views.about'),
    url(r'^addctfchallenge', 'collabCTF.views.addctfchallenge'),
    url(r'^addctfoverview', 'collabCTF.views.addctfoverview'),
    url(r'^profile', 'collabCTF.views.profile'),
    url(r'^settings', 'collabCTF.views.settings'),
    url(r'^ctf/(?P<ctf_slug>[a-z\d_\-]+)/', 'competition.views.view_ctf'),
    url(r'^tools/ajax/hash$', 'collabCTF.views.hash_val', name='tools_hash'),
    url(r'^tools/ajax/rot$', 'collabCTF.views.rot_val', name='tools_rot')
)
