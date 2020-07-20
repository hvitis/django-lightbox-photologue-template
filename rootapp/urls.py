""" Extending URLS using include

For example, we include the "base" app's urls so we can create a homepage view with
the base app, but if you want you can do something like:

    path('base/', include(base.urls)),

This would mean the homepage url pattern would now live at, yoursite.com/base/
and the alternate bootstrap template would live at yoursite.com/base/bootstrap/

"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')), # Include url structure at root or base of site
]
