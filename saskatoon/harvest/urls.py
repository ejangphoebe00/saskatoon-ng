from django.urls import include, path, re_path
from rest_framework import routers
from django.views.generic import TemplateView
from . import api, views, autocomplete

# REST FRAMEWORK VIEWS
router = routers.DefaultRouter()
router.register('harvest', api.HarvestViewset, 'harvest')
router.register('property', api.PropertyViewset, 'property')
router.register('equipment', api.EquipmentViewset, 'equipment')
router.register('beneficiary', api.BeneficiaryViewset, 'beneficiary')
router.register('community', api.CommunityViewset, 'community')
router.register('participation', api.RequestForParticipationViewset, 'participation')

urlpatterns = [
    # CREATE VIEWS
    path(r'equipment/create/',
         views.EquipmentCreateView.as_view(),
         name='equipment-create'),

    path(r'property/create/',
         views.PropertyCreateView.as_view(),
         name='property-create'),

    path(r'property/create_public/',
         views.PropertyCreatePublicView.as_view(),
         name='property-create-public'),

    path(r'harvest/create/',
         views.HarvestCreateView.as_view(),
         name='harvest-create'),

    path(r'participation/create/',
         views.RequestForParticipationCreateView.as_view(),
         name='rfp-create'),

    path(r'comment/create/',
         views.CommentCreateView.as_view(),
         name='comment-create'),

    path(r'yield/create/',
         views.harvest_yield_create,
         name='harvest-yield-create'),


    # DELETE VIEWS
    path(r'yield/delete/<int:id>/',
         views.harvest_yield_delete,
         name='harvest-yield-delete'),


    # UPDATE VIEWS
    re_path(r'^property/update/(?P<pk>\d+)/$',
            views.PropertyUpdateView.as_view(),
            name='property-update'),
    re_path(r'^participation/update/(?P<pk>\d+)/$',
            views.RequestForParticipationUpdateView.as_view(),
            name='participation-update'),
    re_path(r'^harvest/update/(?P<pk>\d+)/$',
            views.HarvestUpdateView.as_view(),
            name='harvest-update'),
    re_path(r'^equipment/update/(?P<pk>\d+)/$',
            views.EquipmentUpdateView.as_view(),
            name='equipment-update'),


    # AUTO-COMPLETE VIEWS
    re_path(r'^property-autocomplete/$',
            autocomplete.PropertyAutocomplete.as_view(),
            name='property-autocomplete'),

    re_path(r'^tree-autocomplete/$',
            autocomplete.TreeAutocomplete.as_view(),
            name='tree-autocomplete'),


    # MISC
    path(r'property/thanks/',
         views.TemplateView.as_view(template_name='app/property_thanks.html'),
         name='property-thanks'),

    path(r'stats/',
         views.TemplateView.as_view(template_name='app/stats.html'),
         name='statistics'),

]

urlpatterns += router.urls
