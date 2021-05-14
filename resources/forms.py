from django.forms.models import BaseInlineFormSet


class NonRequiredInlineFormSet(BaseInlineFormSet):
    
    def _construct_form(self, i, **kwargs):
        form = super(NonRequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = True
        return form
