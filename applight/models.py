from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    content = models.TextField(max_length=255)
    ios_url = models.URLField()
    android_url = models.URLField()
    ios_img = models.ImageField(upload_to="banner")
    android_img = models.ImageField(upload_to="banner")
    banner_img = models.ImageField(upload_to="banner")

    def __str__(self):
        return self.title


class Block(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Item"
        verbose_name_plural = "About Items"


class WatchNow(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField(db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Watch Now"
        verbose_name_plural = "Watch Now"


class FeaturesCentral(models.Model):
    features_img = models.ImageField(upload_to="features")
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Features Central Model"


class Features(models.Model):
    central_model = models.ForeignKey(
        FeaturesCentral,
        on_delete=models.CASCADE,
        related_name="items"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    icon = models.CharField(max_length=255)
    delay = models.CharField(max_length=255)

    def __str__(self):
        return f"Features: {self.title}"


class Team(models.Model):
    member_img = models.ImageField(upload_to="team")
    member_full_name = models.CharField(max_length=255)
    member_position = models.CharField(max_length=255)
    delay = models.CharField(max_length=255)

    def __str__(self):
        return self.member_full_name


class Testimonials(models.Model):
    t_img = models.ImageField(upload_to="testimonials")
    t_full_name = models.CharField(max_length=255)
    t_role = models.CharField(max_length=255)
    t_review = models.TextField(max_length=500)

    def __str__(self):
        return self.t_full_name


class FAQ(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    delay = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=255)

    def __str__(self):
        return "Contacts"


class FormSubmission(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  f"Submission by {self.full_name}"