from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from models import Enterprise


class EnterpriseUpdateForm(forms.ModelForm):

    
    """EnterpriseUpdateForm Class. TThis class contains the treatments
     of the existents forms on update enterprise information page.
    """

    class Meta:

        """Meta Class. This class defines the informations
        that will be used based on existent set
        from Enterprise Model.
        """

        model = Enterprise
        fields = '__all__'
