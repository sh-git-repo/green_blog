from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Blog

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username='test',
                email='test@test.com',
                password='pwd'
        )

        self.post = Blog.objects.create(
                title='Wonderful',
                message='Bagban.',
                usr=self.user
        )

    def test_title(self):
        b_obj = Blog(title='Sample')
        self.assertEqual(str(b_obj), b_obj.title)

    def test_main(self):
        self.assertEqual(f'{self.post.title}', 'Wonderful')
        self.assertEqual(f'{self.post.message}', 'Bagban.')
        self.assertEqual(f'{self.post.usr}', 'test')

    def test_home_view(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bagban.')
        self.assertTemplateUsed(response, 'blog_home.html')

    def test_detail_view(self):
        response=self.client.get('/msg/1/')
        no_response=self.client.get('/msg/1111/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response,'Wonderful')
        self.assertTemplateUsed(response,'blog_detail.html')
    
    def test_about_view(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Us.')
        self.assertTemplateUsed(response, 'blog_about.html')

# Create your tests here.
