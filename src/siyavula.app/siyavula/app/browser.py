from five import grok
from Acquisition import aq_inner

from plone.memoize import view
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IContentish, ISiteRoot
from siyavula.app.section import ISection

class MainTemplateHelpers(grok.View):
    """Get some dynamic things we need in the main template.
    """
    
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('main-template-helpers')
    
    def render(self):
        """No-op to keep grok.View happy
        """
        return ''

    def portal(self):
        return aq_inner(self.context)

    @view.memoize
    def sections(self):
        portal = self.portal()
        sections = portal.getFolderContents({'portal_type':'siyavula.app.section'})
        return [i.getObject() for i in sections]
        
    @view.memoize
    def current_section(self, context=None):
        return None

    @view.memoize
    def tagline_style(self):
        section = self.current_section()
        if section and section.colour:
            return 'color:#%s;' % section.colour
        else:
            return 'color:#3096d3;'

    @view.memoize
    def books(self):
        """Get the books.
        """
        context = aq_inner(self.context)
        pc = getToolByName(context, 'portal_catalog')
        query = {'portal_type' : 'siyavula.app.book',
                 'review_state' : 'published',
                 'sort_on' : 'getObjPositionInParent',
                }
        brains = pc(query)
        return [brain.getObject() for brain in brains][:5]

    def books_blurb(self):
        portal = self.portal()
        settings = portal.settings
        return settings.books_blurb.output

    def headers(self):
        """
        Return all the available headers in a list, so that we can use the
        headers logic for normal page and the home page.
        """
        portal = self.portal()
        settings = portal.settings
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
    """Get some dynamic things we need in the main template.
    """
    
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('main-template-helpers')
    
    def portal(self):
        context = aq_inner(self.context)
        return context.portal_url.getPortalObject()

    @view.memoize
    def current_section(self, context=None):
        if not context:
            context = aq_inner(self.context)
        if ISection.providedBy(context):
            return context
        if ISiteRoot.providedBy(context):
            return None
        return self.current_section(context=context.__parent__)

    def headers(self):
        """
        Return just the current section in a list, so that we can use the
        headers logic for normal page and the home page.
        """
        section = self.current_section()
        if section and section.header:
            return [section]
        return []

class FrontPageView(grok.View):
    """Get some dynamic things we need in the main template.
    """
    
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('frontpageview')

    def get_settings(self):
        return self.context.settings

    def banners(self):
        """ Return banners for rotating """
        return []

    def features(self):
        """ Return featured sections"""
        settings = self.get_settings()
        return [settings.left_section.to_object,
                settings.center_section.to_object,
                settings.right_section.to_object]
