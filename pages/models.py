from django.db import models
from ckeditor.fields import RichTextField

class HomePage(models.Model):
    hero_title = RichTextField()
    hero_subtitle = RichTextField()
    hero_image = models.ImageField(upload_to="home/hero/")
    cta_text = models.CharField(max_length=50, default="Get Started")

    def __str__(self):
        return "Home Page"

class HomeStat(models.Model):
    home = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="stats")
    value = models.CharField(max_length=20)   # 20+
    label = models.CharField(max_length=50)   # Projects

    def __str__(self):
        return f"{self.value} {self.label}"

class WhyBestSection(models.Model):
    home = models.ForeignKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name="why_best_sections",
        null=True,      # 👈 TEMPORARY
        blank=True      # 👈 TEMPORARY
    )
    title = RichTextField()
    highlight_word = models.CharField(max_length=50)
    image = models.ImageField(upload_to="home/why-best/")


class WhyBestPoint(models.Model):
    section = models.ForeignKey(
        WhyBestSection,
        on_delete=models.CASCADE,
        related_name="points"
    )
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to="home/why-best-point/")

    def __str__(self):
        return self.text

class WorkProcess(models.Model):
    home = models.ForeignKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name="processes"
    )
    image = models.ImageField(upload_to="home/process/")

    def __str__(self):
        return "Work Process Image"

class Testimonial(models.Model):
    home = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="testimonials")
    name = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to="home/testimonials/")
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.name

class Project(models.Model):
    home = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="projects")
    image = models.ImageField(upload_to="home/projects/")

    def __str__(self):
        return "Project Image"

class FAQ(models.Model):
    home = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="faqs")
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question

class WebDevelopmentPage(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    description = RichTextField()
    hero_image = models.ImageField(upload_to='web/')

    def __str__(self):
        return "Web Development Page"


class WebFeature(models.Model):
    page = models.ForeignKey(WebDevelopmentPage, on_delete=models.CASCADE, related_name="features")
    icon_class = models.CharField(
        max_length=50,
        help_text="Example: bx bx-code-alt"
    )
    bg_color = models.CharField(
        max_length=20,
        help_text="Tailwind color: bg-red-100, bg-green-100"
    )
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ServiceSection(models.Model):
    PAGE_TYPE = (
        ('web', 'web_devlopment'),
        ('software', 'software_devlopment'),
        ('digital', 'digital_marketing'),
        ('about', 'about_us'),
    )

    page_type = models.CharField(
        max_length=20,
        choices = PAGE_TYPE
        )

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")

    IMAGE_POSITION = (
        ('left', 'Image Left'),
        ('right', 'Image Right'),
    )
    image_position = models.CharField(
        max_length=10,
        choices=IMAGE_POSITION,
        default='right'
    )

    def __str__(self):
        return self.title

class PricingSection(models.Model):
    PAGE_TYPE = (
        ('web', 'web_devlopment'),
        ('digital', 'digital_marketing'),
    )

    page_type = models.CharField(
        max_length=20,
        choices = PAGE_TYPE
        )
    title = models.CharField(max_length=200, default="Plans & Pricing")

    def __str__(self):
        return f"{self.page_type} {self.title}"


class PricingPlan(models.Model):
    section = models.ForeignKey(
        PricingSection,
        on_delete=models.CASCADE,
        related_name="plans"
    )

    name = models.CharField(max_length=100)   # Basic / Standard / Premium
    price = models.CharField(max_length=50)  # ₹7,999
    button_text = models.CharField(max_length=50, default="Buy Now")

    def __str__(self):
        return f"{self.section} {self.name}"


class PricingFeature(models.Model):
    plan = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        related_name="features"
    )
    feature = models.CharField(max_length=200)

    def __str__(self):
        return self.feature

class AboutCard(models.Model):
    SECTION_CHOICES = (
        ('vision', 'Our Vision'),
        ('mission', 'Our Mission'),
    )

    section = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(
        upload_to="about/images/"
    )

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"

class EnquiryModal(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True)
    button_text = models.CharField(max_length=50, default="Get a Quote")

    def __str__(self):
        return self.title


class EnquiryService(models.Model):
    modal = models.ForeignKey(
        EnquiryModal,
        on_delete=models.CASCADE,
        related_name="services"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
