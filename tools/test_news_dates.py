import copy
import unittest
from news_dates import stamp


class RegistrationDates(unittest.TestCase):
    def test_new_entry_uses_korean_registration_month_and_stays_fixed(self):
        old = {'title': 'Existing', 'news_date': '2026-01'}
        new = {'title': 'New paper', 'url': 'https://doi.org/10.test/new', 'year': '2025', 'news_date': '2026-01'}
        edited = dict(new, title='Corrected paper title')
        history = [('2026-09-01T00:00:00+00:00', [old]),
                   ('2026-09-30T16:00:00+00:00', [old, new]),
                   ('2026-12-01T00:00:00+00:00', [old, edited])]
        data = stamp({'journal': [copy.deepcopy(old), copy.deepcopy(edited)]}, history, [old])
        self.assertEqual(data['journal'][0]['news_date'], '2026-01')
        self.assertEqual(data['journal'][1]['news_date'], '2026-10')
        self.assertEqual(data['journal'][1]['news_added_at'], '2026-10-01T01:00:00+09:00')
        again = stamp(copy.deepcopy(data), history + [('2027-01-01T00:00:00+00:00', [old, edited])], [old])
        self.assertEqual(data, again)

    def test_existing_undated_papers_are_not_announced_as_new(self):
        old = {'title': 'Old paper', 'url': 'https://doi.org/old'}
        changed = dict(old, title='Old paper corrected')
        data = stamp({'journal': [changed]}, [('2026-09-01T00:00:00+00:00', [old]), ('2026-10-01T00:00:00+00:00', [changed])], [old])
        self.assertNotIn('news_date', data['journal'][0])

    def test_uncommitted_paper_does_not_get_a_guessed_date(self):
        with self.assertRaises(ValueError):
            stamp({'journal': [{'title': 'Uncommitted'}]}, [], [])


if __name__ == '__main__':
    unittest.main()
