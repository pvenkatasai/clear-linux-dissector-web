# Clear Linux Dissector - view definitions
#
# Copyright (C) 2018-2019 Intel Corporation
#
# Licensed under the MIT license, see COPYING.MIT for details

import os
import sys
from datetime import datetime
from itertools import islice

import reversion
from django import forms
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission, User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.models import Site
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import resolve, reverse, reverse_lazy
from django.db import transaction
from django.db.models import Count, Q
from django.db.models.functions import Lower
from django.db.models.query import QuerySet
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from pkg_resources import parse_version

import settings
from dissector.forms import (ImageComparisonCreateForm,
                              ImageComparisonRecipeForm, LocalBuildDiffForm,
                              VersionComparisonForm, ComparisonImportForm)
from dissector.models import (ImageComparison, ImageComparisonRecipe,
                               VersionComparison, VersionComparisonDifference,
                               VersionComparisonFileDiff)
from layerindex.models import (Branch, LayerItem, LayerBranch, ClassicRecipe,
                              Source, Patch, Update)
from layerindex.views import (ClassicRecipeSearchView, ClassicRecipeDetailView,
                              ClassicRecipeLinkWrapper)

from layerindex import tasks, utils

# Create your views here.


class diff_home_view(TemplateView):
    def get_context_data(self, *args, **kwargs):
        #Builds=os.listdir('/tools/release/apl/master/gp2.0')
        context = super(diff_home_view, self).get_context_data(*args, **kwargs)
        #context['message'] = 'Local Native Daily Builds'
        #context['Builds'] = Builds
        return context

class DiffViewNew(TemplateView):
    def get_context_data(self, *args, **kwargs):
        #Builds=os.listdir('/tools/release/apl/master/gp2.0')
        context = super(DiffViewNew, self).get_context_data(*args, **kwargs)
        Builds=os.listdir('/tools/release/apl/master/gp2.0/sos-mr1')
        context['message'] = 'Local SOS-MR1 Native Daily Builds'
        context['Builds'] = Builds
        #context['message'] = 'Local Native Daily Builds'
        #context['Builds'] = Builds
        return context