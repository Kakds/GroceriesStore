import unittest
from services.ReportGenerator import generate_reports

class TestReports(unittest.TestCase):
    def test_generate_random_report_id_type(self):
        report_id = generate_random_report_id()

        self.assertIsInstance(report_id, int)

    def test_generate_random_report_id_range(self):
        report_id = generate_random_report_id()

        self.assertTrue(0 <= report_id < 10000)
