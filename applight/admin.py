from django.contrib import admin

from .models import (
    Banner,
    About,
    WatchNow,
    FeaturesCentral,
    Features,
    Team,
    Testimonials,
    FAQ,
    Block,
    Contact
)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Banner.objects.exists():
            return False

        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if About.objects.count() >= 3:
            return False

        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(WatchNow)
class WatchNowAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if WatchNow.objects.count() >= 1:
            return False

        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return True


class FeaturesModelInline(admin.TabularInline):
    model = Features
    extra = 1


@admin.register(FeaturesCentral)
class FeaturesCentralAdmin(admin.ModelAdmin):
    inlines = [FeaturesModelInline]

    def has_add_permission(self, request):
        if FeaturesCentral.objects.exists():
            return False

        return super().has_add_permission(request)


admin.site.register(Team)
admin.site.register(Testimonials)
admin.site.register(FAQ)
admin.site.register(Block)
admin.site.register(Contact)
