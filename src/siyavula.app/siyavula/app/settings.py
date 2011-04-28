from five import grok
from zope import schema

from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage
from siyavula.app.section import ISection

from siyavula.app import _

class ISettings(form.Schema):
    """ Settings for the site. 
    """
    
    title = schema.TextLine(
            title=_(u"Title"),
        )
    
    left_section = RelationChoice(
            title=_(u"Left featured section"),
            source=ObjPathSourceBinder(object_provides=ISection.__identifier__),
            required=False,
            )

    center_section = RelationChoice(
            title=_(u"Center featured section"),
            source=ObjPathSourceBinder(object_provides=ISection.__identifier__),
            required=False,
            )

    right_section = RelationChoice(
            title=_(u"Right featured section"),
            source=ObjPathSourceBinder(object_provides=ISection.__identifier__),
            required=False,
            )

    books_blurb = RichText(
            title=_(u"Books Blurb"),
            description=_(u"The blurb (Text) displayed to the right of the book thumbnails in the footer."),
            required=False,
        )

class View(grok.View):
    grok.context(ISettings)
    grok.require('zope2.View')
