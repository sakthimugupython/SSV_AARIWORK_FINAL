from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import HeroSection, Service, Collection, Arrival, AcademySection, GalleryItem, AboutHeroSection, AboutStory, AboutMissionVision, AboutValue, AboutReason, AcademyHero, AcademyIntroduction, AcademyCourse, AcademyBenefit, AcademyTestimonial, AcademyCTA, ContactHeroSection, HomeTestimonial

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

def home(request):
    # Fetch dynamic content
    hero = HeroSection.objects.filter(is_active=True).first()
    services = Service.objects.all()
    collections = Collection.objects.all()[:3]  # Limit to 3 for home page
    arrivals = Arrival.objects.all()[:8]  # Limit to 8 for display
    academy = AcademySection.objects.filter(is_active=True).first()
    gallery_items = GalleryItem.objects.all()[:3]  # Limit to 3 for display
    courses = AcademyCourse.objects.all()[:4]  # Limit to 4 courses for home page

    testimonials = HomeTestimonial.objects.all()  # Fetch all testimonials

    context = {
        'hero': hero,
        'services': services,
        'collections': collections,
        'arrivals': arrivals,
        'academy': academy,
        'gallery_items': gallery_items,
        'courses': courses,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create email content
        email_subject = f"Contact Form: {subject}"
        email_body = f"""
New contact form submission:

Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject}

Message:
{message}
        """

        try:
            # Send email to admin (appears to come from customer's email)
            send_mail(
                email_subject,
                email_body,
                email,  # From customer's email address
                [settings.ADMIN_EMAIL],  # To admin email
                fail_silently=False,
            )

            # Send confirmation email to user (from default address)
            confirmation_subject = "Thank you for contacting SSV AARI WORK"
            confirmation_body = f"""
Dear {name},

Thank you for contacting SSV AARI WORK. We have received your message and will get back to you within 24 hours.

Your message details:
Subject: {subject}
Message: {message}

Best regards,
SSV AARI WORK Team
            """

            send_mail(
                confirmation_subject,
                confirmation_body,
                settings.DEFAULT_FROM_EMAIL,  # From default address for confirmation
                [email],  # Send confirmation to user's email
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')

        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again or contact us directly.')
            return redirect('contact')

    # Handle GET request - fetch dynamic content and return the contact form
    hero = ContactHeroSection.objects.filter(is_active=True).first()
    context = {'hero': hero}
    return render(request, 'contact.html', context)

def about(request):
    # Fetch dynamic content for about page
    hero = AboutHeroSection.objects.filter(is_active=True).first()
    story = AboutStory.objects.filter(is_active=True).first()
    mission_vision = AboutMissionVision.objects.filter(is_active=True).first()
    values = AboutValue.objects.all()
    reasons = AboutReason.objects.all()

    context = {
        'hero': hero,
        'story': story,
        'mission_vision': mission_vision,
        'values': values,
        'reasons': reasons,
    }
    return render(request, 'about.html', context)

def collections(request):
    # Fetch dynamic content for collections page
    hero = HeroSection.objects.filter(is_active=True).first()
    collections_data = Collection.objects.all()
    arrivals = Arrival.objects.all()[:6]  # Limit to 6 for collections page
    academy = AcademySection.objects.filter(is_active=True).first()
    courses = AcademyCourse.objects.all()[:4]  # Limit to 4 courses for collections page

    context = {
        'hero': hero,
        'collections': collections_data,
        'arrivals': arrivals,
        'academy': academy,
        'courses': courses,
    }
    return render(request, 'collections.html', context)

def ssv_academy(request):
    # Fetch dynamic content for academy page
    hero = AcademyHero.objects.filter(is_active=True).first()
    introduction = AcademyIntroduction.objects.filter(is_active=True).first()
    courses = AcademyCourse.objects.all()
    benefits = AcademyBenefit.objects.all()
    testimonials = AcademyTestimonial.objects.all()[:2]  # Limit to 2 for display
    cta = AcademyCTA.objects.filter(is_active=True).first()

    context = {
        'hero': hero,
        'introduction': introduction,
        'courses': courses,
        'benefits': benefits,
        'testimonials': testimonials,
        'cta': cta,
    }
    return render(request, 'ssv_academy.html', context)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AuthenticationForm()

    # Add placeholders to form fields
    form.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
    form.fields['password'].widget.attrs.update({'placeholder': 'Enter your password'})

    return render(request, 'auth/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    # Add placeholders to form fields
    form.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
    form.fields['email'].widget.attrs.update({'placeholder': 'Enter your email address'})
    form.fields['password1'].widget.attrs.update({'placeholder': 'Create a password'})
    form.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})

    return render(request, 'auth/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                # Generate password reset link (for demo, we'll just send a confirmation)
                reset_link = f"http://127.0.0.1:8000/reset-password/{user.id}/"

                subject = "Password Reset Request - SSV AARI WORK"
                message = f"""
                Hello {user.username},

                You requested a password reset for your SSV AARI WORK account.

                Click the link below to reset your password:
                {reset_link}

                If you didn't request this, please ignore this email.

                Best regards,
                SSV AARI WORK Team
                """

                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                messages.success(request, 'Password reset instructions have been sent to your email.')
                return redirect('login')

            except User.DoesNotExist:
                messages.error(request, 'No account found with this email address.')
                return render(request, 'auth/forgot_password.html')

    return render(request, 'auth/forgot_password.html')

def reset_password(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'Invalid reset link.')
        return redirect('login')

    if request.method == 'POST':
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if new_password and confirm_password:
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password reset successfully! You can now login with your new password.')
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match.')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'auth/reset_password.html', {'user': user})
