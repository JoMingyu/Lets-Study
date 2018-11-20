# Lets-Study
나만 읽기 아까운 글이나 문서를 모아두는 공간입니다. 어떤 주제를 공부하거나, 공부의 방향을 잡거나, 그냥 가볍게 읽기 위한 재밌는 글을 원하는 누군가가, 양질의 글에 쉽게 접근할 수 있도록 도와주는 것이 이 저장소의 목적입니다.

의식의 흐름으로 나눈 카테고리에, 링크로 이루어진 리스트 형태로 구성됩니다. 일단 링크 막 모아두고, 한번 읽고 나면 이게 어떤 글이고 왜 추천하는지를 간략하게 작성하고 있습니다.

여러분도 북마크에서 몇 개만 공유해 주세요. 레포 주인이 공부하는 분야가 넓지 않아서, 별 거 아닌 것처럼 보이는 기여더라도 큰 도움이 됩니다.

## 배경지식
### 그냥 배경지식
- [Microservices with gRPC](https://medium.com/@goinhacker/microservices-with-grpc-d504133d191d)
- [함수형 프로그래밍이란?](https://medium.com/@lazysoul/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80-d881230f2a5e)
- [검색엔진최적화(SEO) 쉬운 가이드](https://blog.usefulparadigm.com/%EA%B2%80%EC%83%89%EC%97%94%EC%A7%84%EC%B5%9C%EC%A0%81%ED%99%94-seo-%EC%89%AC%EC%9A%B4-%EA%B0%80%EC%9D%B4%EB%93%9C-f003911b0a79)
- [정규표현식의 개념과 기초 문법](https://soooprmx.com/archives/7718)  
    sooop님의 블로그는 개념에 대한 정의가 깔끔하고, 쉬운 설명에 비해 많은 지식이 들어오는 가성비 높은 글 천지라 개인적으로 마음속 1순위 블로그인데, 감사하게도 정규 표현식에 대해서도 써 주셨다.
- [regexr - 정규표현식을 연습할 수 있는 playground](https://regexr.com/)
- [협정 세계시(UTC)](https://ko.wikipedia.org/wiki/%ED%98%91%EC%A0%95_%EC%84%B8%EA%B3%84%EC%8B%9C)  
    세계 표준시. 우리나라는 여기에 9시간을 더한 KST라는 한국 표준시를 사용한다.
- [ISO 8601](https://ko.wikipedia.org/wiki/ISO_8601)  
    `2018-11-13T22:36:38+09:00`처럼 생겨먹은, 시간에 대한 i18n 처리를 할 때 거론되는 날짜와 시간에 관련된 국제 표준. format이 한가지 종류가 아니라는 점(날짜를 YYYY-MM-DD로 표현하는 경우도 있고, YYYYMMDD로 표현하는 경우도 있으며 시간이 UTC라면 +00:00 대신 Z를 쓸 수 있다.)과 timezone에 대한 표기 없이 UTC와의 시차만 표현한다는 점이 흥미로웠다. 어딘가 시간이 들어가는 곳에서는 그냥 KST로 저장하고 `2018-11-13 15:31:10`처럼 표현했는데, 모든 시간을 UTC로 저장하고 ISO 8601 포맷을 사용하는 게 가장 확장성이 높을 듯. 동일한 시간대에서 통신 시 지역 시간을 가정하는 것이 편할지라도, 서로 다른 시간대 간의 통신에서는 애매할 수 있을테니 ISO 8601 포맷을 사용하여 UTC에서 얼마를 더해 이 시각이 나왔는지를 알려주는 것이 좋을 것이다.
- [유닉스 시간](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4_%EC%8B%9C%EA%B0%84)  
    Epoch(1970-01-01T00:00:00Z)로부터의 경과 시간을 초로 환산하여 정수로 나타낸 것. 여담으로 timestamp는 '시각을 나타내는 문자열'이라는 다소 큰 범위의 정의를 가지고 있어서, 1256953732같이 생긴 건 [unix time](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4_%EC%8B%9C%EA%B0%84)이라고 부르는 것이 가장 정확하다. `Sat Jul 23 02:16:57 2018`같은 것도 타임스탬프라고 부르기 때문.
- [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)  
    시각을 표기하는 곳에서 KST, CST, EDT같이 timezone에 대해서는 약어만 마주치며 살다가, PrestoDB에서 `Asia/Seoul`같은 표현을 보고 이리저리 찾아보니 timezone의 약어는 표준이 따로 없다고 한다. 그래서 timezone 약어 목록으로 가장 유명한 [Time Zone Abbreviations](https://www.timeanddate.com/time/zones/)를 찾아봤더니 `CST`가 미국 중부 표준시, 중국 표준시, 쿠바 표준시를 모두 나타내는 등의 모호함이 있었다. tz database time zones라는 이름을 가진 해당 링크는 그 이름처럼 [IANA TZDB](https://www.iana.org/time-zones)에서 사용하는 타임존 목록을 그대로 가져와 정리한 것인데, 약어 대신 `Asia/Tokyo`, `Europe/Lisbon`처럼 지역명을 사용하고 있다. 이게 타임존을 다루는 데에 사실상 가장 현실적인 방안이라고들 생각하는 것 같다.
- [JSONSchema](http://tcpschool.com/json/json_schema_schema)  
    JSON payload를 검증하는 데에 쓸 수 있는 JSONschema. 처음 봤을땐 뭐 이런 TMI 스펙이 다있어? 싶었는데 이젠 이거 없으면 validation이 어렵다.

### 백엔드에 가까운
- [초보를 위한 도커 안내서 - 1. 도커란 무엇인가?](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
- [초보를 위한 도커 안내서 - 2. 설치하고 컨테이너 실행하기](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)
- [초보를 위한 도커 안내서 - 3. 이미지 만들고 배포하기](https://subicura.com/2017/02/10/docker-guide-for-beginners-create-image-and-deploy.html)
- [Map AWS services to Google Cloud Platform products](https://cloud.google.com/free/docs/map-aws-google-cloud-platform)
- [[야생의 땅: 듀량고] SPOF 없는 분산 MMORPG 서버](https://www.slideshare.net/sublee/spof-mmorpg)
- [[야생의 땅: 듀랑고] 서버 아키텍처 Vol. 2 (자막)](https://www.slideshare.net/sublee/lt-vol-2)
- [채점 현황 속도 올리기 - 스타트링크](https://startlink.blog/2018/03/09/%EC%B1%84%EC%A0%90-%ED%98%84%ED%99%A9-%EC%86%8D%EB%8F%84-%EC%98%AC%EB%A6%AC%EA%B8%B0/)  
    백준 온라인 저지(BOJ)에서 채점 현황 페이지의 속도를 올리기 위한 경험이 담겨 있다. real world에서의 쿼리 튜닝에 관한 이야기라 재밌게 본 것 같다.
- [ipify: 300억 요청 처리, 그 너머로](http://www.haruair.com/blog/4108)  
    IP 주소 검색 서비스인 [ipify](https://www.ipify.org/)를 Node.js로 개발하고, 성능에 문제를 겪은 뒤, Go로 API를 다시 작성해 문제를 해결한 이야기. 월간 200 달러로 300억 요청 처리. Go에 뽐뿌가 오게 만드는 글이다. 근데 Node.js가 왜 훨씬 느렸는지가 구체적으로 안 나와 있어서 아쉬웠다. ab라는 벤치마킹 툴을 새로 알게 되어 좋았음.
- [ab - HTTP 서버 벤치마킹 툴](https://httpd.apache.org/docs/2.4/en/programs/ab.html)  
    학교에서 한창 기숙사 관련 웹 서비스의 백엔드를 개발할 때 벤치마킹 코드를 직접 작성했었던 적 있는데, 그 때 이 도구를 알았으면 덜 삽질했었을텐데 싶다.

### HTTP에 가까운
- [API Security Checklist-ko](https://github.com/shieldfy/API-Security-Checklist/blob/master/README-ko.md)
- [API development tools](https://github.com/yosriady/api-development-tools)
- [REST API 제대로 알고 사용하기](http://meetup.toast.com/posts/92)
- [그런 REST API로 충분한가](http://slides.com/eungjun/rest#/)
- [So what’s this GraphQL thing I keep hearing about?](https://medium.freecodecamp.org/so-whats-this-graphql-thing-i-keep-hearing-about-baf4d36c20cf)
- [GraphQL을 오해하다](https://medium.com/@FourwingsY/graphql%EC%9D%84-%EC%98%A4%ED%95%B4%ED%95%98%EB%8B%A4-3216f404134)
- [HTTPS는 HTTP보다 빠르다](https://tech.ssut.me/2017/05/07/https-is-faster-than-http/)
- [나만 모르고 있던 HTTP2](http://www.popit.kr/%EB%82%98%EB%A7%8C-%EB%AA%A8%EB%A5%B4%EA%B3%A0-%EC%9E%88%EB%8D%98-http2/)  
    아니 뭐 이렇게까지 HTTP/1.1을 까고 HTTP/2를 찬양하나 싶었는데, 이유 있는 비판인 것 같다. HTTP/2가 SPDY를 기반으로 개발되었고, 구글이 HTTP/2가 SPDY를 대체할 것이라고 발표한 것은 처음 알았다.
- [WebSocket과 Socket.io](https://d2.naver.com/helloworld/1336)  
    결국 웹소켓의 요지는 polling을 push 방식으로 만든다는 건데, HTTP/2.0의 server push 기능이 어느정도 웹소켓을 흉내낼 수 있지 않을까 싶었다.
- [HTTP 응답코드 결정 다이어그램](https://github.com/for-GET/http-decision-diagram)

### 코딩이나 패턴에 관한 얘기
- [Why is global state so evil?](https://softwareengineering.stackexchange.com/questions/148108/why-is-global-state-so-evil)  
    전역 변수가 왜 나쁜지에 대한 이야기
- [So Singletons are bad, then what?](https://softwareengineering.stackexchange.com/questions/40373/so-singletons-are-bad-then-what)
- [코드 커버리지 80% 넘긴 썰 - 테스팅을 잘 하기 위한 8퍼센트 개발팀의 삽질기](https://brunch.co.kr/@leehosung/43)
- [점진적인 레거시 웹 어플리케이션 개선 과정](https://www.slideshare.net/arawnkr/ss-115339631)
- [Higher-order-function(고차함수) with Kotlin](https://medium.com/@lazysoul/high-order-function-%EA%B3%A0%EC%B0%A8%ED%95%A8%EC%88%98-22b147d0c4a5)  
    인자로 함수를 취하거나, 결과로 함수를 반환하는 함수. HOF라고도 부른다. 이게 수학에서도 있는 개념이라고 함. Java에서 메소드에 overrided method가 포함된 익명 클래스를 만들며 그 객체를 넘겨주는 것도 HOF라고 부를 수 있을까?

### 소프트웨어 공학
### AWS
### Git
### Linux

## CS
### 자료구조

## 언어
### Python
#### 언어 자체에 대한 이야기
- [Glossary](https://docs.python.org/3/glossary.html)  
    iterable, iterator, awaitable, context manager, coroutine function과 같이, 파이썬을 쓰다 보면 한번쯤은 마주치게 되는 단어들이 정리된 문서.
- [Hidden features of Python](https://stackoverflow.com/questions/101268/hidden-features-of-python)  
    그다지 알려지지 않았지만 유용한 Python의 기능들.
- [Intermediate Python](http://book.pythontips.com/en/latest/index.html)  
    파이썬에 이런 기능도 있는데 혹시 알아? 하는 느낌의 팁북. 바로 위의 'Hidden features of Python'과 비슷한 느낌이다.
- [A collection of design patterns/idioms in Python](https://github.com/faif/python-patterns)  
    파이썬으로 구현한 이런저런 디자인 패턴들의 모음.
- [wtfpython](https://github.com/satwikkansal/wtfpython)  
    파이썬을 사용하며 생길 수 있는 해프닝들의 모음인데, 흥미로운 주제들이 많이 정리되어 있다.
- [Better Python 59 Ways](https://github.com/SigmaQuan/Better-Python-59-Ways)  
    한국에서는 '파이썬 코딩의 기술'이라고 이름지어진, 'Effective Python'이라는 도서에서 사용된 59가지 예제 모음
- [제너레이터와 코루틴](https://soooprmx.com/archives/5622)
- [비동기 파이썬](https://mingrammer.com/translation-asynchronous-python/)  
    Hackernoon에 작성된 [Asynchronous Python](https://hackernoon.com/asynchronous-python-45df84b82434)을 번역한 글. 그린 스레드부터 콜백 스타일, asyncio와 async/await 문법까지 차근차근 설명되어 있다.
- [Python GC가 작동하는 원리](https://winterj.me/python-gc/)
- [파이썬 언더스코어(_)에 대하여](https://mingrammer.com/underscore-in-python/)
- [Removing duplicates in lists](https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists)  
    리스트에서 중복된 요소를 제거하는 방법에 대한 이야기다. 알아두면 요긴하게 써먹을 수 있음.
- [Difference between append vs. extend list methods in Python](https://stackoverflow.com/questions/252703/difference-between-append-vs-extend-list-methods-in-python)  
    list를 확장하는 메소드로 append와 extend가 있는데, 이 둘의 차이. 3번째 답변이 오버로딩된 연산자와 timeit을 통한 시간 복잡도까지 잘 설명하고 있다.
- [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)  
    Python 3.5부터 사용 가능한 type definition. typing 모듈의 overload 데코레이터로 오버로딩도 가능하다.

#### 개발 환경
- [가상 환경 및 패키지](https://docs.python.org/ko/3/tutorial/venv.html)
- [pipenv란 무엇인가](https://medium.com/@erish/python-pipenv-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-961b00d4f42f)  
    virtualenv+pyenv+pip가 합쳐진 형태의, Python계의 npm인 pipenv에 대한 소개. pyenv가 설치되어 있으면 알아서 필요한 버전을 설치하고 가상 환경을 열어준다는 게 정말 맘에 든다. pyenv 설치하고, pyenv-virtualenv 설치하고, requirements.txt를 dev와 production에 나눠 만들 필요가 없으니 정말 편한 도구.
- [pipenv로 Python 프로젝트 관리하기](https://cjh5414.github.io/how-to-manage-python-project-with-pipenv/)  
    글 자체가 깔끔하게 정리되어 있기도 하고, pipenv가 제공하는 명령어들에 대한 구체적인 설명이 들어 있어서 초심자에게 더 좋은듯.
#### 표준 라이브러리
- [파이썬의 새로운 병렬처리 API – Concurrent.futures](https://soooprmx.com/archives/5669)
- [asyncio : 단일 스레드 기반의 Nonblocking 비동기 코루틴 완전 정복](https://soooprmx.com/archives/6882)
- [collection.OrderedDict](https://pymotw.com/2/collections/ordereddict.html)  
    내 생각엔 OrderedDict를 써볼만한 case가 그리 많진 않을 것 같은데, OrderedDict를 써야 하는 적은 case 입장에서는 정말 개이득인 컨테이너 타입인 것 같다.(메인 언어로 파이썬 쓴지 1년 넘는 동안 딱 2번 써봤지만, 그때마다 OrderedDict 덕분에 정말 편-안했음) 단지 넣은 순서대로 dictionary가 유지된다는 것 뿐이지, 자동으로 sort는 해주지 않는다는 것을 인지하고 있어야 한다.
- [Find Monday's date with Python](https://stackoverflow.com/questions/1622038/find-mondays-date-with-python)  
    특정 datetime 객체를 기준으로 다음주 월요일과 저번주 월요일에 대한 datetime 객체를 가져오는 방법. timedelta로 weekday만큼을 day에 빼주면 'datetime 객체가 속한 week의 월요일'이 되고, 여기에 week를 1 더하면 다음주 월요일, week를 1 빼면 저번주 월요일이 된다. datetime에서 월요일을 0으로 사용한다는 것을 응용함. 다른 예로 datetime 객체가 속한 week의 화요일에 대한 datetime을 원한다면 weekday + 1만큼을 day에서 빼주면 된다. 언제든 적재될 수 있는 어떤 데이터가 매주 월요일에 지워져야 하는 경우, expire를 계산할 때 유용할 것 같다. 다음주 월요일 0시 0분의 시각과 현재 시각의 delta를 사용하면 되니까.
#### 외부 라이브러리
- [aiohttp로 하는 비동기 HTTP 요청](https://item4.github.io/2017-11-26/Asynchronous-HTTP-Request-with-aiohttp/)
#### 테스팅
#### SQLAlchemy
- [SQLAlchemy 시작하기](https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-1/)  
    잘 정리된 SQLAlchemy 한글 튜토리얼
- [Literal SELECT](https://stackoverflow.com/questions/7533146/how-do-i-select-literal-values-in-an-sqlalchemy-query)  
    UNION 쿼리 등에서 자주 사용되는 literal SELECT를 SQLAlchemy에서는 어떻게 표현하는지에 대한 질문이다.
- [Query 객체로 WHERE절 작성하기(Common filter operators)](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators)  
    SQLAlchemy의 Query 객체에서는 WHERE 절을 filter 메소드로 표현하는데, 여기에 들어가는 일반적인 operator들에 대한 정리다.
- [How to pass a not like operator in a sqlalchemy ORM query](https://stackoverflow.com/questions/5018694/how-to-pass-a-not-like-operator-in-a-sqlalchemy-orm-query)  
    Bitwise not operator가 아니라, `sqlalchemy.not_` 함수를 사용해서도 NOT을 표현할 수 있다.
- [sqlalchemy.orm.query.Query.slice(start, stop)](https://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.slice)  
    Query 객체에서 LIMIT 쿼리를 표현하려면, slice 메소드를 사용하거나, __getitem__에 슬라이싱이 지원되므로 빌트인 슬라이싱 연산을 사용할 수 있다. 이건 [all 메소드의 코드](https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/orm/query.py#L2835-L2841)와 [\_\_getitem\_\_ 메소드의 코드](https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/orm/query.py#L2666-L2690), 그 바로 밑에 있는 [slice 메소드의 코드](https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/orm/query.py#L2693-L2732)를 살펴보면 도움이 많이 된다.
- [How to union two subqueries in SQLAlchemy](https://stackoverflow.com/questions/20024744/how-to-union-two-subqueries-in-sqlalchemy-and-postgresql)  
    Query 객체의 union이나 union_all 메소드를 통해 UNION, UNION ALL 쿼리를 표현할 수 있다.
- [SQLAlchemy: engine, connection and session difference](https://stackoverflow.com/questions/34322471/sqlalchemy-engine-connection-and-session-difference)  
    engine, connection, session의 차이가 무엇이고 각각 언제 써먹어야 할지를 알 수 있다.
- [Avoiding boilerplate session handling code in SQLAlchemy functions](https://stackoverflow.com/questions/14799189/avoiding-boilerplate-session-handling-code-in-sqlalchemy-functions)  
    contextlib.contextmanager를 통해 session을 다루는 보일러플레이트를 with-as 문으로 관리하도록 만드는 패턴
- [Contextual/Thread-local Sessions](https://docs.sqlalchemy.org/en/latest/orm/contextual.html)  
    context에 의존하는 어플리케이션에 적용하기 적합한 scoped_session에 대한 가이드. 하나의 스레드에서 동일한 세션을 이용해 여러 작업을 처리하는 경우, 함수에 session을 파라미터로 넘겨줘서 session을 유지하는 경우가 많은데 scoped_session을 사용하면 이러한 문제가 줄어든다.
- [How to execute raw SQL in SQLAlchemy](https://stackoverflow.com/questions/17972020/how-to-execute-raw-sql-in-sqlalchemy-flask-app)  
    raw SQL을 실행하는 방법
- [Column and Data Types](https://docs.sqlalchemy.org/en/latest/core/type_basics.html)  
    데이터 타입이 Generic Types/SQL Standard and Multiple Vendor Types/Vendor-Specific Types로 나뉜다는 것을 알게 됐다. Vendor-Specific Types는 한번쯤 써볼만한 것 같음.
- ['select as' in SQLAlchemy](https://stackoverflow.com/questions/9187530/using-alias-for-select-as-in-sqlalchemy)  
    Column.label 메소드로 aliasing(SELECT AS)를 표현하는 방법
- [SQLAlchemy simple example of sum, average, min, max](https://stackoverflow.com/questions/11830980/sqlalchemy-simple-example-of-sum-average-min-max)  
    sqlalchemy.sql.functions 모듈의 함수를 이용해 aggregation을 하는 방법
- [Dealing with duplicate primary keys on insert in SQLAlchemy](https://stackoverflow.com/questions/10322514/dealing-with-duplicate-primary-keys-on-insert-in-sqlalchemy-declarative-style)  
    질문이 굉장히 세세한데, 결론은 `session.add` 대신 `session.merge` 메소드를 사용하면 primary key duplicate 시 알아서 update하도록 만들 수 있다는 것이다.
- [Get the number of rows in table using SQLAlchemy](https://stackoverflow.com/questions/10822635/get-the-number-of-rows-in-table-using-sqlalchemy)  
    쿼리에 대한 row count를 어떻게 반환받는지에 대한 질문이다. 답변의 내용처럼, 그냥 `query.count()`는 wrapped select 꼴의 쿼리를 생성하기 때문에 `session.query(func.count(...)).scalar()`같은 방식을 사용하기도 한다.
- [SQLAlchemy Transaction 관리 Practice 공유](https://blog.qodot.me/post/sqlalchemy-transaction-%EA%B4%80%EB%A6%AC-practice-%EA%B3%B5%EC%9C%A0/)  
    데이터베이스에 접근할 때마다 context를 열지 않고, 데코레이팅된 함수 단위로 세션을 발급하는 식으로 트랜잭션을 관리하는 practice다. Flask에 SQLAlchemy를 엮어서 쓸 때마다 단지 'with문 쓰는게 좀 번거롭다' 정도만 생각했지, 더 나은 방법을 생각하려고 하지 않았던 게, 내 머리에서 이런 아이디어가 나오지 않았던 이유인 것 같다.
#### Peewee
#### MongoEngine
#### Zappa
#### boto3
- [When to use a boto3 client and when to use a boto3 resource?](https://stackoverflow.com/questions/39272744/when-to-use-a-boto3-client-and-when-to-use-a-boto3-resource/39273710)  
    boto3.resource는 단지 boto3.client를 wrapping한 high level API이며, boto3.resource는 boto3.client의 모든 API를 래핑하지 않으므로 어쩔수 없이 boto3.client나 boto3.resource.meta.client를 사용해야 한다는 것을 잘 요약해준 것 같다.
- [boto3 - credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#configuring-credentials)  
    boto3가 credential을 어디서 가져오는지, 우선순위는 어떤지에 대한 문서.
- [Upload-Download File From S3 with Boto3](https://qiita.com/hengsokvisal/items/329924dd9e3f65dd48e7)  
    boto3로 S3에 객체를 업로드하고, 다운로드하는 기본적인 인터랙션에 대한 가이드.
- [How do I get the file/key size in boto S3?](https://stackoverflow.com/questions/5315603/how-do-i-get-the-file-key-size-in-boto-s3)  
    버킷에서 특정 객체의 size를 얻어오기 위한 방법. s3 client 객체의 head_object로 객체에 HEAD 요청을 보내면 된다.

### Golang
#### 언어 자체에 대한 이야기
- [고루틴은 어떻게 동작하는가?](https://stonzeteam.github.io/How-Goroutines-Work/)

## 데이터베이스에 관련된
- [What is an ORM and where can I learn more about it?](https://stackoverflow.com/questions/1279613/what-is-an-orm-and-where-can-i-learn-more-about-it)  
    ORM이 무엇이고, 장점과 단점은 무엇인지에 대한 설명. ORM 라이브러리는 대부분 무겁고 러닝커브가 생기긴 하지만, 상황에 따라 동적으로 SELECT 쿼리를 빌드하는 머리아픈 경험을 해 봤다면 ORM이 이만큼 유연할 수가 없다. 복잡한 쿼리가 아니라면 성능 문제도 딱히 없는 것 같다. 이래저래 논쟁을 끌고 다니는 기술이긴 한데, 단점을 감당하지 않기 위해서 ORM으로 얻을 수 있는 메리트를 모두 포기하고 raw SQL을 쓸 이유가 딱히 없지 않을까 싶다. 물론 대용량 데이터를 다룰 때는 raw SQL을 쓰는 것이 마음 편한 듯.
- [DBMS는 어떻게 트랜잭션을 관리할까?](https://d2.naver.com/helloworld/407507)  
    CUBRID의 개발을 이끌고 있는 엔지니어가 쓴, 트랜잭션의 관리를 DBMS 레벨에서 설명한 글. ACID 성질부터 UNDO와 REDO, 상태 로깅과 전이 로깅, 커밋을 하면 어떤 일이 일어나는지, group commit과 트랜잭션 철회 등이 정말 잘 정리되었다. 역시 기술은 해본 사람이 잘 아는 것 같다.
### SQL
### MySQL
- [Illegal mix of collations for operation 'like'](https://stackoverflow.com/questions/18629094/illegal-mix-of-collations-for-operation-like-while-searching-with-ignited-data)  
    DATETIME 필드에 대해 유니코드가 아닌 문자열로 LIKE 쿼리 수행 시 발생하는 문제에 대한 SOF 질문
- [Insert into a MySQL table or update if exists](https://stackoverflow.com/questions/4205181/insert-into-a-mysql-table-or-update-if-exists)  
    key duplication이 없다면 insert하고, 있으면 update를 MySQL에서 어떻게 하는지에 대한 SOF 질문. 다른 데이터베이스 엔진에서는 `UPSERT`나 `MERGE`라는 이름으로 사용되고 있는 것 같다.
### PrestoDB
### MongoDB
### SQLite
### Redis
### Memcached

## Android
- [Android 공식 가이드](https://developer.android.com/guide/index.html?hl=ko)
- [Android의 HTTP 클라이언트 라이브러리](http://d2.naver.com/helloworld/377316)
- [Using Retrofit 2.x as REST client](http://www.vogella.com/tutorials/Retrofit/article.html)
- [Retrofit 2와 함께하는 정말 쉬운 HTTP](https://academy.realm.io/kr/posts/droidcon-jake-wharton-simple-http-retrofit-2/)  
    Realm academy같은 게 백엔드에는 없는게 너무 아쉽다. 내가 못 찾는건가..
- [Android와 개발 패턴](https://tosslab.github.io/android/2015/03/01/01.Android-mvc-mvvm-mvp)
- [Firebase를 실제 모바일 백엔드로 사용하면 일어날 수 있는 일들](https://academy.realm.io/kr/posts/firebase-as-a-real-mobile-backend/)
- [Android의 ORM](http://d2.naver.com/helloworld/472196)
- [Android의 이미지로딩 라이브러리](http://d2.naver.com/helloworld/429368)
- [Android 앱 메모리 최적화](http://d2.naver.com/helloworld/539525)
- [안드로이드 BadTokenException의 원인과 해결방법](https://blog.sangyoung.me/2016/12/28/BadTokenException/)  
    context알못에게 큰 시련과도 같은 BadTokenException. 내 경우 retrofit의 onResponse에서 다이얼로그를 띄울 때 ContextWrapper.getApplicationContext()의 반환을 전달했더니 났던 오류다.

## 웹 프론트엔드
- [PostCSS](https://medium.com/@FourwingsY/postcss-%EC%86%8C%EA%B0%9C-727310aa6505)
- [Learning React 예제 한국어 번역](https://github.com/enshahar/learning-react-kor)
- [한국어로 배우는 리엑트](https://github.com/reactkr/learn-react-in-korean)
- [React Bit](https://github.com/vasanthk/react-bits)
- [Awesome React Components](https://github.com/brillout/awesome-react-components)
- [네이버 메일 모바일웹 리엑트 적용기](http://d2.naver.com/helloworld/4966453)
- [React 인가 Vue 인가?](https://joshua1988.github.io/web_dev/vue-or-react/)
- [[번역] React를 본격적으로 하기 전 알면 좋은 6가지](https://jaeyeophan.github.io/2018/01/02/React-tips-for-beginners/)
- [React 프로젝트의 디렉토리 구조](https://medium.com/@FourwingsY/react-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%9D%98-%EB%94%94%EB%A0%89%ED%86%A0%EB%A6%AC-%EA%B5%AC%EC%A1%B0-bb183c0a426e)
- [webpack3 + postcss 설정하기](https://medium.com/@FourwingsY/webpack-postcss-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0-34f9c486093a)
- [카카오페이지 웹 React 포팅 후기](https://medium.com/@ljs0705/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%8E%98%EC%9D%B4%EC%A7%80-%EC%9B%B9-react-%ED%8F%AC%ED%8C%85-%ED%9B%84%EA%B8%B0-76402cc5e031)

## 웹 프레임워크
### Flask
- [Flask 1.0 Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)
- [Flask 1.0 공식 튜토리얼](http://flask.pocoo.org/docs/1.0/tutorial/)
- [Flask 1.0에서 달라진 점](https://winterj.me/flask-release/)
- [Patterns for Flask 1.0](http://flask.pocoo.org/docs/1.0/patterns/)
### Spring
- [스프링부트로 웹 서비스 출시하기](http://jojoldu.tistory.com/250?category=635883)
- [Gradle + SpringBoot + Travis CI + Coveralls + 텔레그램 연동하기](http://jojoldu.tistory.com/275)
- [스프링 부트 2.0 레퍼런스 코딩](https://github.com/keesun/study/blob/master/spring-boot-reference-coding.md)
- [JWT 기반 로그인 구현 예제](https://github.com/szerhusenBC/jwt-spring-security-demo)
- [폼 기반 인증 구현 튜토리얼](http://cusonar.tistory.com/8?category=607756)
- [MVC 구조에서 service와 serviceImpl을 왜 만드는가](http://multifrontgarden.tistory.com/97)
### Express.js
- [Express에서 Sequelize를 사용할 때 Circular Import Problem을 해결하는 방법 - sequelize/express-example](https://github.com/sequelize/express-example)

## 뭔가 어디 카테고리에 특별히 넣어두기 애매한데 재미는 있는 회고록이나 글
- [Scala의 도입을 회고하며](https://medium.com/rainist-engineering/%EC%8A%A4%EC%B9%BC%EB%9D%BC%EC%9D%98-%EB%8F%84%EC%9E%85%EC%9D%84-%ED%9A%8C%EA%B3%A0%ED%95%98%EB%A9%B0-d491125abeb9)
- [우리(Reddit)가 Typescript를 선택한 이유](https://medium.com/@constell99/%EC%9A%B0%EB%A6%AC%EA%B0%80-typescript%EB%A5%BC-%EC%84%A0%ED%83%9D%ED%95%9C-%EC%9D%B4%EC%9C%A0-b0a423654f1e)
- [OP.GG 오픈부터의 1년을 되돌아보며](http://log.op.gg/op-gg-1%EB%85%84-%EC%8A%A4%ED%86%A0%EB%A6%AC/)
- [배달의민족 앱에 적용된 오프라인 모드에 대하여](http://woowabros.github.io/experience/2018/11/05/about_offline_mode.html)
- [DEVIEW 2016 참가 신청 기능 개발기](https://d2.naver.com/helloworld/5048491)  
    결론은 '신청자 수를 RDB에서 관리하지 않고 Redis 기반의 분산 메모리 저장소인 nbase-arc로 바꿨더니 잘 되더라'였다. 글만 보면 그냥 nbase 붙이고 나니까 너무나도 매끄럽고 쉽게 해결된 것만 같다. nbase-arc의 INCR 연산이 단순히 UPDATE 쿼리보다 속도가 빨라서 병목이 생기지 않았던 걸까? 이걸 조금 더 설명해줬으면 좋았을 것 같다. 무튼 캐시가 중요하긴 한가 보다. 2017, 2018 개발기도 올라왔으면 좋겠다.
