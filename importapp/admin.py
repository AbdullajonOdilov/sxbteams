from django.contrib import admin
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


from .models import (Xabar, Hamkor, Product_category_1, Product_category_2, Product, Contact, AboutUs, Work, Employee,
                     Exsport, Import, CustomsClearance, Outsourcing,
                     New, PressCenter_1, PressCenter_2, AppealOfLegal, Corruption, CompanyDetails, Image, PhotoGallery,
                     VideoGallery, Telegram, Product_image, StatsImportExport)
from modeltranslation.admin import TranslationAdmin



class XabarAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Email', 'Date', 'Checked')
    ordering = ('-User',)
    search_fields = ('User', 'Email')

admin.site.register(Xabar, XabarAdmin)


class HamkorAdmin(admin.ModelAdmin):
    list_display = ('id', 'Image', 'Date')
    ordering = ('-id',)
    search_fields = ('id', 'Date')

admin.site.register(Hamkor, HamkorAdmin)


class Product_category_1Admin(TranslationAdmin):
    list_display = ('id', 'Name', 'Type_of_product', 'Date')
    ordering = ('-Type_of_product',)
    search_fields = ('Name', 'Date', 'Type_of_product')

admin.site.register(Product_category_1, Product_category_1Admin)


class Product_category_2Admin(TranslationAdmin):
    list_display = ('id', 'Name', 'Type_1', 'Date')
    search_fields = ('Name', 'Date')


admin.site.register(Product_category_2, Product_category_2Admin)


class ProductAdmin(TranslationAdmin):
    list_display = ['id', 'Name', 'Type_2', 'display_images', 'Date']
    ordering = ('-Name',)
    search_fields = ('Name', 'Date')

    def display_images(self, obj):
        return ", ".join([image.Image.url for image in obj.Images.all()])

    display_images.short_description = 'Images'

admin.site.register(Product, ProductAdmin)

class Product_imageAdmin(TranslationAdmin):
    list_display = ('id', 'Date', 'Image')
    ordering = ('-Date',)

admin.site.register(Product_image, Product_imageAdmin)


class DateRangeFilter(SimpleListFilter):
    title = _('Date Range')
    parameter_name = 'date_range'

    def lookups(self, request, model_admin):
        return (
            ('today', _('Today')),
            ('this_week', _('This week')),
            ('this_month', _('This month')),
            ('this_year', _('This year')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'today':
            return queryset.filter(date=date.today())
        elif self.value() == 'this_week':
            start_date = date.today() - timedelta(days=date.today().weekday())
            end_date = start_date + timedelta(days=6)
            return queryset.filter(date__range=[start_date, end_date])
        elif self.value() == 'this_month':
            start_date = date.today().replace(day=1)
            end_date = start_date + relativedelta(months=1, days=-1)
            return queryset.filter(date__range=[start_date, end_date])
        elif self.value() == 'this_year':
            start_date = date.today().replace(month=1, day=1)
            end_date = start_date + relativedelta(years=1, days=-1)
            return queryset.filter(date__range=[start_date, end_date])


class StatsImportExportAdmin(admin.ModelAdmin):
    list_display = ('product', 'type', 'summa', 'organisation', 'date')
    list_filter = ('type', 'date',)
    search_fields = ('product__Name', 'organisation', 'comment')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Prefetch related 'product' for optimization if needed
        return qs.select_related('product')

    def total_summa_export(self, queryset):
        total_export_sum = queryset.filter(type='export').aggregate(total_sum=Sum('summa'))['total_sum']
        return total_export_sum if total_export_sum is not None else 0.0

    def total_summa_import(self, queryset):
        total_import_sum = queryset.filter(type='import').aggregate(total_sum=Sum('summa'))['total_sum']
        return total_import_sum if total_import_sum is not None else 0.0

    def total_summa_export_period(self, request, queryset, start_date, end_date):
        if start_date and end_date:
            total_export_sum_period = queryset.filter(type='export', date__range=[start_date, end_date]).aggregate(total_sum=Sum('summa'))['total_sum']
            return total_export_sum_period if total_export_sum_period is not None else 0.0
        else:
            return 0.0

    def total_summa_import_period(self, request, queryset, start_date, end_date):
        if start_date and end_date:
            total_import_sum_period = queryset.filter(type='import', date__range=[start_date, end_date]).aggregate(total_sum=Sum('summa'))['total_sum']
            return total_import_sum_period if total_import_sum_period is not None else 0.0
        else:
            return 0.0

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        queryset = self.get_queryset(request)

        # Get start_date and end_date from request GET parameters
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        # Calculate totals for the entire queryset
        extra_context['total_summa_export'] = self.total_summa_export(queryset)
        extra_context['total_summa_import'] = self.total_summa_import(queryset)

        # Calculate totals for the specified period if start_date and end_date are provided
        extra_context['total_summa_export_period'] = self.total_summa_export_period(request, queryset, start_date, end_date)
        extra_context['total_summa_import_period'] = self.total_summa_import_period(request, queryset, start_date, end_date)
        print(extra_context['total_summa_export_period'])
        print()
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(StatsImportExport, StatsImportExportAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Company', 'Connected', 'Date')
    ordering = ('-Name',)
    search_fields = ('Name', 'Company', 'Date')

admin.site.register(Contact, ContactAdmin)


class AboutUsAdmin(TranslationAdmin):
    list_display = ('id', 'Name', 'Date')
    ordering = ('-Name',)
    search_fields = ('Name', 'Date')

admin.site.register(AboutUs, AboutUsAdmin)


class WorkAdmin(TranslationAdmin):
    list_display = ('id', 'Position', 'Date')
    ordering = ('-id', '-Date',)
    search_fields = ('id', 'Date')

admin.site.register(Work, WorkAdmin)


class EmployeeAdmin(TranslationAdmin):
    list_display = ('id', 'Name', 'Email', 'Phone', 'Position', 'Date')
    ordering = ('-Name', '-Position', '-Date')
    search_fields = ('Name', 'Email', 'Phone', 'Date')

admin.site.register(Employee, EmployeeAdmin)


class ExsportAdmin(TranslationAdmin):
    list_display = ('id', 'Date')
    ordering = ('-id', '-Date')
    search_fields = ('id', 'Date')

admin.site.register(Exsport, ExsportAdmin)


class ImportAdmin(TranslationAdmin):
    list_display = ('id', 'Date')
    ordering = ('-id', '-Date')
    search_fields = ('id', 'Date')

admin.site.register(Import, ImportAdmin)


class CustomsClearanceAdmin(TranslationAdmin):
    list_display = ('id', 'Date')
    ordering = ('-id', '-Date')
    search_fields = ('id', 'Date')

admin.site.register(CustomsClearance, CustomsClearanceAdmin)


class OutsourcingAdmin(TranslationAdmin):
    list_display = ('id', 'Date')
    ordering = ('-id', '-Date')
    search_fields = ('id', 'Date')

admin.site.register(Outsourcing, OutsourcingAdmin)


class NewAdmin(TranslationAdmin):
    list_display = ('id', 'Name', 'Image', 'Video_file', 'Date')
    ordering = ('-Name', '-Date')
    search_fields = ('Name', 'Date')

admin.site.register(New, NewAdmin)


class PressCenter_1Admin(TranslationAdmin):
    list_display = ('id', 'Name', 'Image', 'Video_file', 'Date')
    ordering = ('-Name', '-Date')
    search_fields = ('Name', 'Date')

admin.site.register(PressCenter_1, PressCenter_1Admin)


class PressCenter_2Admin(TranslationAdmin):
    list_display = ('id', 'Name', 'Image', 'Video_file', 'Date')
    ordering = ('-Name', '-Date')
    search_fields = ('Name', 'Date')

admin.site.register(PressCenter_2, PressCenter_2Admin)

class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Date')
    ordering = ('-id', '-Date')
    search_fields = ('id', 'Date')

admin.site.register(PhotoGallery, PhotoGalleryAdmin)

class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Date')
    ordering = ('-id', '-Date')
    search_fields = ('id', 'Date')

admin.site.register(VideoGallery, VideoGalleryAdmin)


class AppealOfLegalAdmin(admin.ModelAdmin):
    list_display = ('id', 'Subject', 'FullName', 'Phone', 'SubjectType', 'Date')
    ordering = ('-FullName', '-Date', '-SubjectType')
    search_fields = ('FullName', 'Date')

admin.site.register(AppealOfLegal, AppealOfLegalAdmin)


class CorruptionAdmin(TranslationAdmin):
    list_display = ('id', 'Name', 'Date')
    ordering = ('-Name', '-Date')
    search_fields = ('Name', 'Date')

admin.site.register(Corruption, CorruptionAdmin)


class CompanyDetailsAdmin(TranslationAdmin):
    list_display = ('id', 'Location', 'Phone', 'Email', 'Date')
    ordering = ('-Email', '-Date')
    search_fields = ('Email', 'Location', 'Date')

admin.site.register(CompanyDetails, CompanyDetailsAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'Image', 'Date')
    ordering = ('-id', '-Date')
    search_fields = ('id', 'Date')

admin.site.register(Image, ImageAdmin)


class TelegramAdmin(admin.ModelAdmin):
    list_display = ('id', 'apiToken', 'chatID')
    ordering = ('-id', '-Date')
    search_fields = ('id', 'Date')

admin.site.register(Telegram, TelegramAdmin)