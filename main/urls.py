from django.urls import path

from . import views

urlpatterns = [
    # Pages
    path('', views.index, name='index'),
    path('template/', views.template, name='template'),
    path('template/<int:template>/', views.template_page, name='template'),
    path('complete/', views.complete, name='complete'),
    path('<int:checklist>/', views.checklist, name='checklist'),

    # Actions for those pages
    path('addChecklist', views.addChecklist, name='addChecklist'),
    path('checklistForm/<checklist>', views.checklistForm, name='checklistForm'),
    path('completeChecklist/<checklist_id>', views.completeChecklist, name='completeChecklist'),
    path('incompleteChecklist/<checklist_id>', views.incompleteChecklist, name='incompleteChecklist'),
    path('addTemplate', views.addTemplate, name='addTemplate'),
    path('deleteTemplate/<template_id>', views.deleteTemplate, name='deleteTemplate'),
    path('templateForm/<template>', views.templateForm, name='templateForm'),
    path('deleteTemplateItem/<item_id>/<template_id>', views.deleteTemplateItem, name='deleteTemplateItem'),
]