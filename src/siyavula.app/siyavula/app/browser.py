from five import grok
from Acquisition import aq_inner

from plone.memoize import view
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IContentish, ISiteRoot

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

    @view.memoize
    def sections(self):
        context = aq_inner(self.context)
        portal = context.portal_url.getPortalObject()
        sections = portal.getFolderContents({'portal_type':'siyavula.app.section'})
        return [i.getObject() for i in sections]
        
    @view.memoize
    def books(self):
        """Get the message representation of the context
        """
        context = aq_inner(self.context)
        portal = context.portal_url.getPortalObject()
        pc = getToolByName(context, 'portal_catalog')
        query = {'portal_type' : 'siyavula.app.book',
                 'review_state' : 'published',
                 'sort_on' : 'getObjPositionInParent',
                }
        brains = pc(query)
        return [brain.getObject() for brain in brains][:5]

    def books_blurb(self):
        context = aq_inner(self.context)
        portal = context.portal_url.getPortalObject()
        settings = portal.settings
        return settings.books_blurb.output

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
