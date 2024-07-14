from django.contrib import admin
from watchmate.models import Review, StreamPlatform, WatchList

admin.site.register(StreamPlatform)
admin.site.register(WatchList)
admin.site.register(Review)
