from django.test import TestCase

from account.tests.factories.make_user import make_user


class UserTestCase(TestCase):

    def test_create_tutor(self):
        user = make_user({'role': 1})

        self.assertEqual(user.role, 1)
        self.assertTrue(user.tutor)

    def test_create_organization_member(self):
        user = make_user({'role': 2})

        self.assertEqual(user.role, 2)
        self.assertTrue(user.organization)

    def test_switch_relation_on_new_role(self):
        user = make_user({'role': 1})
        self.assertEqual(user.role, 1)
        self.assertTrue(user.tutor)

        user.role = 2
        user.save()

        self.assertEqual(user.role, 2)
        self.assertTrue(user.organization)

        user.role = 1
        user.save()

        self.assertEqual(user.role, 1)
        self.assertTrue(user.tutor)
