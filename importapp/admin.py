from django.contrib import admin
from .models import (Xabar, Hamkor, Product_category_1, Product_category_2, Product, Contact, AboutUs, Work, Employee,
                     Exsport, Import, CustomsClearance, Outsourcing,
                     New, PressCenter_1, PressCenter_2, AppealOfLegal, Corruption, CompanyDetails, Image, PhotoGallery,
                     VideoGallery, Telegram, Product_image, StatsImportExport)
from modeltranslation.admin import TranslationAdmin


class XabarAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Email', 'Date', 'Checked')
    ordering = ('-User',)
    search_fields = ( 'User', 'Email')

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


class StatsImportExportAdmin(admin.ModelAdmin):
    list_filter = ('type', 'product', 'date')

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