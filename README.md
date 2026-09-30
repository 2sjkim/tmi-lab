# TMI Lab · Yonsei University

기존 TMI 홈페이지의 정보를 옮긴 GitHub Pages용 정적 홈페이지입니다. 별도 서버나 유료 서비스 없이 운영할 수 있습니다.

## 미리보기

프로젝트 폴더에서 `python -m http.server 8765 --directory docs`를 실행하고 http://localhost:8765 에 접속합니다.

## GitHub Pages 공개

1. 사용할 GitHub 저장소에 이 폴더의 내용을 업로드합니다.
2. 저장소의 **Settings → Pages**에서 **GitHub Actions**를 선택합니다.
3. `main`에 저장하면 **Publish lab website**가 날짜 계산, 페이지 생성, 배포를 자동 실행합니다.
4. Pages 화면에 표시되는 공개 주소를 확인합니다.

사용자/조직 대표 홈페이지는 `계정명.github.io` 저장소를, 일반 프로젝트 홈페이지는 원하는 저장소 이름을 사용하면 됩니다. 모든 내부 경로가 상대경로이므로 두 형태를 모두 지원합니다.

## 구성

- Home: 연구실 소개, 연구 방향, 최근 논문, 연락처
- Research: 기존 홈페이지에 공개된 세 가지 연구 방향
- People: 교수 소개, 연구원 18명, 직원 1명, 졸업생 10명
- Publications: Journal 68편, Conference 94건, 연도별 목록
- Patents: 28건
- Join Us: 연구 주제, 관심 분야, 지원 연락처

## 수정

- 논문·구성원·교수 소개: `docs/content.json`
- 홈페이지 문구와 페이지 구성: `tools/build.py`
- 디자인: `docs/style.css`
- 메뉴 동작: `docs/site.js`

원본 데이터나 페이지 구성을 수정해 `main`에 저장하면 자동으로 HTML을 생성해 배포합니다. 로컬 미리보기는 `python tools/build.py`로 생성하며 Python 표준 라이브러리만 필요합니다.

### Automatic Journal and Recent News updates

Add a paper to `journal` in `docs/content.json` and save to main. GitHub Actions builds and deploys both Journal and Home. Home shows the latest three registrations, even if a newly added paper has an older publication year.

Provide `title`, `authors`, `venue`, `year` (string), and `links`; optionally add `url` and `journal_name`. No manual `news_date` is needed. The first commit containing the paper determines its registration month in Korea (UTC+9), displayed as `Sep. 2026`. Rebuilding in a later month or editing the title does not reset it. This is a registration month, not a verified acceptance/publication date.

`tools/news_dates.py` reads full Git history and stamps deployment data. Paper identity is matched by `id`, `url`, or normalized `title`. Before changing both title and URL together, first add and commit a stable `id`. `tools/journal_baseline.json` preserves existing papers and their historical news dates; do not add new papers to this baseline.

`.github/workflows/pages.yml` builds and deploys with Pages Source set to GitHub Actions. Computed dates are written to the deployed JSON, without a write-back commit to main. For a local deployment-equivalent build in a full Git checkout, run `python tools/news_dates.py` then `python tools/build.py`. Edit the shared JSON rather than generated HTML, which is regenerated on deployment.

## 자료 기준과 검증

2026-09-29 공개된 https://sites.google.com/view/yonsei-medisyslab/ 의 9개 페이지를 기준으로 이름, 연구 주제, 연락처, 논문, 특허를 보존했습니다. 사진과 로고는 기존 TMI 자료를 로컬 파일로 저장했습니다. 원본에 사진이 없는 Hwanhee Cho와 Eunyoung Ahn은 이니셜로 표시합니다. 본문의 명백한 철자와 대소문자 오류만 정리했습니다.

로고와 본문의 TMI 명칭은 Translational Medical Intelligence로 통일했습니다. 로고는 `docs/assets/tmi-logo-intelligence.png`이며 사이트 강조색은 #14319C입니다.

https://kaist-cvml.github.io/index.html 의 흰 배경, 간결한 메뉴, 제목 구성, 강조색 배치를 참고했습니다. KAIST의 로고, 인물, 연구 성과는 사용하지 않았습니다.

원본 홈페이지의 특허 번호, 영문 성명 표기, 논문 분류를 그대로 유지했으며 별도의 서지 사실 검증이나 수정은 하지 않았습니다. 예를 들어 원문 Journal에 기재된 ICLR 항목도 해당 분류를 유지합니다.

이 패키지는 게시 준비가 완료된 소스입니다. GitHub 계정·대상 저장소가 지정되기 전에는 인터넷에 공개되지 않습니다.
