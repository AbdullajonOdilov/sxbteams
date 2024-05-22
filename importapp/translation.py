from modeltranslation.translator import translator, TranslationOptions
from .models import (Product_category_1, Product_category_2, Product, AboutUs, Work, Employee, Exsport, Import, CustomsClearance, Outsourcing,
    New, PressCenter_1, PressCenter_2, Corruption, CompanyDetails)



class Product_category_1TranslationOptions(TranslationOptions):
    fields = ('Name',)

translator.register(Product_category_1, Product_category_1TranslationOptions)


class Product_category_2TranslationOptions(TranslationOptions):
    fields = ('Name',)

translator.register(Product_category_2, Product_category_2TranslationOptions)


class ProductTranslationOptions(TranslationOptions):
    fields = ('Name', 'Information')

translator.register(Product, ProductTranslationOptions)


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('Name', 'Information')

translator.register(AboutUs, AboutUsTranslationOptions)


class WorkTranslationOptions(TranslationOptions):
    fields = ('Information',)

translator.register(Work, WorkTranslationOptions)


class EmployeeTranslationOptions(TranslationOptions):
    fields = ('Name', 'Position')

translator.register(Employee, EmployeeTranslationOptions)


class ExsportTranslationOptions(TranslationOptions):
    fields = ('Information',)

translator.register(Exsport, ExsportTranslationOptions)


class ImportTranslationOptions(TranslationOptions):
    fields = ('Information',)

translator.register(Import, ImportTranslationOptions)


class CustomsClearanceTranslationOptions(TranslationOptions):
    fields = ('Information',)

translator.register(CustomsClearance, CustomsClearanceTranslationOptions)


class OutsourcingTranslationOptions(TranslationOptions):
    fields = ('Information',)

translator.register(Outsourcing, OutsourcingTranslationOptions)


class NewTranslationOptions(TranslationOptions):
    fields = ('Name', 'Information')

translator.register(New, NewTranslationOptions)


class PressCenter_1TranslationOptions(TranslationOptions):
    fields = ('Name', 'Information')

translator.register(PressCenter_1, PressCenter_1TranslationOptions)


class PressCenter_2TranslationOptions(TranslationOptions):
    fields = ('Name', 'Information')

translator.register(PressCenter_2, PressCenter_2TranslationOptions)


class CorruptionTranslationOptions(TranslationOptions):
    fields = ('Name', 'Information')

translator.register(Corruption, CorruptionTranslationOptions)


class CompanyDetailsTranslationOptions(TranslationOptions):
    fields = ('Location',)

translator.register(CompanyDetails, CompanyDetailsTranslationOptions)
