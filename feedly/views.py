#!/usr/bin/python
#
# This file is part of django-feedly project.
#
# Copyright (C) 2011-2020 William Oliveira de Lagos <william.lagos@icloud.com>
#
# Feedly is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Feedly is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Feedly. If not, see <http://www.gnu.org/licenses/>.
#

import logging, urllib.parse

from django.http import HttpResponse as response
from django.http import JsonResponse
from django.views import View

from .feed import Mosaic,Pages
from .core import Feedly

logger = logging.getLogger("feedly.views")

class BlocksView(View):

    def get(self, request):
        return JsonResponse({'blocks': 'success'})

    def profileview(self, request,name='me'):
        e = Feedly()
        if request.method == 'GET':
            return e.profile_view(request,name)

    def pageview(self, request):
        p = Pages()
        if request.method == 'GET':
            return p.page_view(request)
        
    def pageedit(self, request):
        p = Pages()
        if request.method == 'GET':
            return p.edit_page(request)
        elif request.method == 'POST':
            return p.save_page(request)

    def page(self, request):
        p = Pages()
        if request.method == 'GET':
            return p.view_page(request)
        elif request.method == 'POST':
            return p.create_page(request)

    def mosaic(self, request):
        m = Mosaic()
        if request.method == 'GET':
            return m.view_mosaic(request)

    def deadlines(self, request):
        m = Mosaic()
        if request.method == 'GET':
            return m.deadlines(request)

    def main(self, request):
        e = Feedly()
        if request.method == 'GET':
            return e.start(request)
        elif request.method == 'POST':
            return e.external(request)