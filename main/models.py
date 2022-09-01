from django.db import models

class Template(models.Model):

    ONBOARDING = "onboarding"
    OFFBOARDING = "offboarding"
    TEMPLATE_TYPE = [
        (ONBOARDING, "Onboarding"),
        (OFFBOARDING, "Offboarding"),
    ]
    name = models.CharField(max_length=25)
    type = models.CharField(
        max_length=25,
        choices=TEMPLATE_TYPE,
        default=ONBOARDING,
    )

    def __str__(self):
        return self.name

# Template Items
class Items(models.Model):
    HR = "HR"
    IT = "IT"
    TASK_TYPE = [
        (HR, 'HR'),
        (IT, "IT"),
    ]
    template_id = models.ForeignKey(Template, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    task_type = models.CharField(
        max_length=2,
        choices=TASK_TYPE,
        default=HR,
    )

    def __str__(self):
        return self.task

class Checklist(models.Model):
    ONBOARDING = "onboarding"
    OFFBOARDING = "offboarding"
    TEMPLATE_TYPE = [
        (ONBOARDING, "Onboarding"),
        (OFFBOARDING, "Offboarding"),
    ]
    template_name = models.CharField(max_length=25)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    date = models.DateField()
    notes = models.CharField(max_length=500, default="N/A")
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    type = models.CharField(
        max_length=25,
        choices=TEMPLATE_TYPE,
        default=ONBOARDING,
    )

    def __str__(self):
        return self.fname + " " + self.lname


class Item(models.Model):
    HR = "HR"
    IT = "IT"
    TASK_TYPE = [
        (HR, 'HR'),
        (IT, "IT"),
    ]

    checklist_id = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    task_type = models.CharField(
        max_length=2,
        choices=TASK_TYPE,
        default=HR,
    )
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
    
