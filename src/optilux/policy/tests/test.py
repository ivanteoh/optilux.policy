import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from optilux.policy.testing import\
    OPTILUX_POLICY_INTEGRATION_TESTING


class TestSetup(unittest.TestCase):

    layer = OPTILUX_POLICY_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
    
    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        pid = 'optilux.policy'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')
                        
    def test_portal_title(self):
        portal = self.layer['portal']
        self.assertEqual(
          "Optilux Cinemas",
        portal.getProperty('title')
    )

    def test_portal_description(self):
        portal = self.layer['portal']
        self.assertEqual(
            "Welcome to Optilux Cinemas",
            portal.getProperty('description')
        )

    def test_role_added(self):
        portal = self.layer['portal']
        self.assertTrue("StaffMember" in portal.validRoles())

    def test_workflow_installed(self):
        portal = self.layer['portal']
        workflow = getToolByName(portal, 'portal_workflow')
        self.assertTrue('optilux_sitecontent_workflow' in workflow)

    def test_workflows_mapped(self):
        portal = self.layer['portal']
        workflow = getToolByName(portal, 'portal_workflow')
        self.assertEqual(('optilux_sitecontent_workflow',),
        workflow.getDefaultChain())

    def test_view_permisison_for_staffmember(self):
        portal = self.layer['portal']
        self.assertTrue('View' in [r['name']
            for r in portal.permissionsOfRole('Reader')
            if r['selected']])
        self.assertTrue('View' in [r['name']
            for r in portal.permissionsOfRole('StaffMember')
            if r['selected']])

    def test_staffmember_group_added(self):
        portal = self.layer['portal']
        acl_users = portal['acl_users']
        self.assertEqual(1,
            len(acl_users.searchGroups(name='Staff')))
            
    def test_PloneFormGen_installed(self):
        portal = self.layer['portal']
        portal_types = getToolByName(portal, 'portal_types')
        self.assertTrue("FormFolder" in portal_types)


