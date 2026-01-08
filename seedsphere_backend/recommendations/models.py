from django.db import models

from django.db import models

class Plant(models.Model):
    """
    Django model for Plant data stored as nested documents in MongoDB
    Maps to your MongoDB collection structure with subdocuments
    """
    
    # ========== BASIC IDENTITY ==========
    plant_id = models.CharField(max_length=50, unique=True)
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    short_description = models.TextField()
    images = models.JSONField(default=list, blank=True)  # Array of image URLs
    
    # ========== CHARACTERISTICS & USE CASES ==========
    plant_type = models.JSONField(default=list, blank=True)  # Array: ["Air Purifying", "Flowering", ...]
    growth_rate = models.CharField(max_length=100, blank=True)  # "Fast", "Slow", "Medium"
    max_height = models.CharField(max_length=255, blank=True)
    bloom_season = models.CharField(max_length=255, blank=True)
    
    # ========== CARE & MAINTENANCE (IMPORTANT FOR RECOMMENDATIONS) ==========
    maintenance_level = models.CharField(max_length=100)  # "Low", "Medium", "High" - FILTER FIELD
    sunlight_needs = models.CharField(max_length=255)
    watering_frequency = models.CharField(max_length=255)
    soil_type = models.CharField(max_length=255)
    soil_ph = models.CharField(max_length=50, blank=True)
    fertilizer = models.TextField(blank=True)
    propagation_method = models.JSONField(default=list, blank=True)
    difficulty = models.CharField(max_length=255, blank=True)
    
    # ========== HEALTH & SAFETY ==========
    toxic_to_cats = models.BooleanField(default=False)
    toxic_to_dogs = models.BooleanField(default=False)
    toxic_to_humans = models.BooleanField(default=False)
    toxicity_notes = models.TextField(blank=True)
    common_pests = models.JSONField(default=list, blank=True)
    common_diseases = models.JSONField(default=list, blank=True)
    
    # ========== SCIENCE & EXTRA INFO ==========
    special_feature = models.TextField(blank=True)
    
    # ========== LOCATION/AREA (FOR RECOMMENDATIONS) ==========
    area = models.CharField(
        max_length=100,
        default="All",
        help_text="Geographic area/region (e.g., Indoor, Outdoor, Balcony, Garden)"
    )
    
    # ========== METADATA ==========
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'plants'
        ordering = ['common_name']
        indexes = [
            models.Index(fields=['plant_type']),
            models.Index(fields=['maintenance_level']),
            models.Index(fields=['area']),
        ]
    
    def __str__(self):
        return f"{self.common_name} (ID: {self.plant_id})"

