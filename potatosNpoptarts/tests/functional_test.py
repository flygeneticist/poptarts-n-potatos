from selenium import webdriver
import unittest as ut

# setup and tear down functions in parent class to keep code dry
class SiteLayoutMasterTest(ut.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    """
    TESTS COVERING GENERAL SITE FUNCTIONALITY
    """
    def test_basic_site_layout_present(self): #
        # blog title should be shown for all pages
        self.assertIn('Potatos-n-Poptarts', browser.title)
        # pages should display the blog logo
        self.assertIn('a img #logo', browser.body)
        # logo should link to the home page
        self.assertIn('a img #logo', browser.body)
        # footer element present with contact info, nav links, copywrite, etc...
        self.assertIn('footer', browser.body)


class NewVisitorToHomeTest(MasterTest):
    """
        TESTS COVERING THE BLOG HOME PAGE
    """
    def test_can_open_home_page(self):
        assert self.browser.get('http://localhost:8000/')

    # post items should be shown with a title, as a link, plus a short summary

    # there should be a maximum of 10 posts per page, starting with the most recent

    # if there are more than 10 posts additonal posts a link should appear at the bottom
    # of the page directing the users to "Older Posts" and/or "Newer Posts"

    # clicking a post's title should send the user to the full page for that post


class NewVisitorToPostTest(MasterTest):
    """
        TESTS COVERING A BLOG POST PAGE
    """
    def test_can_open_valid_post_page(self):
        assert self.browser.get('http://localhost:8000/testPost')

    def test_open_non_valid_post_returns_404(self):
        assertEquals(self.browser.get('http://localhost:8000/bustedPost'), self.browser.get('http://localhost:8000/404'))

    # post page should have a title at tte top

    # post page should have the post's content displayed after the title

    # post page should allow users to comment at the bottom


class CommentSystemTest(MasterTest):
    """
        TESTS COVERING THE COMMENT SYSTEM
    """
    pass
    # comment can have only one author

    # author is lowest level user (email only required)

    # comment must belong to a blog post

    # comment may also belong to another comment

    # comments from new authors will not show until the author is approved/activatd by an admin

    # comments should show immediately if author is approved

    # admin should receive a notification(email / dashboard) after a comment is sumbitted


class AdminDashboardTest(MasterTest):
    """
        TESTS COVERING THE ADMIN DASHBOARD
    """
    pass
    # Navigating to the admin page should show a login form if user is not signed in / authorized

    # If a login is successful the user should be re-directed to the an admin dasboard page

    # admin page should have a two tabs "Users" and "Posts"

    # admin page should load with the "Posts" tab shown

    # button to create a new post should be shown to authorized users in the nav bar

    # button to create a new user should be shown to authorized users in the nav bar

    # button to logout of dashboard shown in the nav bar


if __name__ == '__main__': #
    unittest.main(warnings='ignore')

