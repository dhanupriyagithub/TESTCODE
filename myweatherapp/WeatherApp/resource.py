from .models import City
from import_export import resources

class cityResource(resources.ModelResource):

    class Meta:
        model=City