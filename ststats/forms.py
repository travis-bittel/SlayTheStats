from django import forms

import ststats.query.query
from ststats import models


class QueryForm(forms.Form):
    CHARACTERS = (
        ("IRONCLAD", "Ironclad"),
        ("THE_SILENT", "Silent"),
        ("DEFECT", "Defect"),
        ("WATCHER", "Watcher")
    )

    character = forms.ChoiceField(choices=CHARACTERS)
    attribute = forms.ChoiceField(choices=[(attribute, attribute.replace('_', ' ').title())
                                           for attribute in ststats.query.query.ATTRIBUTES])


class FilterForm(forms.Form):
    name = forms.CharField()

