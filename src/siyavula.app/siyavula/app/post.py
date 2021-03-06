from five import grok
from zope import schema

from plone.directives import form

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from siyavula.app import _

class IPost(form.Schema):
    """A Post."""
    
    title = schema.TextLine(
            title=_(u"Title"),
        )
    
    description = schema.Text(
            title=_(u"A short summary"),
        )
    
    content = RichText(
            title=_(u"Content"),
            description=_(u"The actual post"),
            required=False
        )
    
    image = NamedImage(
            title=_(u"Image"),
            description=_(u"An image to display with this item"),
            required=False
        )

    url = schema.TextLine(
            title=_(u"URL"),
            description=_(u"An url this item should point to. In most cases, the post url will be used."),
            required=False,
        )

    form_embed_code = schema.Text(
            title=_(u"Form embed code"),
            description=_(u"Use this to embed a google form in the detail view for this post. Normally used for course signups."),
            required=False,
        )

class View(grok.View):
    grok.context(IPost)
    grok.require('zope2.View')
