from django.db import models

# Create your models here.
class Blog(models.Model):
    # _id = models.ObjectIdField()
    vin_number = models.CharField(max_length=30,blank=False, default='')
    iframe = models.TextField()
    iframe_with_params = models.TextField()
    src = models.TextField()
    src_with_params = models.TextField()
    short_id = models.TextField()
    privacy = models.TextField()
    white_label = models.TextField()
    full_screen = models.TextField()
    short_url = models.TextField()
    thumb = models.TextField()
    fields = models.JSONField()
    gallery = models.JSONField()
    interior_hotspots = models.JSONField()
    interior_conditions = models.JSONField()
    exterior_conditions = models.JSONField()
    exterior_hotspots = models.JSONField()
    gallery_pics = models.JSONField()
    safetyFeatures = models.JSONField()
    entertainmentFeatures = models.JSONField()
    luxuryFeatures = models.JSONField()

   

    class Meta:
        db_table = 'mongo_blog'