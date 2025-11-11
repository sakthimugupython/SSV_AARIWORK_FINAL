from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200, default="Crafting Dreams into Reality", help_text="Main hero title")
    subtitle = models.TextField(default="Experience the timeless artistry of traditional AARI embroidery.", help_text="Hero subtitle/description")
    primary_button_text = models.CharField(max_length=50, default="Explore Collections")
    primary_button_url = models.CharField(max_length=100, default="/collections/")
    secondary_button_text = models.CharField(max_length=50, default="Get Quote")
    secondary_button_url = models.CharField(max_length=100, default="/contact/")
    background_image = models.ImageField(upload_to='hero/', blank=True, null=True, help_text="Background image for hero section")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    icon_class = models.CharField(max_length=50, default="fas fa-tshirt", help_text="FontAwesome icon class (e.g., fas fa-tshirt)")
    title = models.CharField(max_length=100, default="Custom Tailored Blouses")
    description = models.TextField(default="Perfect fit with unique embroidery")
    order = models.PositiveIntegerField(default=0, help_text="Order for display")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Collection(models.Model):
    name = models.CharField(max_length=100, default="Basic Collection")
    description = models.TextField(default="Exquisite AARI designs showcasing traditional craftsmanship and modern aesthetics.")
    image = models.ImageField(upload_to='collections/', blank=True, null=True)
    button_text = models.CharField(max_length=50, default="Explore Collection")
    button_url = models.CharField(max_length=100, default="/collections/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Arrival(models.Model):
    name = models.CharField(max_length=100, default="Product")
    description = models.TextField(default="Beautiful AARI embroidery piece showcasing traditional craftsmanship.")
    image = models.ImageField(upload_to='arrivals/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    button_text = models.CharField(max_length=50, default="Enquiry Now")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class AcademySection(models.Model):
    title = models.CharField(max_length=100, default="SSV Academy")
    description = models.TextField(default="Learn the art of Aari embroidery from expert women trainers.")
    feature1 = models.CharField(max_length=100, default="Beginner | Intermediate | Premium Bridal Courses")
    feature2 = models.CharField(max_length=100, default="Online & Offline learning")
    feature3 = models.CharField(max_length=100, default="Certification & gallery showcase")
    button_text = models.CharField(max_length=50, default="Enroll Now")
    button_url = models.CharField(max_length=100, default="/academy/")
    image1 = models.ImageField(upload_to='academy/', blank=True, null=True)
    image2 = models.ImageField(upload_to='academy/', blank=True, null=True)
    image3 = models.ImageField(upload_to='academy/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class GalleryItem(models.Model):
    title = models.CharField(max_length=100, default="Gallery Item")
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class AboutHeroSection(models.Model):
    title = models.CharField(max_length=200, default="About SVV Aari Work", help_text="Main hero title")
    subtitle = models.TextField(default="Discover the story behind our passion for traditional AARI embroidery.", help_text="Hero subtitle")
    years_experience = models.PositiveIntegerField(default=15)
    designs_completed = models.PositiveIntegerField(default=1000)
    happy_clients = models.PositiveIntegerField(default=500)
    background_image = models.ImageField(upload_to='about/hero/', blank=True, null=True, help_text="Background image for hero section")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class AboutStory(models.Model):
    title = models.CharField(max_length=100, default="Our Story")
    main_text = models.TextField(default="Founded with a vision to preserve traditional AARI embroidery...")
    secondary_text = models.TextField(default="What started as a small initiative has grown into a comprehensive platform...")
    value1_icon = models.CharField(max_length=50, default="fas fa-heart")
    value1_title = models.CharField(max_length=100, default="Women Empowerment")
    value2_icon = models.CharField(max_length=50, default="fas fa-gem")
    value2_title = models.CharField(max_length=100, default="Traditional Craft")
    value3_icon = models.CharField(max_length=50, default="fas fa-globe")
    value3_title = models.CharField(max_length=100, default="Cultural Heritage")
    story_image = models.ImageField(upload_to='about/story/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class AboutMissionVision(models.Model):
    mission_title = models.CharField(max_length=100, default="Our Mission")
    mission_text = models.TextField(default="To preserve the traditional art of AARI embroidery...")
    mission_icon = models.CharField(max_length=50, default="fas fa-bullseye")
    vision_title = models.CharField(max_length=100, default="Our Vision")
    vision_text = models.TextField(default="To become a global leader in authentic AARI embroidery...")
    vision_icon = models.CharField(max_length=50, default="fas fa-eye")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Mission & Vision"

class AboutValue(models.Model):
    icon_class = models.CharField(max_length=50, default="fas fa-leaf", help_text="FontAwesome icon class")
    title = models.CharField(max_length=100, default="Sustainability")
    description = models.TextField(default="Eco-friendly practices and materials")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class AboutReason(models.Model):
    icon_class = models.CharField(max_length=50, default="fas fa-clock", help_text="FontAwesome icon class")
    title = models.CharField(max_length=100, default="15+ Years Experience")
    description = models.TextField(default="Master artisans with decades of expertise")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class ContactHeroSection(models.Model):
    title = models.CharField(max_length=200, default="Contact Us", help_text="Main banner title")
    subtitle = models.TextField(default="Get in touch with us for inquiries, custom orders, or workshop registrations", help_text="Banner subtitle/description")
    background_image = models.ImageField(upload_to='contact/hero/', blank=True, null=True, help_text="Background image for contact banner")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class AcademyHero(models.Model):
    title = models.CharField(max_length=200, default="SSV Academy", help_text="Main hero title")
    subtitle = models.TextField(default="Master the art of AARI embroidery from master craftsmen.", help_text="Hero subtitle")
    course_levels = models.PositiveIntegerField(default=4)
    students_trained = models.PositiveIntegerField(default=500)
    certification_rate = models.PositiveIntegerField(default=100)
    background_image = models.ImageField(upload_to='academy/hero/', blank=True, null=True, help_text="Background image for hero section")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class AcademyIntroduction(models.Model):
    title = models.CharField(max_length=200, default="Master the Art of AARI")
    main_text = models.TextField(default="At SSV Academy, we believe that the beauty of AARI embroidery should be shared with the world.")
    feature1_icon = models.CharField(max_length=50, default="fas fa-user-graduate")
    feature1_title = models.CharField(max_length=100, default="Expert Instructors")
    feature1_description = models.TextField(default="Learn from master craftsmen with decades of experience")
    feature2_icon = models.CharField(max_length=50, default="fas fa-hands-helping")
    feature2_title = models.CharField(max_length=100, default="Hands-on Learning")
    feature2_description = models.TextField(default="Practical training with real materials and techniques")
    feature3_icon = models.CharField(max_length=50, default="fas fa-users")
    feature3_title = models.CharField(max_length=100, default="Small Class Sizes")
    feature3_description = models.TextField(default="Personalized attention in intimate learning environments")
    feature4_icon = models.CharField(max_length=50, default="fas fa-certificate")
    feature4_title = models.CharField(max_length=100, default="Certification Provided")
    feature4_description = models.TextField(default="Official recognition of your skills and expertise")
    background_image = models.ImageField(upload_to='academy/intro/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class AcademyCourse(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    title = models.CharField(max_length=100, default="Beginner Aari Course")
    duration = models.CharField(max_length=50, default="4 Weeks")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=2500.00)
    description = models.TextField(default="Perfect for absolute beginners. Learn the fundamentals of Aari embroidery.")
    schedule = models.CharField(max_length=100, default="Mon–Wed–Fri, 10 AM – 12 PM")
    feature1 = models.CharField(max_length=100, default="Basic stitching techniques")
    feature2 = models.CharField(max_length=100, default="Thread handling & fabric preparation")
    feature3 = models.CharField(max_length=100, default="Simple floral patterns")
    image = models.ImageField(upload_to='academy/courses/', blank=True, null=True)
    enrollment_url = models.URLField(default="https://wa.me/+917639027885")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class AcademyBenefit(models.Model):
    icon_class = models.CharField(max_length=50, default="fas fa-infinity", help_text="FontAwesome icon class")
    title = models.CharField(max_length=100, default="Lifetime Access")
    description = models.TextField(default="Video tutorials for online students")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class AcademyTestimonial(models.Model):
    name = models.CharField(max_length=100, default="Priya Sharma")
    role = models.CharField(max_length=100, default="Advanced Graduate")
    content = models.TextField(default="SSV Academy transformed my hobby into a successful business.")
    rating = models.PositiveIntegerField(default=5)
    avatar_color = models.CharField(max_length=20, default="#007bff")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class AcademyCTA(models.Model):
    title = models.CharField(max_length=200, default="Ready to Start Your AARI Journey?")
    subtitle = models.TextField(default="Join hundreds of students who have discovered their passion for AARI embroidery")
    button_text = models.CharField(max_length=50, default="Contact for Enrollment")
    button_url = models.URLField(default="https://wa.me/+917639027885")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class HomeTestimonial(models.Model):
    video_title = models.CharField(max_length=150, blank=True, default="", help_text="Title to display for the testimonial video")
    name = models.CharField(max_length=100, default="Customer Name")
    content = models.TextField(default="Amazing service and quality work!")
    video = models.FileField(upload_to='testimonials/videos/', blank=True, null=True, help_text="Upload customer testimonial video")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
