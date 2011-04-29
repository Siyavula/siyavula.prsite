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
            description=_(u"Image for the wide button with the section name."),
            required=False,
        )

    tagline = schema.TextLine(
            title=_(u"Tagline"),
            description=_(u"A small tagline, used next to the button image at the top."),
            required=False,
        )
    
    colour = schema.TextLine(
            title=_(u"Tagline colour"),
            description=_(u"The tagline colour, in Hex. eg: 34FE56"),
            required=False,
        )
    
    header = NamedImage(
            title=_(u"Header Image"),
            description=_(u"An image displayed as a banner at the top of the section."),
            required=False,
        )

    headerblurb = RichText(
            title=_(u"Header Blurb"),
            description=_(u"The blurb (Text) displayed on top of the header image, if any. Recommended styles: H2 and normal text."),
            required=False,
        )

    content = RichText(
            title=_(u"Content"),
            description=_(u"A longer description. Used in the section page, if any. Also used if the section is one of the 3 displayed on the front page."),
            required=False,
        )
    
    embed_code = schema.Text(
            title=_(u"Youtube embed code"),
            description=_(u"Youtube embed code for a video for this section. Only use a 280 pixel wide code."),
            required=False,
        )

    form_embed_code = schema.Text(
            title=_(u"Form embed code"),
            description=_(u"Form embed code. This is to be used with the form layout."),
            required=False,
        )

class View(grok.View):
    grok.context(ISection)
    grok.require('zope2.View')

    def tagline_style(self):
        colour = self.context.colour
        if colour:
            return 'color:#%s;' % colour
        else:
            return 'color:#3096d3;'

    def posts(self):
        brains = self.context.getFolderContents({'portal_type': 'siyavula.app.post'})
        return [brain.getObject() for brain in brains]


class BooksView(View):
    grok.name('booksview')

    def books(self):
        brains = self.context.getFolderContents({'portal_type': 'siyavula.app.book'})
        return [brain.getObject() for brain in brains]

class CoursesView(View):
    grok.name('coursesview')

class FormView(View):
    grok.name('formview')

class BlogView(View):
    grok.name('blogview')

    def posts(self):
        brains = self.context.getFolderContents({'portal_type': 'siyavula.app.post', 'sort_on': 'created', 'sort_order': 'reverse'})
        return [brain.getObject() for brain in brains]

