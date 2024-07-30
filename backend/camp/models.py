from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.
class Campaign(models.Modal):
    title=models.Charfield(max_length=200)
    description=models.Textfield()
    slug=models.models.Slugfield(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    logo=CloudinaryField('Image', overwrite=True,format="jpg")
    
    
    class Meta:
        ordering=('-created_at',)
        
    def __str__(self):
        return self.title
    
    def save(self,**args, **kwargs ):
        to_assign=slugify(self.title)

        if Campaign.objects.filter(slug=to_assign).exist():
            
            to_assign=to_assign+str(Campaign.object.all().count())
            
        self.slug=to_assign
        
        super().save(**args,**kwargs)

class Subscriber(modals.Model):
    campaign=models.ForeignKey(to=Campaign, on_delete=models.DO_NOTHING)