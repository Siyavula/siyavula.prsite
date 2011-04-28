from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from siyavula.app import _

class ISettings(form.Schema):
    """ Settings for the site. 
    """
    
    title = schema.TextLine(
            title=_(u"Title"),
        )
    
    description = schema.Text(
            title=_(u"A short summary"),
        )
    
class View(grok.View):
    grok.context(ISettings)
    grok.require('zope2.View')
