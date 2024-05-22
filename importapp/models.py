from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField


class Xabar(models.Model):
    User = models.CharField(verbose_name="User", max_length=255)
    Email = models.EmailField(
        verbose_name="Email", max_length=255, blank=True, null=True)
    Message = models.TextField(verbose_name="Message")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    Checked = models.BooleanField(
        verbose_name="Has been answered", default=False)

    def __str__(self):
        return self.User

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'A - Xabarlar'
        ordering = ["-Checked"]


class Hamkor(models.Model):
    Image = models.ImageField(verbose_name="Image", upload_to="Hamkor")
    Urls = models.URLField(verbose_name="Hamkor url", max_length=200)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = 'Hamkor'
        verbose_name_plural = 'D - Hamkorlar'
        ordering = ["-Date"]


class Product_category_1(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    class product_choise(models.TextChoices):
        Import = 'I', _('Import')
        Export = 'E', _('Export')
    Type_of_product = models.CharField(
        verbose_name="Mahsulot turi", choices=product_choise.choices, default=product_choise.Export, max_length=2)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return f"{self.get_Type_of_product_display()} - {self.Name}"

    class Meta:
        verbose_name = '1-mahsulot kategoriyasi'
        verbose_name_plural = 'B - 1-mahsulot kategoriyalari(asosiy)'

class Product_category_2(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    Type_1 = models.ForeignKey(
        Product_category_1, verbose_name="Category", on_delete=models.CASCADE)
    Image = models.ImageField(verbose_name="Image", upload_to="product")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return f"{self.Type_1} - {self.Name}"

    class Meta:
        verbose_name = '2-mahsulot kategoriyasi'
        verbose_name_plural = 'B - 2-mahsulot kategoriyalari'


class Product(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    Type_2 = models.ForeignKey(
        Product_category_2, verbose_name="Category", on_delete=models.CASCADE)
    Image = models.ImageField(verbose_name="Image", upload_to="product")
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return f"{self.Type_2} - {self.Name}"

    class Meta:
        verbose_name = '3-mahsulot'
        verbose_name_plural = 'B - 3-mahsulot'


class Contact(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    Email = models.EmailField(
        verbose_name="Email", max_length=255, blank=True, null=True)
    Company = models.CharField(verbose_name="Company", max_length=255)
    Phone = PhoneField(blank=True, help_text='Contact phone number')
    Message = models.TextField(verbose_name="Message")
    Connected = models.BooleanField(
        verbose_name="Has been answered", default=False)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Aloqa'
        verbose_name_plural = 'A - Aloqalar'


class AboutUs(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Kompaniya haqida ma'lumot"
        verbose_name_plural = "A - Kompaniya haqida ma'lumotlar"


class Work(models.Model):
    Information = RichTextField(
        verbose_name="Information")
    Position = models.BooleanField(verbose_name="Active", default=False)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = "Ish vakansiyasi"
        verbose_name_plural = "A - Ish vakansiyalari"


class Employee(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    Email = models.EmailField(
        verbose_name="Email", max_length=255, blank=True, null=True)
    Image = models.ImageField(verbose_name="Image", upload_to="Employee")
    Phone = PhoneField(blank=True, help_text='Contact phone number')
    ReceptionDate = models.CharField(
        verbose_name="Reception date", max_length=255)
    Position = models.CharField(
        verbose_name="Employee position", max_length=255)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Xodim ma'lumotlari"
        verbose_name_plural = 'A - Xodimlar'


class Exsport(models.Model):
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = 'Exsport'
        verbose_name_plural = 'C - Exsport'


class Import(models.Model):
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = 'Import'
        verbose_name_plural = 'C - Import'


class CustomsClearance(models.Model):
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = 'Bojxona rasmiylashtiruvi'
        verbose_name_plural = 'C - Bojxona rasmiylashtiruvi'


class Outsourcing(models.Model):
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = 'Autsorsing'
        verbose_name_plural = 'C - Autsorsing'


class New(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    Image = models.ImageField(verbose_name="Image",
                              upload_to="New", blank=True, null=True)
    Video_file = models.FileField(
        upload_to='post_files', blank=True, null=True)
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'E - Yangiliklar'


class PressCenter_1(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    Image = models.ImageField(verbose_name="Image",
                              upload_to="PressCenter1", blank=True, null=True)
    Video_file = models.FileField(
        upload_to='post_files', blank=True, null=True)
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Matbuot markazi'
        verbose_name_plural = 'E - Matbuot markazi'


class PressCenter_2(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    Image = models.ImageField(verbose_name="Image",
                              upload_to="PressCenter2", blank=True, null=True)
    Video_file = models.FileField(
        upload_to='post_files', blank=True, null=True)
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Ko'rgazma"
        verbose_name_plural = "E - Ko'rgazmalar"


class PhotoGallery(models.Model):
    Image = models.ImageField(verbose_name="Image",
                              upload_to="PhotoGallery/", blank=True, null=True)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = 'Fotogalereya'
        verbose_name_plural = 'E - Fotogalereya'


class VideoGallery(models.Model):
    Video_file = models.FileField(
        upload_to='VideoGallery/', blank=True, null=True)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = 'Videogalereya'
        verbose_name_plural = 'E - Videogalereya'


class AppealOfLegal(models.Model):
    class AppealOfLegalChoiches(models.TextChoices):
        Legal = 'L', _('Legal')
        Individual = 'I', _('Individual')
    Subject = models.CharField(
        verbose_name="Appeal type", choices=AppealOfLegalChoiches.choices, default=AppealOfLegalChoiches.Legal, max_length=2)
    FullName = models.CharField(verbose_name="FullName", max_length=255)
    BirthDate = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    PassportData = models.CharField(
        verbose_name="Passport information", max_length=255)
    Address = models.CharField(verbose_name="Adress", max_length=255)
    Index = models.CharField(verbose_name="Index", max_length=255)
    Email = models.EmailField(
        verbose_name="Email", max_length=255, blank=True, null=True)
    Phone = PhoneField(blank=True, help_text='Contact phone number')
    SubjectType = models.CharField(verbose_name="Subject type", max_length=255)
    QuestionText = models.TextField(verbose_name="Question text")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.FullName

    class Meta:
        verbose_name = 'Yuridik shikoyat'
        verbose_name_plural = 'F - Yuridik shikoyatlar'


class Corruption(models.Model):
    Name = models.CharField(verbose_name="Name", max_length=255)
    Information = RichTextField(
        verbose_name="Information")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Korrupsiyaga oid shikoyat'
        verbose_name_plural = 'F - Korrupsiyaga oid shikoyatlar'


class CompanyDetails(models.Model):
    Location = models.CharField(verbose_name="Location", max_length=255)
    Phone = PhoneField(blank=True, help_text='Contact phone number')
    Video_file = models.FileField(
        upload_to='post_files', blank=True, null=True)
    Email = models.EmailField(verbose_name="Email",
                              max_length=255, blank=True, null=True)
    Work_time = models.CharField(
        verbose_name='Work time', max_length=255, blank=True, null=True)
    YouTube = models.URLField(
        verbose_name="Youtube link", max_length=200, blank=True, null=True)
    Facebook = models.URLField(
        verbose_name="Facebook link", max_length=200, blank=True, null=True)
    Telegram = models.URLField(
        verbose_name="Telegram link", max_length=200, blank=True, null=True)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name = "Kompaniya ma'lumoti"
        verbose_name_plural = "G - Kompaniya ma'lumotlari"


class Image(models.Model):
    Image = models.ImageField(verbose_name="Image", upload_to="MainImages")
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = 'Rasmlar'
        verbose_name_plural = 'G - Web sahifaning asosiy rasmi'


class Telegram(models.Model):
    apiToken = models.CharField(verbose_name="Api Token", max_length=255)
    chatID = models.CharField(verbose_name="Chat Id", max_length=255)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    class Meta:
        verbose_name = 'Telegram'
        verbose_name_plural = 'G - Telegram'
