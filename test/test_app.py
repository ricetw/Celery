from unittest import mock

from . import BaseTestCase

from app import *
from tasks import *


class TestFlask(BaseTestCase):  # mock/assert多一些

    @mock.patch('tasks.add.delay')
    def test_post(self, mock_add):
        mock_add.return_value = AsyncResult(
            'a4155a5d-8d0a-43e3-804b-bcb674b36f7a', app=celery_app)
        response = self.client.post('/post', json={'x': 5, 'y': 5})
        self.assertEqual(mock_add.called, True)
        self.assertEqual(response.status_code, 200)

    @mock.patch('tasks.subtract.delay')
    def test_get(self, mock_subtract):
        mock_subtract.return_value = AsyncResult(
            'a4155a5d-8d0a-43e3-804b-bcb674b36f7a', app=celery_app)
        response = self.client.get('/get', query_string={'x': 5, 'y': 5})
        self.assertEqual(mock_subtract.called, True)
        self.assertEqual(response.status_code, 200)

    def test_get_task_info(self):
        response = self.client.get(
            '/get_task_info', query_string={'id': 'a4155a5d-8d0a-43e3-804b-bcb674b36f7a'})
        self.assertEqual(response.status_code, 200)


class TestCelery(BaseTestCase):

    def test_add(self):
        tasks = add.apply({'x': 5}, {'y': 5})
        self.assertEqual(tasks.status, "SUCCESS")

    def test_subtration(self):
        tasks = subtract.apply({'x': 5}, {'y': 5})
        self.assertEqual(tasks.status, "SUCCESS")

    def test_crontab_test(self):
        tasks = crontab_test.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_zero_oclock(self):
        tasks = zero_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_one_oclock(self):
        tasks = one_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_two_oclock(self):
        tasks = two_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_three_oclock(self):
        tasks = three_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_four_oclock(self):
        tasks = four_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_five_oclock(self):
        tasks = five_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_six_oclock(self):
        tasks = six_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_seven_oclock(self):
        tasks = seven_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_eight_oclock(self):
        tasks = eight_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_nine_oclock(self):
        tasks = nine_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_ten_oclock(self):
        tasks = ten_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_eleven_oclock(self):
        tasks = eleven_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_twelve_oclock(self):
        tasks = twelve_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_thirteen_oclock(self):
        tasks = thirteen_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_fourteen_oclock(self):
        tasks = fourteen_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_fifteen_oclock(self):
        tasks = fifteen_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_sixteen_oclock(self):
        tasks = sixteen_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_seventeen_oclock(self):
        tasks = seventeen_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_eighteen_oclock(self):
        tasks = eighteen_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_nineteen_oclock(self):
        tasks = nineteen_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_twenty_oclock(self):
        tasks = twenty_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_twenty_one_oclock(self):
        tasks = twenty_one_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_twenty_two_oclock(self):
        tasks = twenty_two_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")

    def test_twenty_three_oclock(self):
        tasks = twenty_three_oclock.apply()
        self.assertEqual(tasks.status, "SUCCESS")
