from django.contrib import admin
from .models import ChaiVariety, ChaiCertificate, chaiReview, Store

# Register your models here.

# tabular inline se wo doosre model k saath hi dikhta h alag se model nahi dikhta
# extra = 2 mtlb iske field kitni baar dikhenge
class ChaiReviewInline(admin.TabularInline):
    model = chaiReview
    extra=2

# admin.ModelAdmin is most popular, list_display m jo bhi daal rahe ho these are model ki fields 
# inlines mtlb iski inline m doosra wala class hoga
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'date_added')
    inlines = (ChaiReviewInline,)

# Many to many m useful filter_horizontal
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date')
    
admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
admin.site.register(Store, StoreAdmin)



