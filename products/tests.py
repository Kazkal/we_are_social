# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Product

# Create your tests here.
class PageTest(TestCase):

    def test_check_content_is_correct(self):
        product_page =self.client.get('/products/')
        self.assertTemplateUsed(product_page,"products/products.html")
        product_page_template_output = render_to_response("products/products.html",{'products':Product.objects.all()}).content
        self.assertEqual(product_page.content, product_page_template_output)