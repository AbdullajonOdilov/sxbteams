from django.urls import path
from .views import ( index, about_us, works, employee, products, product_kategory,
            product_kategory_detail, services, message, news,
            press_center_1, press_center_2, new_details, feedback, press_center_1_details, press_center_2_details, photo_gallery, video_gallery, corruption, contact, set_language)

urlpatterns = [
    path('', index, name="index"),
    path('about-us/', about_us, name="about_us"),
    path('works/', works, name="works"),
    path('employee/', employee, name="employee"),
    path('products/<int:id>/', products, name="products"),
    path('product_kategory/<int:id>/', product_kategory, name="product_kategory"),
    path('product_kategory_detail/<int:id>/', product_kategory_detail, name="product_kategory_detail"),
    path('services/<int:id>/', services, name="services"),
    path('message/', message, name="message"),
    path('news/', news, name="news"),
    path('new/<int:id>/', new_details, name="new"),
    path('press-center_1/', press_center_1, name="press_center_1"),
    path('press-center_1_details/<int:id>/', press_center_1_details, name="press_center_1_details"),
    path('press-center_2/', press_center_2, name="press_center_2"),
    path('press-center_2_details/<int:id>/', press_center_2_details, name="press_center_2_details"),
    path('feedback/', feedback, name="feedback"),
    path('photo-gallery/', photo_gallery, name="photo_gallery"),
    path('video-gallery/', video_gallery, name="video_gallery"),
    path('corruption/', corruption, name="corruption"),
    path('contact/', contact, name="contact"),
    path('set_language/<int:id>/', set_language, name="set_language"),

]
handler404 = "importapp.views.page_not_found_view"