from five import grok
from Acquisition import aq_inner

from plone.memoize import view
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IContentish, ISiteRoot
from siyavula.app.section import ISection

class MainTemplateHelpers(grok.View):
    """Get some dynamic things we need in the main template."""
    
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('main-template-helpers')
    
    def render(self):
        """No-op to keep grok.View happy."""
        return ''

    def portal(self):
        """Return the portal object."""
        return aq_inner(self.context)

    @view.memoize
    def sections(self):
        """Get the sections in the portal root."""
        portal = self.portal()
        sections = portal.getFolderContents(
                {'portal_type':['Folder', 'siyavula.app.section']})
        excludes = ['news', 'events', 'Members']
        return [i.getObject() for i in sections if i.id not in excludes]
        
    @view.memoize
    def current_section(self, context=None):
        """If we are in the portal root, there is no current section."""
        return None

    @view.memoize
    def tagline_style(self):
        """Return a hex color string for styling the tagline."""
        section = self.current_section()
        if section and section.colour:
            return 'color:#%s;' % section.colour
        else:
            return 'color:#3096d3;'

    @view.memoize
    def books(self):
        """Get the books to show at the bottom of the page."""
        context = aq_inner(self.context)
        pc = getToolByName(context, 'portal_catalog')
        query = {'portal_type' : 'siyavula.app.book',
                 'review_state' : 'published',
                 'sort_on' : 'getObjPositionInParent',
                }
        brains = pc(query)
        return [brain.getObject() for brain in brains][:5]

    def books_blurb(self):
        """Return the editable blurb used at the bottom next to the books."""
        portal = self.portal()
        settings = portal.settings
        if not settings.books_blurb:
            return ''
        return settings.books_blurb.output

    def headers(self):
        """Return all available header images.

        Return all the available headers in a list, so that we can use the
        headers logic for normal page and the home page.

        """
        portal = self.portal()
        headers = []
        pc = getToolByName(portal, 'portal_catalog')
        query = {'portal_type' : 'siyavula.app.header',
                 'review_state' : 'published',
                 'sort_on' : 'getObjPositionInParent',
                }
        brains = pc(query)
        for brain in brains:
            ob = brain.getObject()
            if ob.header:
                headers.append(ob)

        return headers

class MainTemplateHelpersContent(MainTemplateHelpers):
    """Get some dynamic things we need in the main template."""
    
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('main-template-helpers')
    
    def portal(self):
        """Get the portal object."""
        context = aq_inner(self.context)
        return context.portal_url.getPortalObject()

    @view.memoize
    def current_section(self, context=None):
        """Return the current section, used to determine headers etc."""
        if not context:
            context = aq_inner(self.context)
        if ISection.providedBy(context):
            return context
        if ISiteRoot.providedBy(context):
            return None
        return self.current_section(context=context.__parent__)

    def headers(self):
        """Return the current section if it has a header image.

        Return just the current section in a list, so that we can use the
        headers logic for normal page and the home page.

        """
        section = self.current_section()
        if section and section.header:
            return [section]
        return []

class FrontPageView(grok.View):
    """Get some dynamic things we need in the front page template."""
    
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('frontpageview')

    def get_settings(self):
        """Get the site settings object."""
        return self.context.settings

    def banners(self):
        """ Return banners for rotating."""
        return []

    def features(self):
        """ Return featured sections."""
        settings = self.get_settings()
        return [settings.left_section.to_object if settings.left_section else None,
                settings.center_section.to_object if settings.center_section else None,
                settings.right_section.to_object if settings.right_section else None]


class MailForm(grok.View):
    """Mail things."""

    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('mailform')

    def render(self):
        """Mail the form contents."""
        mail_host = getToolByName(self.context, 'MailHost')
        portal_url = getToolByName(self.context, 'portal_url')
        portal = portal_url.getPortalObject()
        mail_to = portal.getProperty('email_from_address')
        if mail_to is None or len(mail_to) < 1:
            return 'An error has occurred. Please contact the site administrators.'

        mail_from = mail_to
        # get the basic mail settings and details
        mail_host = getToolByName(self.context, 'MailHost')

        # Compose email        
        subject = "Email form result"
        message = """The following email address asked to be included in your mailing list:
%s""" % self.context.REQUEST.get('email', 'No email')
                  
        # Send email
        mail_host.secureSend(message, mail_to, mail_from, subject=subject)
        return 'Your email was successfully submitted.'
