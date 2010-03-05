from django.db import models
from django.contrib.auth.models import User

from snippets.prodjango.current_user import registration

class CurrentUserField(models.ForeignKey):
    def __init__(self, **kwargs):
        super(CurrentUserField, self).__init__(User, null=True, **kwargs)

    def contribute_to_class(self, cls, name):
        super(CurrentUserField, self).contribute_to_class(cls, name)
        registry = registration.FieldRegistry()
        registry.add_field(cls, self)

try:
    from south.modelsinspector import add_introspection_rules
    rules = [
        (
            (CurrentUserField, ),
            [],
            {
            },
        ),
    ]
    add_introspection_rules(rules, ["^snippets\.prodjango\.current_user\."])
except  ImportError:
    pass
