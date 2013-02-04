django-noseplus
===============

Some addons for django-nose

Install ``django_nose`` in ``INSTALLED_APPS``

Best results should come with:

	from django_nose.testcases import FastFixtureTestCase
	from django_noseplus.testcases import TestCaseMixin
  from django_noseplus.testcases import create_functions

	class FooTest(TestCaseMixin, FastFixtureTestCase):
		pass

  create_functions(TestCase, globals())

Now you can use pep8-compliant names and methods such as ``self.assert_ok(res)``

