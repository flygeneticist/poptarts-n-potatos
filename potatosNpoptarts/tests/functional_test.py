from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

"""
    TESTS COVERING GENERAL SITE FUNCTIONALITY ACROSS ALL PAGES
"""
# site should have the correct title shown in the browser
assert 'Poptarts-n-Potatos' in browser.title

# pages should display the blog logo

# logo should link to the home page

# footer element present with contact info, nav links, copywrite, etc...

"""
    TESTS COVERING THE BLOG HOME PAGE
"""
# post item should be shown with a title, as a link, plus a short summary

# there should be a maximum of 10 posts per page, starting with the most recent

# if there are more than 10 posts additonal posts a link should appear at the bottom
# of the page directing the users to "Older Posts" and/or "Newer Posts"

# clicking a post's title should send the user to the full page for that post

"""
    TESTS COVERING A BLOG POST PAGE
"""
# post page should have a title at tte top

# post page should have the post's content displayed after the title

# post page should allow users to comment at the bottom

"""
    TESTS COVERING THE COMMENT SYSTEM
"""
# comment can have only one author

# author is lowest level user (email only required)

# comment must belong to a blog post

# comment may also belong to another comment

# comments from new authors will not show until the author is approved/activatd by an admin

# comments should show immediately if author is approved

# admin should receive a notification(email / dashboard) after a comment is sumbitted

"""
    TESTS COVERING THE ADMIN DASHBOARD
"""
# Navigating to the admin page should show a login form if user is not signed in / authorized

# If a login is successful the user should be re-directed to the an admin dasboard page

# admin page should have a two tabs "Users" and "Posts"

# admin page should load with the "Posts" tab shown

# button to create a new post should be shown to authorized users in the nav bar

# button to create a new user should be shown to authorized users in the nav bar

# button to logout of dashboard shown in the nav bar
