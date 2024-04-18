import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AboutModel(BaseModel):
    ava = models.ImageField(upload_to='about/')
    name_uz = models.CharField(max_length=15)
    name_ru = models.CharField(max_length=15)
    name_en = models.CharField(max_length=15)
    short_description_uz = models.CharField(max_length=100, null=True, blank=True)
    short_description_ru = models.CharField(max_length=100, null=True, blank=True)
    short_description_en = models.CharField(max_length=100, null=True, blank=True)
    long_description_uz = RichTextUploadingField()
    long_description_ru = RichTextUploadingField()
    long_description_en = RichTextUploadingField()

    def __str__(self):
        return self.name_en

    def save(self, *args, **kwargs):
        if AboutModel.objects.exists():
            raise ValidationError("Only one instance of AboutModel is allowed.")
        super(AboutModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'About'


class TagModel(BaseModel):
    name_uz = models.CharField(max_length=30)
    name_ru = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)

            while BlogModel.objects.filter(slug=self.slug).exists():
                slug = BlogModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name_en:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

            super().save(*args, **kwargs)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tags'


class BlogModel(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    description_uz = RichTextUploadingField()
    description_ru = RichTextUploadingField()
    description_en = RichTextUploadingField()
    image = models.ImageField(upload_to='blog/images')
    tags = models.ManyToManyField(TagModel, blank=True, related_name='blogs')
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)

            while BlogModel.objects.filter(slug=self.slug).exists():
                slug = BlogModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title_en:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

            super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        db_table = 'blogs'
        ordering = ['-created_at']


class ProjectModel(BaseModel):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images')
    description_uz = RichTextUploadingField()
    description_ru = RichTextUploadingField()
    description_en = RichTextUploadingField()
    github = models.URLField(blank=True, null=True)
    source = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)

            while BlogModel.objects.filter(slug=self.slug).exists():
                slug = BlogModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name_en:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'projects'


class ContactModel(BaseModel):
    name = models.CharField(max_length=255)
    email_or_phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        db_table = 'contacts'


class SocialModel(BaseModel):
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    github = models.URLField()
    linkedin = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    telegram = models.URLField()

    def __str__(self):
        return "socials"

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'
