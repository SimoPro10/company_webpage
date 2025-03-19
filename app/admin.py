from django.contrib import admin
from .models import (GeneralInfo,
                     Service,
                     Testimonial,
                     FrequentlyAskedQuestions,
                     ContactFormLog,Blog,Author)

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name']
    readonly_fields = ['email']
  
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description']
    search_fields = ['title',
                    'description']
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["username",
                    "user_job_title",
                    "display_rating_count",
                    ]
    
    def display_rating_count(self, obj):
        return '*' * obj.rating_count

    display_rating_count.short_description = "Rating"

@admin.register(FrequentlyAskedQuestions)
class FrequentlyAskedQuestionsAdmin(admin.ModelAdmin):
    list_display = ['question','answer']

@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'subject',
                    'action_time',
                    'is_success',
                    'is_error',
                    ]
    def has_add_permission(self, request):
        pass

    def has_change_permission(self, request, obj=None):
        pass
    
    def has_delete_permission(self, request, obj=None):
        pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name',
                    'last_name',
                        ]



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
                    'category',
                    'blog_image',
                    'created_at']
        
    