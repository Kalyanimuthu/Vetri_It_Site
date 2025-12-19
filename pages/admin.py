from django.contrib import admin
from .models import (
    EnquiryModal,
    EnquiryService,
    AboutCard,
    WebDevelopmentPage,
    WebFeature,
    ServiceSection,
    PricingFeature,
    PricingPlan,
    PricingSection,
    HomePage,
    HomeStat,
    WhyBestSection,
    WhyBestPoint,
    WorkProcess,
    Testimonial,
    Project,
    FAQ,
)

# =========================
# HOME PAGE INLINES
# =========================

class HomeStatInline(admin.TabularInline):
    model = HomeStat
    extra = 3


class WorkProcessInline(admin.TabularInline):
    model = WorkProcess
    extra = 6


class TestimonialInline(admin.StackedInline):
    model = Testimonial
    extra = 3


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 6


class FAQInline(admin.StackedInline):
    model = FAQ
    extra = 4


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    inlines = [
        HomeStatInline,
        WorkProcessInline,
        TestimonialInline,
        ProjectInline,
        FAQInline,
    ]


# =========================
# WHY BEST SECTION
# =========================

class WhyBestPointInline(admin.TabularInline):
    model = WhyBestPoint
    extra = 6


@admin.register(WhyBestSection)
class WhyBestSectionAdmin(admin.ModelAdmin):
    inlines = [WhyBestPointInline]


# =========================
# WEB DEVELOPMENT PAGE
# =========================

class WebFeatureInline(admin.TabularInline):
    model = WebFeature
    extra = 5


@admin.register(WebDevelopmentPage)
class WebDevelopmentPageAdmin(admin.ModelAdmin):
    inlines = [
        WebFeatureInline,
        
    ]

@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page_type')
    list_filter = ('page_type',)

# =========================
# PRICING
# =========================

class PricingFeatureInline(admin.TabularInline):
    model = PricingFeature
    extra = 5


class PricingPlanInline(admin.StackedInline):
    model = PricingPlan
    extra = 3
    show_change_link = True


@admin.register(PricingSection)
class PricingSectionAdmin(admin.ModelAdmin):
    inlines = [PricingPlanInline]


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    inlines = [PricingFeatureInline]


@admin.register(AboutCard)
class AboutCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order', 'is_active')
    list_filter = ('section', 'is_active')
    ordering = ('order',)

class EnquiryServiceInline(admin.TabularInline):
    model = EnquiryService
    extra = 4


@admin.register(EnquiryModal)
class EnquiryModalAdmin(admin.ModelAdmin):
    inlines = [EnquiryServiceInline]
