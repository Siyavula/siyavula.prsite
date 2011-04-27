from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from siyavula.app import _

class ISection(form.Schema):
    """A site section folder.
    """
    
    title = schema.TextLine(
            title=_(u"Title"),
        )
    
    description = schema.Text(
            title=_(u"A short summary"),
        )
    
    button = NamedImage(
            title=_(u"Button Image"),
            description=_(u"Image for the wide button."),
        )

    colour = schema.TextLine(
            title=_(u"Section colour in hex format, eg 23fe45"),
        )
    
    tagline = RichText(
            title=_(u"Tagline"),
            description=_(u"A small tagline, used next to the image at the top."),
        )
    
    content = RichText(
            title=_(u"Content"),
            description=_(u"A longer description. Used in the section page, if any. Also used if the section is one of the 3 displayed on the front page."),
        )
    
    header = NamedImage(
            title=_(u"Header Image"),
            description=_(u"An image displayed as a banner at the top of the section."),
        )

    display_on_frontpage = schema.Bool(
            title=_(u"Display On Frontpage"),
            description=_(u"Show the section as one of the 3 sections on the front page?"),
        )

class View(grok.View):
    grok.context(ISection)
    grok.require('zope2.View')

class BooksView(grok.View):
    grok.context(ISection)
    grok.require('zope2.View')
    grok.name('booksview')
