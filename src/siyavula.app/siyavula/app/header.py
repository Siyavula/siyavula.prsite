from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from siyavula.app import _

class IHeader(form.Schema):
    """A header image.
    """
    
    title = schema.TextLine(
            title=_(u"Title"),
        )
    
    header = NamedImage(
            title=_(u"Header Image"),
            description=_(u"An image displayed as a banner at the top of the section."),
        )

    headerblurb = RichText(
            title=_(u"Header Blurb"),
            description=_(u"The blurb (Text) displayed on top of the header image, if any. Recommended styles: H2 and normal text."),
        )
