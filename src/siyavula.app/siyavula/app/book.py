from five import grok
from zope import schema

from plone.directives import form

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from siyavula.app import _

class IBook(form.Schema):
    """A book.
    """
    
    title = schema.TextLine(
            title=_(u"Title"),
        )
    
    description = schema.Text(
            title=_(u"A short summary"),
        )
    
    content = RichText(
            title=_(u"Content"),
            description=_(u"A longer description of the book"),
            required=False
        )
    
    cover = NamedImage(
            title=_(u"Cover Image"),
            description=_(u"Please upload an image"),
            required=False
        )

    price = schema.TextLine(
            title=_(u"Price"),
            description=_(u"Price of the book, including the Rand sign"),
            required=False
        )
    
    availability = schema.TextLine(
            title=_(u"Availability"),
            description=_(u"Availability, eg 'Out of Stock', 'In stock'"),
            required=False
        )
    
    shipping = schema.TextLine(
            title=_(u"Shipping details"),
            description=_(u"When it will ship, eg 'Ships in 3 days'"),
            required=False
        )
    
    download_link = schema.TextLine(
            title=_(u"Download Link"),
            description=_(u"Link for a direct download."),
            required=False
        )
    
    online_link = schema.TextLine(
            title=_(u"Online reading link"),
            description=_(u"Link for reading the book online"),
            required=False
        )
    
class View(grok.View):
    grok.context(IBook)
    grok.require('zope2.View')

