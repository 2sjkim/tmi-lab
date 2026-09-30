# TMI Lab Website

**Translational Medical Intelligence Lab · Yonsei University**  
[홈페이지](https://yonsei-tmi.github.io/) · [내용 편집](docs/content.json) · [게시 상태](https://github.com/yonsei-tmi/yonsei-tmi.github.io/actions)

연구실 구성원을 위한 홈페이지 편집 안내입니다. 논문, 구성원, 뉴스는 주로 `docs/content.json`에서 관리합니다. 변경사항을 게시하려면 저장소 쓰기 권한이 필요합니다.

## 빠르게 수정하기

1. [docs/content.json](docs/content.json)을 열고 연필 아이콘 **Edit this file**을 누릅니다.
2. 해당 항목을 찾아 수정합니다. 새 항목은 같은 목록의 기존 항목을 복사해 추가하면 편합니다.
3. **Commit changes**에서 변경 내용을 적고 저장합니다. `main`에 저장되거나 변경사항이 병합되면 자동 게시가 시작됩니다.
4. [Actions](https://github.com/yonsei-tmi/yonsei-tmi.github.io/actions)의 **Publish lab website**에서 최신 실행의 성공 여부를 확인하고 홈페이지를 새로고침합니다.

여러 파일을 함께 고칠 때는 한 브랜치에서 수정한 뒤 하나의 Pull Request로 `main`에 병합하는 것을 권장합니다. 서로 의존하는 파일을 따로 저장하면 중간 상태에서 검사가 실패할 수 있습니다.

**`docs/index.html`, `docs/journal.html` 등 HTML 파일을 직접 수정하지 마세요.** 게시할 때 원본 데이터와 `tools/build.py`로 다시 생성되므로 직접 수정한 내용은 덮어써집니다.

## 무엇을 어디에서 수정하나요?

| 수정할 내용 | 파일 / 항목 |
| --- | --- |
| Journal / Conference / Patents | [docs/content.json](docs/content.json)의 `journal` / `conference` / `patents` |
| 수상·행사 등 수동 Recent News | 같은 파일의 `news` |
| Researchers / Alumni | 같은 파일의 `researchers` / `alumni` |
| 교수님 소개·경력·학력 | 같은 파일의 `professor` |
| 교수님 사진 | 같은 파일의 `images.professor` 첫 번째 경로 |
| Home 소개, Research, Join Us 문구·주소 | [tools/build.py](tools/build.py)의 해당 페이지 생성 부분 |
| 교수님 이름·직함·소속·연락처·Scholar 링크 | `tools/build.py`의 `profile` 부분 |
| 색상·글씨 크기·간격·모바일 배치·Home 배경 | [docs/style.css](docs/style.css) |
| 사진과 로고 파일 | [docs/assets](docs/assets) |

## Recent News 편집하기

### 표시 규칙

- **Journal 자동 소식 + `news`의 수동 소식**을 합쳐 최신 **5개**만 표시합니다.
- Conference와 Patents는 Home에 자동 추가되지 않습니다. 알리고 싶다면 `news`에 직접 입력합니다.
- `news_date`는 표시 날짜입니다. `2026-09`를 입력하면 **Sep. 2026**으로 표시됩니다.
- 정렬에는 `news_added_at`이 우선 사용됩니다. 없으면 `news_date`의 해당 월 1일을 기준으로 정렬합니다. 같은 달의 순서를 명확히 하려면 `news_added_at`도 입력하세요.
- 6번째 이후 소식은 데이터에 남지만 Home에는 표시되지 않습니다. 새 소식을 올릴 때 오래된 항목을 삭제할 필요는 없습니다.

### 수상·행사 소식을 수기로 추가하기

`docs/content.json`의 **기존 `news` 배열 안에** 아래처럼 항목을 추가합니다. 다음은 현재 수상 소식의 형식입니다. 이미 등록된 항목을 중복 추가하지 말고 새 소식에 맞게 바꾸세요.

```json
{
  "id": "yoonha-eo-bite2text-2026",
  "news_date": "2026-09",
  "news_added_at": "2026-09-30T00:00:00+09:00",
  "segments": [
    { "text": "Congratulations! " },
    { "text": "Yoonha Eo", "bold": true },
    { "text": " won the " },
    {
      "text": "Second Place Award",
      "bold": true,
      "color": "red",
      "url": "https://odin2026.grand-challenge.org/challenge-winners/"
    },
    { "text": " in Bite2Text challenge at " },
    {
      "text": "MICCAI 2026, ODIN Workshop",
      "bold": true,
      "url": "https://odin-workshops.org/2026/"
    },
    { "text": "." }
  ]
}
```

| 항목 | 입력 방법 |
| --- | --- |
| `id` | 소식마다 다른 영문 식별자. 제목을 수정해도 유지합니다. |
| `news_date` | 표시할 월 `YYYY-MM` 또는 날짜 `YYYY-MM-DD`. 화면에는 영문 월·연도로 표시됩니다. |
| `news_added_at` | 정렬 기준 시점. 예: `2026-09-30T09:00:00+09:00`. `+09:00`은 한국 시간입니다. 날짜를 바꿀 때 이 값도 확인하세요. |
| `segments` | 순서대로 이어 붙일 문장 조각의 목록 |
| `text` | 표시할 글자. 조각 사이의 공백도 직접 넣습니다. |
| `bold` | `true`이면 볼드체. 기본 강조 색상은 논문 제목과 같은 진한 색입니다. |
| `color` | 빨간 강조가 필요할 때만 `"red"`를 넣습니다. |
| `url` | 링크가 필요할 때만 전체 `https://...` 주소를 넣습니다. 밑줄은 항상 표시됩니다. |

강조가 없는 소식은 `"segments": [{ "text": "Your news sentence." }]`처럼 한 조각으로 작성하면 됩니다. `text` 안에 `**볼드체**`나 `<strong>` 같은 Markdown/HTML을 넣지 말고 위 속성을 사용하세요.

기존 소식은 해당 `id`를 찾아 `segments`와 날짜를 수정합니다. 삭제하려면 `news`에서 해당 `{ ... }` 항목을 제거하고 앞뒤 쉼표를 정리합니다.

### Journal 자동 소식의 내용과 날짜 수정하기

자동 문구는 다음 형식입니다.

> The paper "논문 제목" is accepted to 저널명.

논문 제목은 `journal`의 `title`, 저널명은 `journal_name`을 사용합니다. `journal_name`이 없으면 `venue`의 첫 쉼표 앞부분을 사용합니다. 이 필드를 수정하면 Home에도 함께 반영됩니다.

| 대상 | 날짜 처리 |
| --- | --- |
| 새로 추가하는 Journal | 처음 저장된 시점의 **한국 시간 기준 월**을 자동 입력합니다. 나중에 다시 게시해도 최초 등록 월을 유지합니다. |
| 사이트에 이미 있던 기존 Journal | 확인한 **실제 출판 월**을 `news_date`에 입력하고 `news_date_source`를 `"publication_month"`로 기록합니다. |
| 수동 `news` 소식 | 작성자가 `news_date`와 필요 시 `news_added_at`을 직접 정합니다. |

기존 논문의 날짜 필드 예시:

```json
{
  "news_date": "2025-07",
  "news_date_source": "publication_month",
  "publication_date_reference": "https://pubmed.ncbi.nlm.nih.gov/40570896/"
}
```

위 세 필드는 **해당 논문 객체 안에 추가할 필드**이며 논문 항목 전체를 대체하는 예시가 아닙니다. 출판 월은 출판사·DOI 페이지 또는 PubMed 등에서 확인하세요. 게시 시스템이 인터넷에서 출판 월을 자동 검색하지는 않습니다.

새 Journal의 `news_date`와 `news_added_at`은 게시 과정에서 자동 계산되므로 수동으로 바꿔도 덮어써집니다. 기존 논문 여부는 `tools/journal_baseline.json`으로 구분합니다. 이 파일에는 새 논문을 추가하지 마세요.

자유로운 문장의 논문 소식은 `news`에 작성할 수 있지만, **자동 소식과 수동 소식은 중복 제거되지 않습니다.** 같은 논문을 양쪽에 등록하면 두 번 표시될 수 있습니다. 현재 자동 소식의 개별 숨김 기능은 없습니다. 자동 문구 수정은 논문 필드에서, 독립적인 소식 추가는 `news`에서 하는 방식으로 운영합니다.

## Journal / Conference / Patents 추가하기

해당 배열에서 **최신 항목을 위에** 놓고 이전 연도 항목은 같은 연도 묶음에 넣습니다.

```json
{
  "id": "journal-your-paper-2026",
  "year": "2026",
  "title": "Your paper title",
  "authors": "Author One, Author Two, Jongduk Baek",
  "venue": "Journal Name, 2026",
  "journal_name": "Journal Name",
  "url": "https://doi.org/your-doi",
  "links": []
}
```

- 위 예시는 `journal`용입니다. 실제 내용으로 바꾸세요. `year`는 숫자가 아닌 **문자열 `"2026"`**으로 입력합니다.
- `title`, `authors`, `venue`, `year`, `links`를 유지합니다. 링크가 없어도 `links`는 `[]`로 둡니다. DOI가 아직 없으면 `url`을 생략합니다.
- `url`이 있으면 제목 옆에 **Link**가 표시됩니다. 추가 링크는 `"links": [{ "text": "Code", "url": "https://example.org/" }]` 형식입니다.
- Conference도 같은 기본 형식입니다. `journal_name`은 필요 없으며 `venue`에 학회명을 적습니다.
- Patents는 `title`에 특허명, `authors`에 발명자, `venue`에 특허 번호·등록일을 적습니다. 기존 항목을 복사해 수정하면 됩니다.
- `[J68]`, `[C94]`, `[P28]` 같은 번호는 **자동 생성**합니다. 제목에 번호를 넣지 마세요. 오래된 항목이 1번이고 최신일수록 번호가 큽니다. 중간 항목을 추가·삭제·이동하면 번호가 달라질 수 있습니다.
- `venue`에 입력한 `Editor's Choice`, `Oral Presentation`은 자동으로 빨간색 강조가 적용됩니다.

새 Journal에는 `id`를 부여하고 유지하는 것을 권장합니다. `id`가 없는 기존 논문의 **제목과 DOI를 동시에 바꾸려면**, 먼저 `id`만 추가해 한 번 저장한 뒤 제목·DOI를 수정하세요. 최초 등록 날짜가 새로 계산되는 것을 막기 위한 순서입니다.

## 구성원 추가·수정하기

### Researchers

`researchers` 배열에서 기존 구성원을 복사해 수정합니다.

```json
{
  "name": "Member Name",
  "group": "M.S./Ph.D. Students",
  "appointment": "M.S./Ph.D. Student (2026.03 - present)",
  "background": [
    "B.S. in Department of Artificial Intelligence, Yonsei University"
  ],
  "details": [
    "M.S./Ph.D. Student",
    "CT reconstruction, medical image analysis",
    "member@yonsei.ac.kr"
  ],
  "image": "assets/member-name.jpg"
}
```

`details`는 **직함 → 연구 관심 분야 → 이메일** 순서를 유지합니다. `Interest:`와 이메일 표시 위치는 자동으로 처리됩니다. Scholar 링크가 있으면 `"scholar_url": "https://scholar.google.com/citations?user=..."` 필드를 추가합니다.

| 화면의 그룹명 | `group`에 넣을 정확한 값 |
| --- | --- |
| Research Associates | `Research Associate` |
| Postdocs | `Postdoc` |
| Ph.D. Students | `Ph.D. Students` |
| M.S./Ph.D. Students | `M.S./Ph.D. Students` |
| M.S. Students | `M.S. Students` |

화면에 복수형으로 표시되더라도 `group`은 위 표 그대로 사용합니다. 같은 그룹 안에서는 배열 순서대로 표시됩니다. `appointment`와 `background`도 함께 유지하세요. 사진이 없으면 `"image": ""`로 두면 이니셜이 표시됩니다.

### Alumni / Staff

졸업생은 `alumni` 배열에 아래 형식으로 추가하고 Researchers의 기존 항목은 제거합니다. `group`, `appointment`, `background`를 그대로 옮기지 말고 Alumni 형식으로 정리합니다.

```json
{
  "name": "Member Name",
  "details": ["Ph.D.", "Current affiliation or position", "member@example.org"],
  "image": "assets/member-name.jpg"
}
```

Staff는 `researchers` 안에서 `details`의 첫 항목이 `"Staff"`인 구성원입니다. 이 구분값은 유지하고 기존 Staff 항목에서 이름·연락처·사진을 수정하세요.

### Professor

`professor.bio`는 소개 문장, `professor.experience`는 경력, `professor.education`은 학력입니다. 경력은 `dates`와 `description`, 학력은 여기에 `details` 배열을 더한 기존 형식을 유지합니다. 이름·소속·연락처 등은 위의 파일 안내 표를 참고하세요.

## 사진·로고 바꾸기

1. 새 파일을 `docs/assets/`에 올립니다. 영문 소문자·숫자·하이픈으로 된 파일명을 권장합니다.
2. 구성원 사진은 `content.json`의 `image`를 `assets/파일명.jpg`로 바꿉니다. 경로에 `docs/`를 붙이지 않습니다.
3. 교수님 사진은 `images.professor`의 첫 번째 경로를 수정합니다.
4. Home 배경은 `style.css`의 `.home-main>.hero`에서 이미지 경로를 바꿉니다. 상단 로고 경로는 `build.py`의 header 부분에 있습니다.

구성원 사진은 세로형 비율로 표시됩니다. 얼굴이 위쪽 중앙에 오도록 준비하고, 큰 원본은 웹용으로 줄이면 로딩이 빨라집니다. 새 파일명을 사용하면 이전 사진이 캐시에 남는 문제를 줄일 수 있습니다.

## 저장 전 확인 / 문제가 생겼을 때

- JSON의 키와 문자열에는 큰따옴표 `"`를 사용합니다. 항목 사이에는 쉼표를 넣되 마지막 항목 뒤에는 붙이지 않습니다.
- 파일 전체를 예시 한 항목으로 덮어쓰지 마세요. 최상위 `journal`, `news`, `researchers` 등의 구조를 유지합니다.
- 사진·링크가 열리는지, PC와 모바일에서 배치가 올바른지 확인합니다.
- 변경이 안 보이면 최신 Actions 실행이 완료됐는지 확인합니다. 성공했는데 이전 화면이 보이면 새로고침하거나 캐시를 확인합니다. CSS·JavaScript 변경 시 `build.py`의 해당 파일 `?v=...` 값도 갱신하면 캐시 문제를 줄일 수 있습니다.
- **Run failed**가 나오면 해당 실행의 빨간색 단계에서 오류를 확인합니다. JSON 문법, 필수 필드 누락, 생성 코드 오류를 먼저 확인하세요. 실패한 변경은 게시되지 않으며 이전에 성공한 사이트가 유지됩니다. 검사를 끄지 말고 원인을 수정합니다.
- 잘못 수정했다면 파일의 **History**에서 이전 내용을 확인해 복원한 뒤 다시 저장합니다.

## 로컬에서 미리보기 (선택)

Python 3과 Node.js가 설치된 환경에서 저장소 폴더를 열고 실행합니다.

```sh
python tools/test_news_dates.py
node tools/test_publications.cjs
python tools/build.py
python -m http.server 8765 --directory docs
```

[http://localhost:8765](http://localhost:8765)에 접속합니다. 환경에 따라 `python` 대신 Windows의 `py` 또는 macOS/Linux의 `python3`를 사용합니다. 미리보기만으로는 사이트가 공개되지 않습니다.

새 Journal의 자동 날짜까지 배포와 똑같이 확인하려면, 전체 Git 이력이 있는 저장소에서 변경사항을 커밋한 뒤 `python tools/news_dates.py`를 `build.py`보다 먼저 실행합니다. 이 명령은 로컬 `content.json`에 계산된 날짜를 쓰므로 일반 내용 편집에 꼭 필요한 단계는 아닙니다.

<details>
<summary>유지보수 담당자용 파일 구성</summary>

```text
docs/
  content.json              # 논문·구성원·수동 뉴스 원본
  assets/                   # 이미지와 로고
  style.css                 # 디자인과 반응형 배치
  publications.js           # 브라우저의 논문·뉴스 표시
  site.js                   # 메뉴·TOP·연락처·데이터 로딩
  *.html                    # 자동 생성된 페이지
tools/
  build.py                  # 전체 페이지 생성
  news_dates.py             # 새 Journal 등록 월 계산
  journal_baseline.json     # 기존 논문 식별 목록
  test_news_dates.py        # 등록 날짜 검증
  test_publications.cjs     # 논문·뉴스 표시 검증
.github/workflows/pages.yml # main 변경 시 검증·생성·게시
```

Pages 설정은 **GitHub Actions**를 사용합니다. 등록 월은 Git 이력으로 계산해 게시용 데이터에 반영하며, 원본 JSON에 다시 커밋하지 않습니다. 뉴스 표시 규칙을 바꿀 때는 정적 페이지를 만드는 `build.py`와 브라우저용 `publications.js`를 함께 맞추고 검증하세요.

</details>
