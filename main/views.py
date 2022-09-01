from django.shortcuts import redirect, render
from .models import Checklist, Template, Items, Item
from django.views.decorators.http import require_POST

# Main page view
def index(request):
    incomplete = Checklist.objects.order_by("date").filter(complete=False)
    onTemplates = Template.objects.filter(type="onboarding")
    offTemplates = Template.objects.filter(type="offboarding")

    context = {'incomplete' : incomplete, 'onTemplates' : onTemplates, 'offTemplates' : offTemplates, 'complete' : complete,}
    return render(request, 'main/index.html', context)

def complete(request):
    complete = Checklist.objects.order_by("date").filter(complete=True)

    context = {'complete' : complete}
    return render(request, 'main/complete.html', context)

def completeChecklist(request, checklist_id):

    checklist = Checklist.objects.get(id=checklist_id)
    checklist.complete = True
    checklist.save()

    return redirect('index')

def incompleteChecklist(request, checklist_id):

    checklist = Checklist.objects.get(id=checklist_id)
    checklist.complete = False
    checklist.save()

    return redirect('complete')

# Checklist form add view
@require_POST
def addChecklist(request):
    checklist = Checklist.objects.order_by("id")
    item = Item.objects.order_by("checklist_id")

    if request.method == "POST":
        # This is the beginning of the actions that take place when the form is submitted on the home page
        if request.POST.get("submit"):
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            template = request.POST.get("template")
            date = request.POST.get("date")
            notes = request.POST.get("notes")
            template = Template.objects.get(name=template)
            # I am not sure if this will work or not, but I am hoping it will
            if template.type == 'onboarding':
                type = 'Onboarding'
            else:
                type = 'Offboarding'
            items = Items.objects.filter(template_id=template.id)
            # Add the type to here
            checklist.create(template_name=template, fname=fname, lname=lname, date=date, notes=notes, complete=False, type=type)
            new_checklist = Checklist.objects.latest("date_created")
            for i in items:
                item.create(checklist_id=new_checklist ,task=i, task_type=i.task_type)

    return redirect('index')

# Checklist page view
def checklist(request, checklist):
    checklist = Checklist.objects.get(id=checklist)
    items = Item.objects.filter(checklist_id=checklist)

    context = {'checklist' : checklist, "items": items}
    return render(request, 'main/checklist.html', context)

def checklistForm(request, checklist):
    checklist = Checklist.objects.get(id=checklist)
    items = Item.objects.filter(checklist_id=checklist)

    if request.method == "POST":
        if request.POST.get("save"):
            print(request.POST)
            for item in items:
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
                checklist.notes = request.POST.get("notes")
                checklist.save()

        elif request.POST.get("addItemHR"):
            text = request.POST.get("HRText")
            if len(text) > 3:
                checklist.item_set.create(checklist_id=checklist, task=text, task_type="HR")
        elif request.POST.get("addItemIT"):
            text = request.POST.get("ITText")
            if len(text) > 3:
                checklist.item_set.create(checklist_id=checklist, task=text, task_type="IT")

    return redirect('checklist', checklist.id)


# Template page and views

def template(request):
    onTemplates = Template.objects.filter(type='onboarding')
    offTemplates = Template.objects.filter(type='offboarding')
    context = {'onTemplates' : onTemplates, 'offTemplates' : offTemplates,}
    return render(request, 'main/template.html', context)

@require_POST
def addTemplate(request):
    template = Template.objects.order_by('id')
    print(request.POST)

    if request.method == "POST":
        if request.POST.get("submit"):
            name = request.POST.get("name")
            type = request.POST.get("template-type")
            type = type.lower()
            template.create(name=name, type=type)

    return redirect('template')  

def template_page(request, template):
    template = Template.objects.get(id=template)
    items = Items.objects.filter(template_id=template)

    context = {'template' : template, 'items' : items}
    return render(request, 'main/template_page.html', context)

def deleteTemplate(request, template_id):
    template = Template.objects.get(id=template_id)
    template.delete()
    
    return redirect('template')

def templateForm(request, template):
    template = Template.objects.get(id=template)
    items = Items.objects.filter(template_id=template)

    if request.POST.get("addItemHR"):
        text = request.POST.get("HRText")
        if len(text) > 3:
            items.create(template_id=template, task=text, task_type="HR")
    elif request.POST.get("addItemIT"):
        text = request.POST.get("ITText")
        if len(text) > 3:
            items.create(template_id=template, task=text, task_type="IT")

    return redirect('template', template.id)

def deleteTemplateItem(request, item_id, template_id):
    item = Items.objects.filter(id=item_id)
    item.delete()

    return redirect('template', template_id)