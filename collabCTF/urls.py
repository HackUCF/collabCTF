from django.conf.urls import patterns, include, url, static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'collabCTF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'collabCTF.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^settings$', 'collabCTF.views.settings', name='settings'),
    url(r'^profile$', 'collabCTF.views.profile', name='profile'),
    url(r'^about$', 'collabCTF.views.about', name='about'),
    url(r'^login$', 'collabCTF.views.log_in', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': "/login"}, name='logout'),
    url(r'^register$', 'collabCTF.views.register', name='register'),
    url(r'^.sidebar$', 'collabCTF.views.sidebar', name='sidebar'),
    url(r'^reports$', 'collabCTF.views.reports', name='reports'),
    url(r'^ctftools$', 'collabCTF.views.ctf_tools', name='ctf_tools'),
    url(r'^about$', 'collabCTF.views.about'),
    url(r'^profile', 'collabCTF.views.profile'),
    url(r'^settings', 'collabCTF.views.settings'),
    url(r'^ctf/add$', 'competition.views.add_ctf', name='add_ctf'),
    url(r'^ctf/(?P<ctf_slug>[a-z\d_\-]+)/$', 'competition.views.view_ctf', name='view_ctf'),
    url(r'^ctf/(?P<ctf_slug>[a-z\d_\-]+)/update$', 'competition.views.update_ctf', name='update_ctf'),
    url(r'^ctf/(?P<ctf_slug>[a-z\d_\-]+)/delete$', 'competition.views.delete_ctf', name='delete_ctf'),
    url(r'^ctf/(?P<ctf_slug>[a-z\d_\-]+)/add$', 'competition.views.add_challenge', name='add_challenge'),
    url(r'^ctf/(?P<ctf_slug>[a-z\d_\-]+)/(?P<chall_slug>[a-z\d_\-]+)/$', 'competition.views.view_challenge',
        name='view_challenge'),
    url(r'^ctf/(?P<ctf_slug>[a-z\d_\-]+)/(?P<chall_slug>[a-z\d_\-]+)/update$', 'competition.views.update_challenge',
        name='update_challenge'),
    url(r'^ctf/(?P<ctf_slug>[a-z\d_\-]+)/(?P<chall_slug>[a-z\d_\-]+)/delete$', 'competition.views.delete_challenge',
        name='delete_challenge'),
    url(r'ctf/(?P<ctf_slug>[a-z\d_\-]+)/(?P<chall_slug>[a-z\d_\-]+)/add', 'competition.views.add_file',
        name='add_file'),

    # ajax
    url(r'^ctf/(?P<ctf_slug>[a-z\d_\-]+)/.chart$', 'competition.ajax.chart_data', name='ctf_chart'),
    url(r'^tools/.hash$', 'collabCTF.views.hash_val', name='tools_hash'),
    url(r'^tools/.rot$', 'collabCTF.views.rot_val', name='tools_rot'),
    url(r'^tools/.base_conversions$', 'collabCTF.views.base_conversion_val', name='tools_base_conversion'),
    url(r'^tools/.xor$', 'collabCTF.views.xor_val', name='tools_xor'),
)

if settings.DEBUG:
    if 'MEDIA_ROOT' in dir(settings):
        media_root = settings.MEDIA_ROOT
    else:
        media_root = 'files'
    urlpatterns += static.static(settings.MEDIA_URL, document_root=media_root)
