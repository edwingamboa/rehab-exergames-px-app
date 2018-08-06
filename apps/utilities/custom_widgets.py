from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django_select2.forms import (
    Select2Widget,
    Select2MultipleWidget
)


def generate_new_button(related_url, name):
    return '<a href="%s" class="btn btn-success btn-flat btn-xs margin pull-right" data-related-id="id_%s" ' \
           'onclick="return showAddPopup(this);"><i class="fa fa-plus-circle"></i> New </a>' \
           % (related_url, name)


def generate_default_related_url(related_model):
    rel_to = related_model
    info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
    return 'admin:%s_%s_add' % info

class RelatedFieldWidgetCanAdd(Select2Widget):
    def __init__(self, related_model, related_url=None, *args, **kw):

        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            related_url = generate_default_related_url(related_model)

        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        output.append(generate_new_button(self.related_url, name))
        return mark_safe(''.join(output))


class RelatedFieldWidgetCanAddMultiple(Select2MultipleWidget):
    def __init__(self, related_model, related_url=None, *args, **kw):

        super(RelatedFieldWidgetCanAddMultiple, self).__init__(*args, **kw)

        if not related_url:
            related_url = generate_default_related_url(related_model)

        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAddMultiple, self).render(name, value, *args, **kwargs)]
        output.append(generate_new_button(self.related_url, name))
        return mark_safe(''.join(output))
