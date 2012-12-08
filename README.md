django-noseplus
===============

Some addons for django-nose

Install ``django_nose`` in ``INSTALLED_APPS``

Best results should come with:

	from django_nose.testcases import FastFixtureTestCase
	from django_noseplus.testcases import TestCaseMixin

	class FooTest(TestCaseMixin, FastFixtureTestCase):
		...

Now you can use pep8-compliant names and methods such as ``self.assert_ok(res)``

