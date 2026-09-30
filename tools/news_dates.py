"""Derive new journal registration dates from immutable repository history."""
import datetime as dt
import json
import pathlib
import subprocess
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
KST = dt.timezone(dt.timedelta(hours=9))


def keys(paper):
    result = set()
    for field in ('id', 'url', 'title'):
        value = paper.get(field)
        if value:
            value = ' '.join(unicodedata.normalize('NFKC', str(value)).split()).casefold().rstrip('/')
            result.add(field + ':' + value)
    return result


def history(root):
    def git(*args):
        return subprocess.check_output(['git', '-C', str(root), *args], encoding='utf-8')
    revisions = git('log', '--first-parent', '--reverse', '--format=%H %cI', '--', 'docs/content.json')
    for line in revisions.splitlines():
        sha, timestamp = line.split(' ', 1)
        result = subprocess.run(['git', '-C', str(root), 'show', sha + ':docs/content.json'], capture_output=True, encoding='utf-8')
        if result.returncode:
            continue  # A historical deletion has no records to register.
        yield timestamp, json.loads(result.stdout).get('journal', [])


def stamp(data, snapshots, baseline):
    legacy = set().union(*(keys(p) for p in baseline))
    seen = {}
    for timestamp, records in snapshots:
        timestamp = dt.datetime.fromisoformat(timestamp).astimezone(KST).isoformat()
        for paper in records:
            aliases = keys(paper)
            first = min([timestamp] + [seen[k] for k in aliases if k in seen])
            if aliases & legacy:
                legacy.update(aliases)
            for alias in aliases:
                seen[alias] = first
    for paper in data['journal']:
        aliases = keys(paper)
        if aliases & legacy:
            continue  # Preserve the existing site's historical news dates.
        dates = [seen[k] for k in aliases if k in seen]
        if not dates:
            raise ValueError('Journal entry must be committed before deployment: ' + paper['title'])
        added = dt.datetime.fromisoformat(min(dates)).astimezone(KST)
        paper['news_added_at'] = added.isoformat()
        paper['news_date'] = added.strftime('%Y-%m')
        paper['news_date_source'] = 'journal_registration_month'
    return data


if __name__ == '__main__':
    path = ROOT / 'docs/content.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    baseline = json.loads((ROOT / 'tools/journal_baseline.json').read_text(encoding='utf-8'))
    stamp(data, history(ROOT), baseline)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Journal registration months resolved from Git history (Asia/Seoul).')
