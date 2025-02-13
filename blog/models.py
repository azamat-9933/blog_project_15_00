from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def post_count(self):
        return self.posts.count()



class Post(models.Model):
    class DifficultyChoices(models.TextChoices):
        easy = "Easy"
        medium = "Medium"
        hard = "Hard"

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True, upload_to="posts/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0, editable=False)
    difficulty = models.CharField(max_length=30, choices=DifficultyChoices.choices)
    reading_time = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="posts")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"