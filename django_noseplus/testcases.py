# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

import re
caps = re.compile('([A-Z])')

def pep8(name):
    return caps.sub(lambda m: '_' + m.groups()[0].lower(), name)

class Pep8TestCase(object):
    """Mixin to do proper names
    USAGE: class ProperTest(testcases.Pep8TestCase, FastFixtureTestCase):
    """

    def __init__(self, *args, **kwargs):
        """Dynamic monkey patchin
        """

        ## Basic cleanups
        ats = [at for at in dir(self)
                if at.startswith('assert') and not '_' in at]

        for at in ats:
            setattr(self, pep8(at), getattr(self, at))

        ## Setup and teardown
        if hasattr(self, 'setup'):
            self.setUp = self.setup

        if hasattr(self, 'teardown'):
            self.tearDown = self.teardown

        return super(Pep8TestCase, self).__init__(*args, **kwargs)


class ExpandedTestCase(object):
    """Mixin for additional cool methods
    Use javaCaps because unittest uses them, recommended use with Pep8TestCase
    """

    def assertCode(self, response, status_code, msg_prefix=''):
        """Asserts the response was returned with the given status code
        """

        if msg_prefix:
            msg_prefix = '%s: ' % msg_prefix

        assert response.status_code == status_code, \
            'Response code was %d (expected %d)' % \
                (response.status_code, status_code)

    def assertOk(self, response, msg_prefix=''):
        """Asserts the response was returned with status 200 (OK)
        """

        return self.assertCode(response, 200, msg_prefix=msg_prefix)

    def assertMailCount(self, count, msg=None):
        """Assert the number of emails sent.
        The message here tends to be long, so allow for replacing the whole
        thing instead of prefixing.
        """

        from django.core import mail

        if msg is None:
            msg = ', '.join([e.subject for e in mail.outbox])
            msg = '%d != %d %s' % (len(mail.outbox), count, msg)
        assert_equals(len(mail.outbox), count, msg)


class TestCaseMixin(Pep8TestCase, ExpandedTestCase):
    """Combine the test cases as a shortcut
    """

    pass


def create_functions(klass, d):
    """Create test functions from klass; you want to inherit from TestCase
    d is the destination dictionary; you want to pass globals()
    """

    class Dummy(klass):
        def nop(self):
            pass

    dummy = Dummy('nop')

    ats = [at for at in dir(dummy)
            if at.startswith('assert') and not '_' in at]

    for at in ats:
        pepd = pep8(at)
        d[pepd] = getattr(dummy, at)

# EOF

