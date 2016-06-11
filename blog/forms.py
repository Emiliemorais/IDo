from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from models import Message, Questionnaire


class MessageForm(forms.ModelForm):

    
    """MessageForm Class. TThis class contains the treatments
     of the existents forms on create message page.
    """

    class Meta:

        """Meta Class. This class defines the informations
        that will be used based on existent set
        from Message Model.
        """

        model = Message
        fields = '__all__'

class QuestionnarieForm(forms.ModelForm):

    
    """QuestionnarieForm Class. TThis class contains the treatments
     of the existents forms on create message page.
    """

    class Meta:

        """Meta Class. This class defines the informations
        that will be used based on existent set
        from Questionnarie Model.
        """

        model = Questionnaire
        fields = '__all__'