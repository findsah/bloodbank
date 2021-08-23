from django.contrib import admin
from donor.models import Donor, BloodDonate
from blood.models import BloodRequest, Stock
from patient.models import Patient

# Register your models here.
@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = Donor


@admin.register(BloodDonate)
class BloodAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = BloodDonate

@admin.register(BloodRequest)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = BloodRequest
@admin.register(Stock)
class StocksAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = Stock
@admin.register(Patient)
class PateintAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = Patient

