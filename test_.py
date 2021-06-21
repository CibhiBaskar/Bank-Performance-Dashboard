#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest

from app import app

class BasicTestCase(unittest.TestCase):
    
    # Ensure that Flask was set up correctly
    
    def test_dashboard_page_content(self):
        tester = app.test_client(self)
        response = tester.get('/dashboard','/predict', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_predict_page_content(self):
        tester = app.test_client(self)
        response = tester.get('/predict', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_content(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Please Login' in response.data)

    # Ensure that main page requires user login
    
    def test_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Please Login' in response.data)
        
    # Ensure login behaves correctly given correct credentials
    
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/',
                               data=dict(username="Cibhi", password="cibhi123"),
                               follow_redirects=True
                              )
        self.assertIn(b'Welcome back, Cibhi!', response.data)
        
    # Ensure login behaves correctly given wrong credentials
    
    def test_wrong_login(self):
        tester = app.test_client(self)
        response = tester.post('/',
                               data=dict(username="test", password="test123"),
                               follow_redirects=True
                              )
        self.assertIn(b'Please Login', response.data)
        
    # Ensure logout behaves correctly after login
        
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/',
                    data=dict(username="Cibhi", password="cibhi123"),
                    follow_redirects=True
            )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'Please Login', response.data)


# In[2]:


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




