from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import MyUser  # Импортируйте только MyUser
from tour.models import Tour, Booking  # Импортируйте Tour и Booking из приложения tour
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email', 'status', 'is_admin')
    search_fields = ('username', 'phone_number', 'email')
    list_filter = ('status', 'is_admin')

class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'available_seats')
    search_fields = ('title', 'category')
    list_filter = ('category', 'price')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('tour', 'user', 'date', 'status', 'total_price')
    search_fields = ('tour__title', 'user__username')
    list_filter = ('status', 'date')
    actions = ['export_bookings_to_csv']

    @admin.action(description='Выгрузить отчеты по бронированиям')
    def export_bookings_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="bookings.csv"'
        writer = csv.writer(response)
        writer.writerow(['Tour', 'User', 'Date', 'Status', 'Total Price'])

        for booking in queryset:
            writer.writerow([booking.tour, booking.user, booking.date, booking.status, booking.total_price])

        return response

@receiver(post_save, sender=Tour)
def send_tour_creation_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Новый тур создан',
            f'Тур "{instance.title}" был успешно создан!',
            'admin@yourapp.com',
            [instance.author.email],
        )

admin.site.register(MyUser, MyUserAdmin)
# admin.site.register(Tour, TourAdmin)
# admin.site.register(Booking, BookingAdmin)
