# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile, Thread, Idea, Tag, TB_UserIdea

# Register your models here.

admin.site.register(Profile)
admin.site.register(Thread)
admin.site.register(Idea)
admin.site.register(Tag)
admin.site.register(TB_UserIdea)
