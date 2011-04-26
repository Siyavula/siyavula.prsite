from five import grok
from zope import schema

from plone.directives import form, dexterity

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

class View(grok.View):
    grok.context(IBook)
    grok.require('zope2.View')

