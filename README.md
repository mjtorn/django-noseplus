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

	create_functions(FooTest, globals())

Now you can use pep8-compliant names and methods such as ``self.assert_ok(res)``
in your test case.

Calling create_functions sets the methods as functions into the global namespace
so you can do tests without a test case class doing teardown and setup between
tests.

