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
