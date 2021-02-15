# Lets-Study
나만 읽기 아까운 글이나 문서를 모아두는 공간입니다. 어떤 주제를 공부하거나, 공부의 방향을 잡거나, 그냥 가볍게 읽기 위한 재밌는 글을 원하는 누군가가, 양질의 글에 쉽게 접근할 수 있도록 도와주는 것이 이 저장소의 목적입니다.

대충 나눈 카테고리에, 링크로 이루어진 unordered list 형태로 구성됩니다. 링크 하나마다 커밋 하나씩, commit description으로 해당 링크에 대한 간단한 요약을 적기도 합니다. 조금 길게 공부할만한 것이 생기면 시간 여유가 있을 때 살펴보고 [TIL](https://github.com/JoMingyu/TIL)에도 커밋합니다.

여러분도 북마크에서 몇 개만 공유해 주세요. 레포 주인이 공부하는 분야가 넓지 않아서, 별 거 아닌 것처럼 보이는 기여더라도 큰 도움이 됩니다.

# 배경지식
## 프로그래밍
### 동시성 프로그래밍
- [파이썬과 비동기 프로그래밍 시리즈](https://velog.io/@sjquant/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B3%BC-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-1-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80)
- [멈추지 않고 기다리기(Non-blocking)와 비동기(Asynchronous) 그리고 동시성(Concurrency)](https://tech.peoplefund.co.kr/2017/08/02/non-blocking-asynchronous-concurrency.html)  
### 함수 관련
- [함수형 프로그래밍이란?](https://medium.com/@lazysoul/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80-d881230f2a5e)
- [Higher-order-function(고차함수) with Kotlin](https://medium.com/@lazysoul/high-order-function-%EA%B3%A0%EC%B0%A8%ED%95%A8%EC%88%98-22b147d0c4a5)  
- [Currying](http://planbs.tistory.com/entry/Currying)  
- [함수형 프로그래밍: partial application과 curry](https://rhostem.github.io/posts/2017-04-20-curry-and-partial-application/)  
- [람다, 익명 함수, 클로저](https://hyunseob.github.io/2016/09/17/lambda-anonymous-function-closure/)  
- [자바스크립트의 호이스팅(Hoisting)](http://asfirstalways.tistory.com/197)  
- [코루틴 소개](https://medium.com/@jooyunghan/%EC%BD%94%EB%A3%A8%ED%8B%B4-%EC%86%8C%EA%B0%9C-504cecc89407)  
- [What is a pure function?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976)  
### 테스팅
- [유닛테스트에 대한 생각](https://blog.outsider.ne.kr/1275?fbclid=IwAR1Z9DPi-JJns_bSccrNZIo8zFo-0B8nAvIEHen3tu0_jaIUS34hY90FVJ0)  
- [테스트 주도 개발이란](http://www.ecogwiki.com/%ED%85%8C%EC%8A%A4%ED%8A%B8_%EC%A3%BC%EB%8F%84_%EA%B0%9C%EB%B0%9C%EC%9D%B4%EB%9E%80)
- [코드 커버리지 80% 넘긴 썰 - 테스팅을 잘 하기 위한 8퍼센트 개발팀의 삽질기](https://brunch.co.kr/@leehosung/43)
- [Realizing quality improvement through test driven development: results and experiences of four industrial teams](https://github.com/tpn/pdfs/raw/master/Realizing%20Quality%20Improvement%20Through%20Test%20Driven%20Development%20-%20Results%20and%20Experiences%20of%20Four%20Industrial%20Teams%20(nagappan_tdd).pdf)
#### Test Double
- [단위 테스트 케이스와 테스트 더블(Test Double)](https://medium.com/@SlackBeck/%EB%8B%A8%EC%9C%84-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%BC%80%EC%9D%B4%EC%8A%A4%EC%99%80-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%8D%94%EB%B8%94-test-double-2b88cccd6a96)
- [Mock Object란 무엇인가?](https://medium.com/@SlackBeck/mock-object%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-85159754b2ac)  
- [Testing Without Mocks: A Pattern Language](https://www.jamesshore.com/Blog/Testing-Without-Mocks.html)
- [What's the difference between a mock & stub?](https://stackoverflow.com/questions/3459287/whats-the-difference-between-a-mock-stub)
- [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
    - [Classical vs Mockist testing](https://agilewarrior.wordpress.com/2015/04/18/classical-vs-mockist-testing/)
#### 테스트에 관한 SaaS
- [Python 프로젝트에 Codecov 연동하기](https://cjh5414.github.io/codecov-python/)
- [codecov vs coveralls](http://text.youknowone.org/post/144201220021/codecov-vs-coveralls)
### 패턴
#### 디자인 패턴
- [So Singletons are bad, then what?](https://softwareengineering.stackexchange.com/questions/40373/so-singletons-are-bad-then-what)
- Repository Pattern
    - [Repository Design Pattern](https://medium.com/@pererikbergman/repository-design-pattern-e28c0f3e4a30)
    - [repository pattern vs ORM](https://stackoverflow.com/questions/10155517/repository-pattern-vs-orm)
    - [Stop using repository pattern with an ORM](http://hamidmosalla.com/2018/11/25/stop-using-repository-pattern-with-an-orm/)
    - [Don't use DAO, use Repository](https://thinkinginobjects.com/2012/08/26/dont-use-dao-use-repository/)
    - [Difference between Repository and Service Layer?](https://stackoverflow.com/questions/5049363/difference-between-repository-and-service-layer)
- Dependency Injection
    - [What is dependency injection?](https://stackoverflow.com/questions/130794/what-is-dependency-injection)
    - [Dependency Injection Demystified](https://www.jamesshore.com/Blog/Dependency-Injection-Demystified.html)
    - [DI 란?](https://gmlwjd9405.github.io/2018/11/09/dependency-injection.html)  
    - [Dependency Injection in Python](https://medium.com/@shivama205/dependency-injection-python-cb2b5f336dce) 
    - [Pinject](https://github.com/google/pinject)  
        `"Dependency Injection" is a 25-dollar term for a 5-cent concept.`
#### 아키텍처 패턴
- [10가지 소프트웨어 아키텍처 패턴](https://mingrammer.com/translation-10-common-software-architectural-patterns-in-a-nutshell/)  
- [Circuit breaker 패턴을 이용한 장애에 강한 MSA 서비스 구현하기](https://bcho.tistory.com/1247)
- [Clean architectures in Python: a step-by-step example](https://www.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/)
#### 캐싱
- [What is difference between LRU and LFU?](https://stackoverflow.com/a/29225598)  
- [WTF is Memoization](https://medium.com/@chialunwu/wtf-is-memoization-a2979594fb2a)  
- [What is the difference between Caching and Memoization?](https://stackoverflow.com/a/6469470)  
- [캐시가 동작하는 아주 구체적인 원리](https://parksb.github.io/article/29.html?utm_source=gaerae.com&utm_campaign=%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%8A%A4%EB%9F%BD%EB%8B%A4&utm_medium=social&fbclid=IwAR2QTpnMNc9fbjbnj6SQWf_VQwJznCBUQ_4NWovcGXXugl-Nd2hDj44JoXI)
### 언어론에 가까운 이야기
- [Exression verses Statement](https://stackoverflow.com/a/19224)  
- [Static/Dynamic vs Strong/Weak](https://stackoverflow.com/a/2351203)  
- [Runtime vs Compile time](https://stackoverflow.com/a/846421)
- [A Python Tutorial To Understanding Scopes and Closures.](https://medium.com/@dannymcwaves/a-python-tutorial-to-understanding-scopes-and-closures-c6a3d3ba0937)
- [Difference between Definition and Declaration](https://www.geeksforgeeks.org/difference-between-definition-and-declaration/)
- [What is the difference between statically typed and dynamically typed languages?](https://stackoverflow.com/questions/1517582/what-is-the-difference-between-statically-typed-and-dynamically-typed-languages)
### 컴파일러에 가까운 이야기
- [What is Short Circuiting?](https://stackoverflow.com/questions/9344305/what-is-short-circuiting-and-how-is-it-used-when-programming-in-java)
- [자바스크립트 개발자를 위한 AST](https://gyujincho.github.io/2018-06-19/AST-for-JS-devlopers)
- [The super tiny compiler](https://github.com/jamiebuilds/the-super-tiny-compiler)
### 좋은 코드를 작성하기 위한 노력
- [개발자에게 유용한 법칙, 이론, 원칙, 그리고 패턴들 #hackerlaws](https://github.com/codeanddonuts/hacker-laws-kr)
- [The Little Manual of API Design](https://github.com/papers-we-love/papers-we-love/blob/master/api_design/api-design.pdf)
- [DRY code vs. WET code](https://www.codementor.io/joshuaaroke/dry-code-vs-wet-code-89xjwv11w)  
- [Red-Green-Refactor](https://www.jamesshore.com/Blog/Red-Green-Refactor.html)
- [Why is global state so evil?](https://softwareengineering.stackexchange.com/questions/148108/why-is-global-state-so-evil)  
- [점진적인 레거시 웹 어플리케이션 개선 과정](https://www.slideshare.net/arawnkr/ss-115339631)
- [Clean Code: 5 Essential Takeaways](https://medium.com/better-programming/clean-code-5-essential-takeaways-2a0b17ccd05c)
- [Why Premature Optimization Is the Root of All Evil](https://stackify.com/premature-optimization-evil/)
### 객체지향 프로그래밍
- [객체지향 개발 5대 원리: SOLID](http://www.nextree.co.kr/p6960/)
- [Parametric Polymorphism](https://rosettacode.org/wiki/Parametric_polymorphism)
#### 코드 퀄리티에 관한 SaaS
- [Sonarqube](https://www.sonarqube.org/)  
- [Scrutinizer](https://scrutinizer-ci.com/)
- [Codacy](https://app.codacy.com/projects)
- [Code Climate](https://codeclimate.com/)
### CI
- [Continuous Integration](https://www.martinfowler.com/articles/continuousIntegration.html)
#### CI를 위한 SaaS
- [About Travis CI](https://medium.com/hbsmith/about-travis-ci-65b04d3dead6)
- [CircleCI Overview](https://circleci.com/docs/2.0/about-circleci/)
- [Welcome to AppVeyor](https://www.appveyor.com/docs/)
### 정규 표현식
- [정규표현식의 개념과 기초 문법](https://soooprmx.com/archives/7718)
- [regexr - 정규표현식을 연습할 수 있는 playground](https://regexr.com/)
- [ignore case sensitivity](https://stackoverflow.com/questions/9655164/regex-ignore-case-sensitivity)
### Glossary
- [Drop-in replacement](https://en.wikipedia.org/wiki/Drop-in_replacement)
### 유틸리티
#### Makefile
- [What does @: (at symbol colon) mean in a Makefile?](https://stackoverflow.com/questions/8610799/what-does-at-symbol-colon-mean-in-a-makefile)

## 웹
- [What are the differences between server-side and client-side programming?](https://softwareengineering.stackexchange.com/a/171210)  

## 프로토콜, 표준, 가이드라인
### 스펙(RFC, ISO standards)
- [What is the maximum length of a valid email address?](https://stackoverflow.com/questions/386294/what-is-the-maximum-length-of-a-valid-email-address/44317754)
### HTTP
- [WebSocket과 Socket.io](https://d2.naver.com/helloworld/1336)  
- [Websockets vs Long Polling](https://www.ably.io/blog/websockets-vs-long-polling/?utm_source=share&utm_medium=ios_app&fbclid=IwAR0ZAaLo_ZhFjL5xO21hsXKk5E_pRule-h0Bzs3gEl3uxB50Y3bi7ganH3w)
- [웹 기술로 구현하는 Adaptive HTTP Streaming](https://meetup.toast.com/posts/131)
- [What are the advantages and disadvantages of using a content delivery network(CDN)?](https://stackoverflow.com/a/2145389)
- [GET이냐 POST냐 그것이 문제로다](https://homoefficio.github.io/2019/12/25/GET%EC%9D%B4%EB%83%90-POST%EB%83%90-%EA%B7%B8%EA%B2%83%EC%9D%B4-%EB%AC%B8%EC%A0%9C%EB%A1%9C%EB%8B%A4/)
#### CORS
- [Understanding CORS](https://medium.com/@baphemot/understanding-cors-18ad6b478e2b)
- [Understanding CORS - spring.io](https://spring.io/understanding/CORS)  
- [Developers don't understand CORS](https://fosterelli.co/developers-dont-understand-cors?fbclid=IwAR3g4df3shqau16v1PSYMXDa_8QO7thqQTyO8NnW3PlF8hlDaIXnkwuIam4)
#### HTTP API
- [API Security Checklist-ko](https://github.com/shieldfy/API-Security-Checklist/blob/master/README-ko.md)
- [API development tools](https://github.com/yosriady/api-development-tools)
- [HTTP 응답코드 결정 다이어그램](https://github.com/for-GET/http-decision-diagram)
- [Web API Pagination with the 'Timestamp_ID' Continuation Token](https://phauer.com/2018/web-api-pagination-timestamp-id-continuation-token/)
- [JSON:API Standard](https://jsonapi.org/)
- [서버 개발자는 클라이언트를 믿지 마라 - 2020 수능 평가원 성적표 대란으로 알아본 흔히 마주치는 휴먼 에러와 폼 데이터 조작에 대응하기](https://juneyoung.io/article/1.html)
#### REST
- [REST API 제대로 알고 사용하기](http://meetup.toast.com/posts/92)
- 그런 REST API로 괜찮은가
    - [그런 REST API로 괜찮은가 - 발표자료](http://slides.com/eungjun/rest#/)
    - [그런 REST API로 괜찮은가 - 영상](https://tv.naver.com/v/2292653)
- [REST 의 Uniform Interface에 대하여](http://midnightcow.tistory.com/entry/REST-What-is-REST-2)
- [Architectural Styles and the Design of Network-based Software Architectures - Roy Fielding](https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf)
- [바쁜 개발자들을 위한 REST 논문 요약](https://blog.npcode.com/2017/03/02/%EB%B0%94%EC%81%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%93%A4%EC%9D%84-%EC%9C%84%ED%95%9C-rest-%EB%85%BC%EB%AC%B8-%EC%9A%94%EC%95%BD/)
- [REST API의 이상향, HATEOAS](https://wallees.wordpress.com/2018/04/19/rest-api-hateoas/)
- [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html)
- REST API Design
    - [RESTful API Design. Best Practices in a Nutshell.](https://phauer.com/2015/restful-api-design-best-practices/?source=post_page---------------------------)
    - [REST API Design: Filtering, Sorting, and Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#)
    - [Best Practices for Designing a Pragmatic RESTful API](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
    - [How to design REST API for export endpoint?](https://stackoverflow.com/questions/33877541/how-to-design-rest-api-for-export-endpoint)
- REST API Design Tips
    - [Is using magic (me/self) resource identifiers going against REST principles?](https://stackoverflow.com/questions/35719797/is-using-magic-me-self-resource-identifiers-going-against-rest-principles)
    - [RESTfully design /login or /register resources?](https://stackoverflow.com/questions/7140074/restfully-design-login-or-register-resources)
    - [Best way to implement a restful toggle-action?](https://stackoverflow.com/questions/3266292/best-way-to-implement-a-restful-toggle-action)
#### GraphQL
- [So what’s this GraphQL thing I keep hearing about?](https://medium.freecodecamp.org/so-whats-this-graphql-thing-i-keep-hearing-about-baf4d36c20cf)
- [GraphQL을 오해하다](https://medium.com/@FourwingsY/graphql%EC%9D%84-%EC%98%A4%ED%95%B4%ED%95%98%EB%8B%A4-3216f404134)
- [Designing GraphQL Mutations](https://dev-blog.apollodata.com/designing-graphql-mutations-e09de826ed97)
#### HTTP2/HTTPS
- [HTTPS는 HTTP보다 빠르다](https://tech.ssut.me/https-is-faster-than-http/)
- [나만 모르고 있던 HTTP2](http://www.popit.kr/%EB%82%98%EB%A7%8C-%EB%AA%A8%EB%A5%B4%EA%B3%A0-%EC%9E%88%EB%8D%98-http2/)  
- [HTTP/2 소개 - Google Developers](https://developers.google.com/web/fundamentals/performance/http2/?hl=ko)  
- [HTTPS는 어떻게 다를까?](https://parksb.github.io/article/24.html)
### JSON 관련
- [커맨드라인 JSON 프로세서 jq - 기초 문법과 작동 원리](https://www.44bits.io/ko/post/cli_json_processor_jq_basic_syntax)
#### NDJSON
- [Newline delemited JSON is awesome](https://medium.com/@kandros/newline-delimited-json-is-awesome-8f6259ed4b4b)  
- [JSON Lines](https://jsonlines.org/)
#### JSONSchema
- [JSONSchema](http://tcpschool.com/json/json_schema_schema)  
- [object - pattern properties](https://json-schema.org/understanding-json-schema/reference/object.html#pattern-properties)  
- [object - Schema dependencies](https://json-schema.org/understanding-json-schema/reference/object.html#schema-dependencies) 
- [JSON Schema: verifying object's values, without keys](https://stackoverflow.com/questions/31117586/json-schema-verifying-objects-values-without-keys)
### 인증 관련
#### JWT
- [Introduction to JSON Web Tokens](https://jwt.io/introduction/)  
#### OAuth
- [구글 API를 통해서 배우는 인증 (oauth 2.0)](https://opentutorials.org/course/2473/16571)
### Protobuf
- [Protobuf](https://developers.google.com/protocol-buffers/docs/proto3)  
- [Google Protocol Buffers and HTTP](https://stackoverflow.com/questions/1425912/google-protocol-buffers-and-http)  
### Date & Time
- [협정 세계시(UTC)](https://ko.wikipedia.org/wiki/%ED%98%91%EC%A0%95_%EC%84%B8%EA%B3%84%EC%8B%9C)
- [유닉스 시간](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4_%EC%8B%9C%EA%B0%84)  
- [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)  
- [ISO 8601](https://ko.wikipedia.org/wiki/ISO_8601)  
- [What's the difference between ISO 8601 and RFC 3339 Date Formats?](https://stackoverflow.com/questions/522251/whats-the-difference-between-iso-8601-and-rfc-3339-date-formats)  
- [DateTimeFormat(Joda-Time)](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html)
### 국제화 관련
- [en_US or en-US, which one should you use?](https://stackoverflow.com/questions/4904803/en-us-or-en-us-which-one-should-you-use)
### DNS
- [Demystifying DNS for web developers](https://medium.com/@jgefroh/demystifying-dns-for-web-developers-ace5a3ae559f)  
- [DNSimple](https://support.dnsimple.com/)
### MQTT
- [How does MQTT protocol work?](https://stackoverflow.com/a/9570898)  
### RSS
- [RSS 2.0 specification](https://validator.w3.org/feed/docs/rss2.html)  
### SEO
- [검색엔진최적화(SEO) 쉬운 가이드](https://blog.usefulparadigm.com/%EA%B2%80%EC%83%89%EC%97%94%EC%A7%84%EC%B5%9C%EC%A0%81%ED%99%94-seo-%EC%89%AC%EC%9A%B4-%EA%B0%80%EC%9D%B4%EB%93%9C-f003911b0a79)
### 가이드라인
- [Command Line Interface Guidelines](https://clig.dev/)

## Git
### Git 구성 요소
- [What is .gitignore exactly?](https://stackoverflow.com/a/27850270)
### Commands
- [git blame](https://git-scm.com/book/ko/v1/Git-%EB%8F%84%EA%B5%AC-Git%EC%9C%BC%EB%A1%9C-%EB%B2%84%EA%B7%B8-%EC%B0%BE%EA%B8%B0)  
- [git rebase -i 사용하기](https://jupiny.com/2018/05/07/git-rebase-i-option/)
### 이럴 땐 이렇게
- [Oh shit, git!](https://ohshitgit.com)
- [How to resolve merge conflict during pull request?](https://stackoverflow.com/a/45819784)
- [How do I update a GitHub forked repository?](https://stackoverflow.com/a/7244456)
- [.gitignore is ignored by Git](https://stackoverflow.com/a/11451731)
- [How can one change the timestamp of an old commit in Git?](https://stackoverflow.com/questions/454734/how-can-one-change-the-timestamp-of-an-old-commit-in-git)  
- [How to change the commit author for one specific commit?](https://stackoverflow.com/questions/3042437/how-to-change-the-commit-author-for-one-specific-commit)
- [좋은 git commit 메시지를 위한 영어 사전](https://blog.ull.im/engineering/2019/03/10/logs-on-git.html)
### Troubleshooting
- [git not displaying unicode file names](https://stackoverflow.com/questions/34549040/git-not-displaying-unicode-file-names)
### GitHub
- [Pull Request를 이용한 개발 흐름을 적용해 보고 나서](https://blog.outsider.ne.kr/1199)
- [GitHub의 Pull Request를 로컬로 가져오기](https://blog.outsider.ne.kr/1204?fbclid=IwAR38bv1LQCyXbgWoo2DfPnnjCu_BtitACL4jkJlIA0e-2pM-A37Jq7-fFBU)
- [Reviewing proposed changes in a pull request](https://help.github.com/en/articles/reviewing-proposed-changes-in-a-pull-request)

## 운영체제별 기반지식
### Linux
- [export, echo 명령어](http://keepcalmswag.blogspot.com/2018/06/linux-unix-export-echo_49.html)
- [lsof 사용법](https://www.lesstif.com/pages/viewpage.action?pageId=20776078)  
- [grep 사용법](https://zzsza.github.io/development/2017/12/16/linux-4/)  
- [awk 사용법](https://zzsza.github.io/development/2017/12/20/linux-6/)  
- [htop Explained Visually](https://codeahoy.com/2017/01/20/hhtop-explained-visually/)  
- [Crontab 사용법](https://jdm.kr/blog/2)  
- [리눅스 명령어 sudo, su, su -](https://www.leafcats.com/168)
- [리눅스 서버의 TCP 네트워크 성능을 결정짓는 커널 파라미터 이야기](https://meetup.toast.com/posts/53)

### Mac
- [How does Coconut Battery determine a Macbook battery's design capacity?](https://apple.stackexchange.com/questions/240406/how-does-coconut-battery-determine-a-macbook-batterys-design-capacity)

## Computer Science
### 컴퓨터 이론
- [유한 상태 기계(Finite State Machine)](https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%95%9C_%EC%83%81%ED%83%9C_%EA%B8%B0%EA%B3%84)
### 운영체제
- [컴퓨터가 코드를 읽는 아주 구체적인 원리](https://parksb.github.io/article/25.html)
- [Race condition 발생시키고 Mutex lock으로 해결하기](https://parksb.github.io/article/16.html)
### 자료구조
- [IEEE 754 - Rounding Rules](https://en.wikipedia.org/w/index.php?title=IEEE_754#Rounding_rules)
- [Bankers Rounding](https://wiki.c2.com/?BankersRounding)
### 알고리즘
- [루프 불변성](http://egloos.zum.com/kuphy00/v/2475164)  
- [시간 복잡도 빠르게 이해하기](https://joshuajangblog.wordpress.com/2016/09/21/time_complexity_big_o_in_easy_explanation/)  
- [점근 표기법](https://ratsgo.github.io/data%20structure&algorithm/2017/09/13/asymptotic/)    
- [분할정복](https://ko.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort)    
- [힙 정렬](https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/)    
- [동적 계획법](https://www.zerocho.com/category/Algorithm/post/584b979a580277001862f182)   
- [파이썬으로 정리하는 Quick-Sort](https://parksb.github.io/article/18.html)
- [Dijkstra’s Shortest Path Algorithm in Python](https://medium.com/cantors-paradise/dijkstras-shortest-path-algorithm-in-python-d955744c7064)
- [Levenshtein Distance](https://madplay.github.io/post/levenshtein-distance-edit-distance)
### 네트워크
- [Top-Down으로 접근하는 네트워크](https://parksb.github.io/article/23.html)

## 보안
### 암호화
- [안전한 패스워드 저장](https://d2.naver.com/helloworld/318732)

## 데이터 엔지니어링, 수학
- [Markov Chains - The University of Auckland](https://www.stat.auckland.ac.nz/~fewster/325/notes/ch8.pdf?fbclid=IwAR0XxZEbI5xJbyrzrTSAp7fYUZACMAPDEGw_bbdUhs6e8gwNjLqPFNm3x4M)
- [From “What is a Markov Model” to “Here is how Markov Models Work”](https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71)

## Marketing
- [User Acquisition - appsflyer](https://www.appsflyer.com/mobile-attribution-glossary/user-acquisition/)  
- [User Acquisition - Adjust](https://www.adjust.com/glossary/user-acquisition/)  
- [Re-Engagement](https://www.adjust.com/glossary/re-engagement/)  
- [What is a tracking link?](https://support.rebrandly.com/hc/en-us/articles/360007299393-What-is-a-tracking-link-)  
- [Single-Touch vs. Multi-Touch Marketing Attribution](https://www.rockerbox.com/blog/attribution-101-single-touch-versus-multi-touch)
- [Retargeting](https://retargeter.com/what-is-retargeting-and-how-does-it-work/)
- [Reattribution](https://www.adjust.com/glossary/reattribution/)
- [알아두면 좋은 이메일마케팅 지표](https://blog.stibee.com/%EC%95%8C%EC%95%84%EB%91%90%EB%A9%B4-%EC%A2%8B%EC%9D%80-%EC%9D%B4%EB%A9%94%EC%9D%BC-%EB%A7%88%EC%BC%80%ED%8C%85-%EC%A7%80%ED%91%9C-92161806525f0)  
- [ARPU / ARPPU](https://plbarts.tistory.com/223)
- [DAU/MAU Reatio](https://www.geckoboard.com/learn/kpi-examples/startup-kpis/dau-mau-ratio/)

# 프로젝트 관리
## PM
- [실리콘밸리PM 무엇이든 물어보세요!](https://www.notion.so/PM-fe42daa7b9be4ef0ba914928953453b9)

# 프로젝트
- [Casbin](https://casbin.org/)  
    memo : An authorization library that supports access control models like ACL, RBAC, ABAC

# 벤치마킹
## 배울 점 많은 코드
### Android
- [WebToon](https://github.com/Pluu/WebToon)
### 백엔드
- [pyconkr-api](https://github.com/pythonkr/pyconkr-api)
- [velog](https://github.com/velopert/velog)
- [SpaceX-API](https://github.com/r-spacex/SpaceX-API)
### 서비스 전체
- [Corona Warn App](https://github.com/corona-warn-app)
## Websites to follow
- [44bits.io](https://www.44bits.io)
- [GeekNews](https://news.hada.io/)

# 교양 컨텐츠
## 소프트웨어 마인드/철학
- [소프트웨어 환멸감(Software disenchantment)](https://muchtrans.com/translations/software-disenchantment.ko.html)
- [소프트웨어 개발자 되기는 왜 어려운가?](https://hl1itj.tistory.com/m/136?category=327240)
- [\[번역\] 개발 배우기가 정말 어려운 이유](https://brunch.co.kr/@jypthemiracle/14)
- [Cognitive Biases in Programming](https://hackernoon.com/cognitive-biases-in-programming-5e937707c27b)
- [당신의 개발자들은 결코 느리지 않다.](http://tech.trenbe.com/?p=547)
- [스타트업에서 성장한다는 주니어의 착각](https://brunch.co.kr/@goodgdg/43?fbclid=IwAR26GEeJxPTR-fgvmtmlWTQBQa4P6N6f1hpiF_yFjydbk4ii-1tVttKaf1g)
- [나는 어떻게 더 나은 프로그래머가 되었는가](https://medium.com/@rinae/%EB%B2%88%EC%97%AD-%EB%82%98%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%8D%94-%EB%82%98%EC%9D%80-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EA%B0%80-%EB%90%98%EC%97%88%EB%8A%94%EA%B0%80-b84c45d8bf98)
- [Avoiding burnout as an ambitious developer](https://stackoverflow.blog/2020/01/13/avoiding-burnout-as-an-ambitious-developer/)
## 조직 문화
- [에어비앤비 엔지니어가 일하는 게 행복한 이유](https://www.youtube.com/watch?v=iaNl6zKTBfg&feature=youtu.be&fbclid=IwAR19X3cC4bYMVlNUy4M4gpkjCxQrk0u0OcEplf1-7MlLnWnokk7iDd5OHik)
- [기능 공장에서 일하고 있다는 12가지 신호](https://cojette.github.io/featurefactory/)
- [Why Development Teams are Slow](https://medium.com/javascript-scene/why-development-teams-are-slow-89107985c75c)
- [사고를 쳐도 혼나지 않는 회사](https://brunch.co.kr/@svillustrated/13)
## UI/UX
- [따릉아! 문제는 UI/UX야!](https://brunch.co.kr/@supernova9/180?fbclid=IwAR2A4e1swo4tUHN8jyCvq9S8KvUzzzhwjqRCG_L4bkeMgbuYbL7M9P7OJfY)
- [Why is Vertical Rhythm an Important Typography Practice?](https://zellwk.com/blog/why-vertical-rhythms/)
## 자기계발
- [잘하려 하면 잘 안 되는 이유](http://moneyman.kr/archives/1666)

# 학습
## 교육 사이트
- [progate](https://progate.com/languages)

# 글 쓰기
## 글 쓰는 데 도움이 되는 것
- [carbon](https://carbon.now.sh/)

# 백엔드
## 백엔드 관련 배경지식
- [Microservices with gRPC](https://medium.com/@goinhacker/microservices-with-grpc-d504133d191d)
- [The Complete Guide to the ELK Stack - 2018](https://logz.io/learn/complete-guide-elk-stack/#intro)
- [Time Series Database and Tick Stack](https://www.slideshare.net/GianlucaArbezzano/time-series-database-and-tick-stack)
### Ops
- [Already learned DevOps? Great, now it’s time for GitOps](https://thenextweb.com/contributors/2018/12/08/all-you-need-to-know-about-gitops/)  
### recovery/failover
- [Failover & Disaster Recovery](https://stackoverflow.com/questions/120139/failover-disaster-recovery)
- [What is failover?](https://searchstorage.techtarget.com/definition/failover)  
- [What is High Availability?](https://www.digitalocean.com/community/tutorials/what-is-high-availability)  
- [Disater Recovery Strategies](http://www.computepatterns.com/517/disaster-recovery-strategies/)
### Deployment
- [Blue/Green Deployment: What It Is and How it Reduces Your Risk](https://rollout.io/blog/blue-green-deployment/)  
## Docker
- [초보를 위한 도커 안내서 - 1. 도커란 무엇인가?](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
- [초보를 위한 도커 안내서 - 2. 설치하고 컨테이너 실행하기](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)
- [초보를 위한 도커 안내서 - 3. 이미지 만들고 배포하기](https://subicura.com/2017/02/10/docker-guide-for-beginners-create-image-and-deploy.html)
- [개발자가 처음 Docker 접할때 오는 멘붕 몇가지](https://www.popit.kr/%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B0%80-%EC%B2%98%EC%9D%8C-docker-%EC%A0%91%ED%95%A0%EB%95%8C-%EC%98%A4%EB%8A%94-%EB%A9%98%EB%B6%95-%EB%AA%87%EA%B0%80%EC%A7%80/)
- [도커를 이용한 웹서비스 무중단 배포하기](https://subicura.com/2016/06/07/zero-downtime-docker-deployment.html)  
- [왜 굳이 도커(컨테이너)를 써야 하나요?](https://www.44bits.io/ko/post/why-should-i-use-docker-container)  
- [Intro Guide to Dockerfile Best Practices](https://blog.docker.com/2019/07/intro-guide-to-dockerfile-best-practices/?utm_source=share&utm_medium=ios_app&fbclid=IwAR1KhKGQv70JzSz51PeTQ3PHETXMSGzigdptAVmWc529bPnaYggDRhucalM)
- [Docker images - types. Slim vs slim-stretch vs stretch vs alpine](https://stackoverflow.com/questions/54954187/docker-images-types-slim-vs-slim-stretch-vs-stretch-vs-alpine)
### Docker 커맨드 관련 지식들
- [Docker 데이터 볼륨 사용하기](http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter06/04)
- [How to mount a single file in a volume](https://stackoverflow.com/questions/42248198/how-to-mount-a-single-file-in-a-volume)
- [How to enter in a Docker container already running with a new TTY](https://stackoverflow.com/questions/20932357/how-to-enter-in-a-docker-container-already-running-with-a-new-tty)  
- [Docker run vs create](https://stackoverflow.com/a/37745261)
### Dockerfile, docker-compose.yml 관련 지식들
- [Docker VOLUME vs COPY vs ADD](http://coderbro.com/docker/2017/10/24/docker-volumes-vs-copy.html)
- [Automation of container creation and creating image with DB packed](https://forums.docker.com/t/automation-of-container-creation-and-creating-image-with-db-packed/4982)  
### Docker 써먹기
- [kitematic](https://kitematic.com/)  
- [아마존 엘라스틱 컨테이너 서비스(ECS) 입문](https://www.44bits.io/ko/post/container-orchestration-101-with-docker-and-aws-elastic-container-service)
- [ECS의 매니지드 컨테이너 AWS 파게이트 시작하기](https://www.44bits.io/ko/post/getting-started-with-ecs-fargate)
### Docker Compose
- [Docker (Compose) 활용법](http://raccoonyy.github.io/docker-usages-for-dev-environment-setup/)  
## Ansible
- [Ansible 101](https://medium.com/@denot/ansible-101-d6dc9f86df0a)  
## Terraform
- [테라폼(Terraform) 기초 튜토리얼 - AWS와 테라폼으로 구현하는 Infrastructure as Code](https://www.44bits.io/ko/post/terraform_introduction_infrastrucute_as_code)  
- [Terraform을 이용한 Infrastructure as Code 실전 구성하기](https://www.slideshare.net/awskorea/configuring-practical-aws-based-infrastructure-as-code-using-terraform-byoun-jeonghun)  
- [Ansible vs Terraform: Fight!](https://linuxacademy.com/blog/devops/ansible-vs-terraform-fight/)  
## 서버 아키텍처 관련 블로깅/발표자료
- [[야생의 땅: 듀랑고] SPOF 없는 분산 MMORPG 서버](https://www.slideshare.net/sublee/spof-mmorpg)
- [[야생의 땅: 듀랑고] 서버 아키텍처 Vol. 2 (자막)](https://www.slideshare.net/sublee/lt-vol-2)
- [DEVIEW 2016 참가 신청 기능 개발기](https://d2.naver.com/helloworld/5048491)  
- [타다 시스템 아키텍처](http://engineering.vcnc.co.kr/2019/01/tada-system-architecture/?fbclid=IwAR1TJy9RpUzM-iR0QZoF0W1pMNjCoZDDvs0tVf21uv01eCX59ulTI0QBT-8)
- [전 세계 팬들이 모일 수 있는 플랫폼 만들기](https://www.slideshare.net/awskr/ss-223007438)
## 웹서버 이야기
- [What is the difference between application server and web server?](https://stackoverflow.com/a/936257)  
- [Difference between proxy server and reverse proxy server](https://stackoverflow.com/a/366212)
## 도움되는 SaaS
- [runscope](https://www.runscope.com)  
- [statuspage.io](https://www.statuspage.io/)  
- [Super](https://super.so/)
- [Oopy](https://www.oopy.io/)
## 도움되는 툴
- [Facebook Account Kit](https://developers.facebook.com/docs/accountkit/)  
- [ab - HTTP 서버 벤치마킹 툴](https://httpd.apache.org/docs/2.4/en/programs/ab.html)
- [wrk](https://github.com/wg/wrk)
## Serverless
- [Serverless Architecture](https://www.slideshare.net/awskr/serverless-architecture-78022209)
- [서버리스 아키텍쳐(Serverless)란?](https://velopert.com/3543)  
## 교양
- [채점 현황 속도 올리기 - 스타트링크](https://startlink.blog/2018/03/09/%EC%B1%84%EC%A0%90-%ED%98%84%ED%99%A9-%EC%86%8D%EB%8F%84-%EC%98%AC%EB%A6%AC%EA%B8%B0/)  
- [ipify: 300억 요청 처리, 그 너머로](http://www.haruair.com/blog/4108)  
## DB
### DB 배경지식
- [What is an ORM and where can I learn more about it?](https://stackoverflow.com/a/1279678)  
- [DBMS는 어떻게 트랜잭션을 관리할까?](https://d2.naver.com/helloworld/407507)  
- [A Detailed Guide to Database Denormalization with Examples](https://rubygarage.org/blog/database-denormalization-with-examples)  
- [How does database indexing work?](https://stackoverflow.com/a/1130)  
- [What do Clustered and Non clustered index actually mean?](https://stackoverflow.com/a/1251652)  
- [Why do you create a View in a database?](https://stackoverflow.com/a/1278620)  
- [Are soft deletes a good idea?](https://stackoverflow.com/questions/2549839/are-soft-deletes-a-good-idea/2549843)  
- [What are OLTP and OLAP. What is the difference between them?](https://stackoverflow.com/questions/21900185/what-are-oltp-and-olap-what-is-the-difference-between-them)  
- [What are Covering Indexes and Covered Queries in SQL Server?](http://gywn.net/tag/covering-index/)  
- [What is a stored procedure?](https://stackoverflow.com/questions/459457/what-is-a-stored-procedure?lq=1)  
- [데이터베이스 분포도(Database Selectivity)](https://jdm.kr/blog/169)
- [What are the materialized views?](https://stackoverflow.com/questions/4463354/what-are-materialized-views)  
- [Are junction tables a good practice?](https://dba.stackexchange.com/questions/106001/are-junction-tables-a-good-practice)
### DB Vendor
- [InfluxDB](https://github.com/influxdata/influxdb)  
- [StatsD](https://github.com/etsy/statsd)  
- [Reduce MySQL Memory Utilization with ProxySQL](https://medium.com/searce/reduce-mysql-memory-utilization-with-proxysql-multiplexing-cbe09da7921c)  
- [druid](http://druid.io/druid.html)  
- [FluentD](https://blog.jonnung.com/system/2018/04/06/fluentd-log-collector-part1/)  
### SQL
#### Common DML(INSERT, SELECT, UPDATE, DELETE)
- [Insert into a MySQL table or update if exists](https://stackoverflow.com/a/4205207)  
- [SELECT 결과를 INSERT 하기](https://zetawiki.com/wiki/SQL_SELECT_%EA%B2%B0%EA%B3%BC%EB%A5%BC_INSERT_%ED%95%98%EA%B8%B0)
- [Multiple select statements in Single query](https://stackoverflow.com/questions/1775168/multiple-select-statements-in-single-query)
- [MySQL Orderby a number, Nulls last](https://stackoverflow.com/a/4195311)
- [How to check for Is not Null And Is not Empty string in SQL server?](https://stackoverflow.com/questions/8660203/how-to-check-for-is-not-null-and-is-not-empty-string-in-sql-server)
- [MySQL UNIQUE key not working](https://stackoverflow.com/questions/22156301/mysql-unique-key-not-working)
#### JOIN
- [Review of SQL JOINS](https://medium.com/@josemarcialportilla/review-of-sql-joins-ac5463dc71c9)
- [LEFT JOIN vs. LEFT OUTER JOIN in SQL Server](https://stackoverflow.com/questions/406294/left-join-vs-left-outer-join-in-sql-server)  
- [MySQL ON vs USING?](https://stackoverflow.com/questions/11366006/mysql-on-vs-using)  
#### Date, Time 연산 관련 쿼리
- [When is a timestamp (auto) updated?](https://stackoverflow.com/questions/18962757/when-is-a-timestamp-auto-updated)  
- [INTERVAL](http://www.mysqltutorial.org/mysql-interval/)  
### MySQL
- [Illegal mix of collations for operation 'like'](https://stackoverflow.com/a/18651057)  
- [MySQL 쓰면서 하지 말아야 할 것 17가지](https://blog.lael.be/post/370)  
- [MySQL 중복 키 관리 방법](http://jason-heo.github.io/mysql/2014/03/05/manage-dup-key2.html)  
- [Understanding MySQL Storage Engines](http://www.mysqltutorial.org/understand-mysql-table-types-innodb-myisam.aspx?fbclid=IwAR2SpjdINoy8rtFiHBpu7PMyAj3iuof5xM1A9-wYJe_c-_SLRKZh6I4DhuQ)
- [How to declare a variable in MySQL?](https://stackoverflow.com/questions/11754781/how-to-declare-a-variable-in-mysql)
- [Illegal mix of collations (utf8_unicode_ci,IMPLICIT) and (utf8_general_ci,IMPLICIT) for operation '='](https://stackoverflow.com/questions/11770074/illegal-mix-of-collations-utf8-unicode-ci-implicit-and-utf8-general-ci-implic)
- [How to show the last queries executed on MySQL?](https://stackoverflow.com/questions/650238/how-to-show-the-last-queries-executed-on-mysql)
- [MySQL cannot create foreign key constraint](https://stackoverflow.com/questions/21526055/mysql-cannot-create-foreign-key-constraint)
- [When to use SELECT … FOR UPDATE?](https://stackoverflow.com/questions/10935850/when-to-use-select-for-update)
- [갭락(Gap Lock)과 넥스트 키 락(Next-Key Lock)](https://idea-sketch.tistory.com/46)
### PrestoDB
- [Date and Time Functions and Operators](https://prestodb.io/docs/current/functions/datetime.html)
- [Presto equivalent of MySQL group_concat](https://stackoverflow.com/questions/44142356/presto-equivalent-of-mysql-group-concat)
### Druid
#### Query
- [Querying - Overview](http://druid.io/docs/latest/querying/querying.html)
- [Transforming Dimension Values](http://druid.io/docs/latest/querying/dimensionspecs.html)  
- [Querying - Aggregations](http://druid.io/docs/latest/querying/aggregations)
- [Querying - Aggregation Granularity](http://druid.io/docs/latest/querying/granularities.html)
### ElasticSearch
#### Query
- [Query and filter context](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html)  
- [ElasticSearch bool query combine](https://stackoverflow.com/a/40755927)  
- [What is the difference between must and filter Query DSL in ElasticSearch?](https://stackoverflow.com/a/43349478)  
- [ElasticSearch match vs term query](https://stackoverflow.com/questions/23150670/elasticsearch-match-vs-term-query)  
- [Source filter](https://www.elastic.co/guide/en/elasticsearch/reference/2.4/search-request-source-filtering.html)  
- [Terms Aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html)  
- [Term level query - range query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-range-query.html) 
- [Exclude empty-string, null and non-existant](https://discuss.elastic.co/t/exclude-empty-string-null-and-non-existant/181140)
- [Best way to check if a field exist in an Elasticsearch document](https://stackoverflow.com/questions/32949321/best-way-to-check-if-a-field-exist-in-an-elasticsearch-document)

#### Others
- [Elastic APM](https://www.elastic.co/guide/en/apm/get-started/current/overview.html)  
## 웹 프레임워크
### Python
#### Flask
- [flask-base](https://github.com/hack4impact/flask-base)
- [fbone](https://github.com/imwilsonxu/fbone)
- [cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask)
- [flask-foundation](https://github.com/JackStouffer/Flask-Foundation)
- [flask-rest-template](https://github.com/alexandre-old/flask-rest-template)
- [flask-appbuilder](https://github.com/dpgaspar/Flask-AppBuilder)
- [flask-realworld-example-app](https://github.com/gothinkster/flask-realworld-example-app)
- [flask-large-application-example](https://github.com/Robpol86/Flask-Large-Application-Example)
- [Flask 1.0 Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)
- [Flask 1.0 공식 튜토리얼](http://flask.pocoo.org/docs/1.0/tutorial/)
- [Flask 1.0에서 달라진 점](https://winterj.me/flask-release/)
- [Patterns for Flask 1.0](http://flask.pocoo.org/docs/1.0/patterns/)
- [Pynash: Proxy objects in Flask (and elsewhere)](http://pynash.org/2013/02/12/proxy-objects/)
- [What is the purpose of Flask's context stacks?](https://stackoverflow.com/questions/20036520/what-is-the-purpose-of-flasks-context-stacks)
- [Output Fields - Flask-RESTful documentation](https://flask-restful.readthedocs.io/en/0.3.5/fields.html)  
- [Signals](http://flask.pocoo.org/docs/1.0/signals/)
### Java
#### Spring
- [스프링부트로 웹 서비스 출시하기](http://jojoldu.tistory.com/250?category=635883)
- [Gradle + SpringBoot + Travis CI + Coveralls + 텔레그램 연동하기](http://jojoldu.tistory.com/275)
- [스프링 부트 2.0 레퍼런스 코딩](https://github.com/keesun/study/blob/master/spring-boot-reference-coding.md)
- [JWT 기반 로그인 구현 예제](https://github.com/szerhusenBC/jwt-spring-security-demo)
- [폼 기반 인증 구현 튜토리얼](http://cusonar.tistory.com/8?category=607756)
- [MVC 구조에서 service와 serviceImpl을 왜 만드는가](http://multifrontgarden.tistory.com/97)
### Node.js
#### Express.js
- [Express에서 Sequelize를 사용할 때 Circular Import Problem을 해결하는 방법 - sequelize/express-example](https://github.com/sequelize/express-example)

# 해킹
## HTTP
- [Permanent URL Hijack Through HTTP 301 Redirect Cache Poisoning](https://blog.duszynski.eu/domain-hijack-through-http-301-cache-poisoning/)

# 프로그래밍 언어
## Python
### 파이썬 더 잘 알기
- [Glossary](https://docs.python.org/3/glossary.html)    
- [제너레이터와 코루틴](https://soooprmx.com/archives/5622)
- [파이썬 언더스코어(_)에 대하여](https://mingrammer.com/underscore-in-python/)
- [Python __getitem__과 slice의 이해](https://item4.github.io/2015-10-26/Understanding-Python-__getitem__-and-slice/)  
- [파이썬의 변수](https://www.slideshare.net/ChrisCho2/pycon-korea-2019)
- [시간 복잡도로 살펴보는 파이썬 내장 자료형의 효율적인 활용](https://www.pycon.kr/program/talk-detail?id=137)
- [리얼월드 메타클래스](https://www.pycon.kr/program/talk-detail?id=6)
- [Why is Python 3.7 fastest](https://speakerdeck.com/jungwinter/why-is-python-3-dot-7-fastest?slide=137)
- [Better Python 59 Ways](https://github.com/SigmaQuan/Better-Python-59-Ways)  
- [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/)
- [Hidden features of Python](https://stackoverflow.com/questions/101268/hidden-features-of-python)  
- [Intermediate Python](http://book.pythontips.com/en/latest/index.html)  
- [A collection of design patterns/idioms in Python](https://github.com/faif/python-patterns)
#### What is
- [What is \_\_pycache__?](https://stackoverflow.com/questions/16869024/what-is-pycache)
- [What is the meaning of single and double underscore before an object name?
](https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name)
#### verses
- [Is there a difference between “raise exception()” and “raise exception” without parenthesis?](https://stackoverflow.com/questions/16706956/is-there-a-difference-between-raise-exception-and-raise-exception-without)
- [What is the difference between range and xrange functions in Python 2.X?](https://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x)
- [Difference between <type 'generator'> and <type 'xrange'>](https://stackoverflow.com/questions/39070168/difference-between-type-generator-and-type-xrange)  
    memo : you should understand that an iterator and an generator are not the same thing.
- [List comprehension vs map](https://stackoverflow.com/questions/1247486/list-comprehension-vs-map)
#### How to
- [Is PYTHONUNBUFFERED=TRUE a good idea?](https://github.com/awslabs/amazon-sagemaker-examples/issues/319)
- [Python equivalent of golang's defer statement](https://stackoverflow.com/a/34625254)  
- [Python - Disable output buffering](https://stackoverflow.com/questions/107705/disable-output-buffering)
- [ignoring backslash character in python](https://stackoverflow.com/questions/36623916/ignoring-backslash-character-in-python/36624018)
- [Nicest way to pad zeroes to a string](https://stackoverflow.com/questions/339007/nicest-way-to-pad-zeroes-to-a-string)
- [How to re-raise an exception in nested try/except blocks?](https://stackoverflow.com/questions/18188563/how-to-re-raise-an-exception-in-nested-try-except-blocks)
- [Sort a list by multiple attributes?](https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes)
- [How can the built-in range function take a single argument or three?](https://stackoverflow.com/questions/13366293/how-can-the-built-in-range-function-take-a-single-argument-or-three)
#### Why
- [Why True/False is capitalized in Python?](https://stackoverflow.com/questions/521476/why-true-false-is-capitalized-in-python)
- [Why is bool a subclass of int?](https://stackoverflow.com/questions/8169001/why-is-bool-a-subclass-of-int)
- [In python, why use logging instead of print?](https://stackoverflow.com/questions/6918493/in-python-why-use-logging-instead-of-print)
- [Why is the order in dictionaries and sets arbitrary?](https://stackoverflow.com/questions/15479928/why-is-the-order-in-dictionaries-and-sets-arbitrary)
#### Unexpected Behaviors
- [wtfpython](https://github.com/satwikkansal/wtfpython)
- [Python 3.x rounding behavior](https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior)
- [How to round float 0.5 up to 1.0, while still rounding 0.45 to 0.0, as the usual school rounding?](https://stackoverflow.com/questions/43851273/how-to-round-float-0-5-up-to-1-0-while-still-rounding-0-45-to-0-0-as-the-usual?rq=1)
- [Behaviour of increment and decrement operators in Python](https://stackoverflow.com/questions/1485841/behaviour-of-increment-and-decrement-operators-in-python)
#### collections
- [Removing duplicates in lists](https://stackoverflow.com/a/7961390)  
- [Difference between append vs. extend list methods in Python](https://stackoverflow.com/a/252711)  
#### 성능
- [Python GIL](https://medium.com/@mjhans83/python-gil-f940eac0bef9)
- [Python GC가 작동하는 원리](https://winterj.me/python-gc/)
- [\_\_slots__ magic](http://book.pythontips.com/en/latest/__slots__magic.html)
- [Exponentials in python x ** y vs math.pow(x, y)](https://stackoverflow.com/questions/20969773/exponentials-in-python-x-y-vs-math-powx-y)
- [How did Python implement the built-in function pow()?](https://stackoverflow.com/questions/5246856/how-did-python-implement-the-built-in-function-pow)
#### Python 3.7
- [dataclasses](https://docs.python.org/ko/3/library/dataclasses.html)
- [Python 3.7’s new builtin breakpoint — a quick tour](https://hackernoon.com/python-3-7s-new-builtin-breakpoint-a-quick-tour-4f1aebc444c)
#### Python 3.8
- [What's coming in Python 3.8](https://lwn.net/SubscriberLink/793818/0c6f9dd271021cd4/)
### 개발 환경
- [가상 환경 및 패키지](https://docs.python.org/ko/3/tutorial/venv.html)
- [pyenv-win](https://pypi.org/project/pyenv-win/)  

#### virtualenv
- [Python Virtualenv](https://medium.com/@Joachim8675309/python-virtualenv-c77e22bf5243)  
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)  

#### pipenv
- [pipenv란 무엇인가](https://medium.com/@erish/python-pipenv-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-961b00d4f42f)  
- [pipenv로 Python 프로젝트 관리하기](https://cjh5414.github.io/how-to-manage-python-project-with-pipenv/)  
- [Force pipenv to create a new virtualenv](https://stackoverflow.com/a/49258323)  
- [How to get pipenv running in docker?](https://stackoverflow.com/a/49705601)  
### 코드 스타일
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html?)
#### Style Checker
- [pycodestyle](https://github.com/PyCQA/pycodestyle)
- [flake8](https://github.com/PyCQA/flake8)
- [pylint](https://github.com/PyCQA/pylint)
- [pyflake](https://github.com/nvie/pyflakes)
#### Formatter
- [autopep8](https://github.com/hhatto/autopep8)
- [yapf](https://github.com/google/yapf)
- [Black](https://github.com/ambv/black)  

### 테스팅
- [코드 테스트하기 - The Hitchhiker's Guide to Python](https://python-guide-kr.readthedocs.io/ko/latest/writing/tests.html)
- [테스트에 걸리는 시간을 92% 줄이기](https://www.pycon.kr/program/talk-detail?id=67)
- [Advanced Python testing techniques](https://www.pycon.kr/program/talk-detail?id=134)
- [How should I verify a log message when testing Python code under nose?](https://stackoverflow.com/questions/899067/how-should-i-verify-a-log-message-when-testing-python-code-under-nose)
- [Assert that logging has been called with specific string](https://stackoverflow.com/questions/31728497/assert-that-logging-has-been-called-with-specific-string)
#### nose
- [Basic usage : Options](https://nose.readthedocs.io/en/latest/usage.html#options)
#### coverage
- [Configuration files](https://coverage.readthedocs.io/en/coverage-4.4.2/config.html)  
- [Coverage.py command line usage](https://coverage.readthedocs.io/en/coverage-4.2/cmd.html)
### 비동기 프로그래밍
- [비동기 파이썬](https://mingrammer.com/translation-asynchronous-python/)  
- [asyncio : 단일 스레드 기반의 Nonblocking 비동기 코루틴 완전 정복](https://soooprmx.com/archives/6882) 
- [What does the “yield from” syntax do in asyncio and how is it different from “await”](https://stackoverflow.com/a/44273861)
- [Blocking-NonBlocking-Synchronous-Asynchronous](https://homoefficio.github.io/2017/02/19/Blocking-NonBlocking-Synchronous-Asynchronous/)

### 라이브러리 패키징
- [파이썬 프로젝트 시작하기 - Setuptools](http://www.flowdas.com/blog/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-setuptools/)
    - [setuptools - python_requires](https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires)

### 표준 라이브러리
#### Data Types
- [datetime](https://www.programiz.com/python-programming/datetime)
    - [Find Monday's date with Python](https://stackoverflow.com/a/1622052)  
    - [Python: get all months in range?](https://stackoverflow.com/questions/35650793/python-get-all-months-in-range)
- [collections.OrderedDict](https://pymotw.com/2/collections/ordereddict.html)  
- [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)  
- [얕은 복사(shallow copy) vs 깊은 복사(deep copy)](https://blueshw.github.io/2016/01/20/shallow-copy-deep-copy/)  
- [enum](https://docs.python.org/3/library/enum.html)  
#### Structured Markup Processing Tools
- [xml.etree.ElementTree](https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2)  
#### Data Persistence
- [pickle](https://www.datacamp.com/community/tutorials/pickle-python-tutorial)  
#### Python Runtime Services
- [abc](https://velog.io/@city7310/abc)  
#### Generic Operating System Services
- [logging](https://realpython.com/python-logging/)
    - [파이썬 로깅의 모든 것](https://hamait.tistory.com/880)
    - [logging.info doesn't show up on console but warn and error do](https://stackoverflow.com/questions/11548674/logging-info-doesnt-show-up-on-console-but-warn-and-error-do/11548754)
#### File and Directory Access
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [os.path](https://docs.python.org/3/library/os.path.html)
- [glob](https://docs.python.org/3/library/glob.html)
#### Functional Programming Modules
- [functools](https://www.journaldev.com/17550/python-functools)
    - [What does functools.wraps do?](https://stackoverflow.com/questions/308999/what-does-functools-wraps-do)
    - [How does the functools partial work in Python?](https://stackoverflow.com/questions/15331726/how-does-the-functools-partial-work-in-python)
- [operator](https://docs.python.org/ko/3.7/library/operator.html)
#### Debugging and Profiling
- [timeit](https://docs.python.org/3/library/timeit.html)  
- [Python Debugging with Pdb](https://realpython.com/python-debugging-pdb/)  
#### Development Tools
- [typing](https://docs.python.org/3/library/typing.html)
    - [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)  
    - [PEP 526 -- Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)
    - [Python Type Hinting and Static Type Checking](https://www.pycon.kr/program/talk-detail?id=5)
    - [the state of type hints in Python](https://www.bernat.tech/the-state-of-type-hints-in-python/)
    - [pyright](https://github.com/Microsoft/pyright)
    - [mypy](http://mypy-lang.org/)
    - [Type hinting in Python 2](https://stackoverflow.com/questions/35230635/type-hinting-in-python-2)
    - [Python type hinting without cyclic imports](https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports)
- [unittest](https://docs.python.org/3/library/unittest.html)
    - [Unit test: Assert logger warning thrown](https://stackoverflow.com/questions/20715042/python-2-7-unit-test-assert-logger-warning-thrown)
    - [Using Python mock to spy on calls to an existing object](https://stackoverflow.com/questions/18869141/using-python-mock-to-spy-on-calls-to-an-existing-object)
#### Concurrent Execution
- [Intro to Threads and Processes in Python](https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b)  
- [파이썬의 새로운 병렬처리 API – Concurrent.futures](https://soooprmx.com/archives/5669)
#### Networking and Interprocess Communication
- [asyncio : 단일 스레드 기반의 Nonblocking 비동기 코루틴 완전 정복](https://soooprmx.com/archives/6882)
#### Data Compression and Archiving
- [gzip](https://docs.python.org/3/library/gzip.html)  
#### Internet Data Handling
- [JSON - The Hitchhiker's Guide to Python](https://docs.python-guide.org/scenarios/json/)  
#### Internet Protocols and Support
- [UUID objects according to RFC 4122](https://docs.python.org/3/library/uuid.html)
- [webbrowser](https://docs.python.org/3.7/library/webbrowser.html)

### 외부 라이브러리
#### CLI
- [zappa](https://github.com/Miserlou/Zappa)  
- [twine](https://pypi.org/project/twine/)  
- [aws-cli](https://github.com/aws/aws-cli)  
- [click](https://github.com/pallets/click)
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
#### Dataclass Helper
- [dacite](https://github.com/konradhalas/dacite)
- [dataclass-json](https://github.com/lidatong/dataclasses-json)
#### Data Types
- [mongoquery](https://github.com/kapouille/mongoquery)
- [stringcase](https://github.com/okunishinishi/python-stringcase)
- [munch](https://github.com/Infinidat/munch)
#### Schema
- [jsonschmea](https://github.com/Julian/jsonschema)  
- [schema](https://github.com/keleshev/schema)  
- [schematics](https://github.com/schematics/schematics)  
- [cerberus](http://docs.python-cerberus.org/en/stable/usage.html#basic-usage)  
- [voluptuous](https://github.com/alecthomas/voluptuous)  
- [pydantic](https://pydantic-docs.helpmanual.io/)  
#### DB Driver
- [What's the difference between MySQLdb, mysqlclient and MySQL connector/Python?](https://stackoverflow.com/questions/43102442/whats-the-difference-between-mysqldb-mysqlclient-and-mysql-connector-python)  
- [mongo-python-driver(pymongo)](https://github.com/mongodb/mongo-python-driver)
- [motor](https://github.com/mongodb/motor)  
- [redis-py](https://github.com/andymccurdy/redis-py)
- [pymemcache](https://github.com/pinterest/pymemcache)  
#### DB Helper
- [mongoengine](https://github.com/MongoEngine/mongoengine)  
- [pypika](https://github.com/kayak/pypika)  
- [SQLAlchemy 시작하기 - Part 1](https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-1/)  
- [peewee](https://github.com/coleifer/peewee)  
- [peewee-async](https://github.com/05bit/peewee-async)\
- [PynamoDB](https://github.com/pynamodb/PynamoDB)
#### HTTP
- [requests](https://github.com/requests/requests)
- [requests-oauthlib](https://github.com/requests/requests-oauthlib)
- [yarl](https://github.com/aio-libs/yarl)
- [furl](https://github.com/gruns/furl)
- [gunicorn으로 flask에서 동시에 여러 요청 처리하기](https://winterj.me/flask-concurrency-test/)
#### Async
- [uvloop](https://github.com/MagicStack/uvloop)  
- [aiohttp로 하는 비동기 HTTP 요청](https://item4.github.io/2017-11-26/Asynchronous-HTTP-Request-with-aiohttp/)
- [aiocache](https://github.com/argaen/aiocache)  
#### Excel Processing
- [xlrd](https://github.com/python-excel/xlrd)
- [xlwd](https://github.com/python-excel/xlwt)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [xlsxwriter](https://xlsxwriter.readthedocs.io/)
- [pyexcelerate](https://github.com/kz26/PyExcelerate)
- [파이썬 엑셀 쓰기 라이브러리 비교](https://libsora.so/posts/python-excel-library/)
#### Drop-in Replacements
- [Arrow](https://arrow.readthedocs.io/en/latest/)  
- [ultrajson(ujson)](https://github.com/esnme/ultrajson)  
#### SaaS Helpers
- [pyfcm](https://github.com/olucurious/PyFCM)  
- [python-firebase](https://github.com/ozgur/python-firebase)  
- [firebase-admin-python](https://github.com/firebase/firebase-admin-python)  
- [elasticsearch-py](https://github.com/elastic/elasticsearch-py)  
- [elastic-apm](https://github.com/elastic/apm-agent-python)  
- [slacker](https://github.com/os/slacker)  
- [boto3](https://github.com/boto/boto3)  
#### Crawling
- [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/)  
#### Testing
- [sure](https://github.com/gabrielfalcao/sure)
- [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio)
- [responses](https://github.com/getsentry/responses)
#### Others
- [pyjwt](https://github.com/jpadilla/pyjwt)  
- [cachetools](https://github.com/tkem/cachetools)  
- [blinker](https://pythonhosted.org/blinker/)  
- [apscheduler](https://github.com/agronholm/apscheduler)  

### SQLAlchemy
- [SQLAlchemy 시작하기 - Part 1](https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-1/)
- [SQLAlchemy 시작하기 - Part 2](https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-2/)  
- [Flask-SQLAlchemy docs - Multiple Databases with Binds](http://flask-sqlalchemy.pocoo.org/2.3/binds/#binds)  
- [SQLAlchemy에서 모든 테이블의 모든 자료 지우기](https://item4.blog/2016-03-30/Truncate-All-Tables-with-SQLAlchemy/)  
    memo : truncate하는 raw query는 FK 문제로 인해 잘 안 될 수 있으므로 SQLAlchemy를 통해 극복하는 내용
#### ORM
- [Basic Relationship Patterns](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html)  
- [SQLAlchemy's "Lazy" Parameter](https://medium.com/@ns2586/sqlalchemys-relationship-and-lazy-parameter-4a553257d9ef)  
- [Column and Data Types](https://docs.sqlalchemy.org/en/latest/core/type_basics.html)
- [synonym](https://docs.sqlalchemy.org/en/13/orm/mapped_attributes.html#synonyms)
#### Query
- [Literal SELECT](https://stackoverflow.com/a/7546802)  
- [Query 객체로 WHERE절 작성하기(Common filter operators)](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators)  
- [How to pass a not like operator in a sqlalchemy ORM query](https://stackoverflow.com/a/5019427)  
- [sqlalchemy.orm.query.Query.slice(start, stop)](https://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.slice)  
- [How to union two subqueries in SQLAlchemy](https://stackoverflow.com/a/20032394)  
- [How to execute raw SQL in SQLAlchemy](https://stackoverflow.com/a/17987782)  
- ['select as' in SQLAlchemy](https://stackoverflow.com/a/9187589)  
- [SQLAlchemy simple example of sum, average, min, max](https://stackoverflow.com/a/11832380)  
- [Get the number of rows in table using SQLAlchemy](https://stackoverflow.com/a/10822842)  
- [What's the difference between filter and filter_by in SQLAlchemy?](https://stackoverflow.com/a/2128558)  
- [How to implement a default condition in all SQLAlchemy's queries](https://stackoverflow.com/questions/40193259/how-to-implement-a-default-condition-in-all-sqlalchemys-queries)
- [SQLAlchemy Docs - ORM Events - Query Events](https://docs.sqlalchemy.org/en/latest/orm/events.html#query-events)
#### Engine, Connection, Session
- [SQLAlchemy: engine, connection and session difference](https://stackoverflow.com/a/34364247)  
- [Avoiding boilerplate session handling code in SQLAlchemy functions](https://stackoverflow.com/a/29805305)  
- [Contextual/Thread-local Sessions](https://docs.sqlalchemy.org/en/latest/orm/contextual.html)  
- [Dealing with duplicate primary keys on insert in SQLAlchemy](https://stackoverflow.com/a/11620706)  
- [SQLAlchemy Transaction 관리 Practice 공유](https://blog.qodot.me/post/sqlalchemy-transaction-%EA%B4%80%EB%A6%AC-practice-%EA%B3%B5%EC%9C%A0/)  
- [Unbind object from session](https://stackoverflow.com/questions/11213665/unbind-object-from-session/11213780)  
- [Session Management - Refreshing / Expiring](https://docs.sqlalchemy.org/en/latest/orm/session_state_management.html#refreshing-expiring)
- [How to close sqlalchemy connection in MySQL](https://stackoverflow.com/questions/8645250/how-to-close-sqlalchemy-connection-in-mysql)  
### Peewee
- [Dynamically defining a database](http://docs.peewee-orm.com/en/latest/peewee/database.html#dynamically-defining-a-database)  
- [How to custom the table name in peewee?](https://stackoverflow.com/a/48024676)  
- [Performing simple joins](http://docs.peewee-orm.com/en/latest/peewee/relationships.html#performing-simple-joins)  
- [Joining multiple tables](http://docs.peewee-orm.com/en/latest/peewee/relationships.html#joining-multiple-tables)  
### MongoEngine
### Zappa
- [Enabling CORS](https://github.com/Miserlou/Zappa#enabling-cors)  
- [Scheduling](https://github.com/Miserlou/Zappa#scheduling)  
- [X-Ray Tracing](https://github.com/Miserlou/Zappa#aws-x-ray)  
### boto3
- [When to use a boto3 client and when to use a boto3 resource?](https://stackoverflow.com/a/39273710)  
- [boto3 - credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#configuring-credentials)  
- [Upload-Download File From S3 with Boto3](https://qiita.com/hengsokvisal/items/329924dd9e3f65dd48e7)  
- [How do I get the file/key size in boto S3?](https://stackoverflow.com/a/5498841)  
## Golang
### 언어 자체에 대한 이야기
- [고루틴은 어떻게 동작하는가?](https://stonzeteam.github.io/How-Goroutines-Work/)

## Java
### 언어 자체에 대한 이야기
- [Evolution of Strings in Java to Compact Strings and Indify String Concatenation](https://arnaudroger.github.io/blog/2017/06/14/CompactStrings.html)

# AWS
- [AWS 101 : Regions and Availability Zones](https://blog.rackspace.com/aws-101-regions-availability-zones)  
## AWS Docker
- [minio - ](https://github.com/minio/minio)
## 컴퓨팅
### EC2
- [EC2(Elastic Compute Cloud)](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/concepts.html)  
- [인스턴스 수명 주기](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html)
- [인스턴스 유형](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/instance-types.html)  
- [인스턴스 구입 옵션](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/instance-purchasing-options.html)  
- [Application Load Balancer 서비스 공개](https://aws.amazon.com/ko/blogs/korea/new-aws-application-load-balancer/)  
- [배치 그룹(Placement Gorup)](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/placement-groups.html)  
#### EBS
- [EBS(Elastic Block Storage)](https://aws.amazon.com/ko/ebs/?nc=sn&loc=1)  
- [EBS 최적화 인스턴스](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/EBSOptimized.html#enable-ebs-optimization)  
#### ELB
- [Application Load Balancer 시작하기](https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/application/application-load-balancer-getting-started.html)  
- [Application Load Balancer를 통한 경로 기반 라우팅 사용](https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/application/tutorial-load-balancer-routing.html)  
### ECS
- [ECS(Elastic Container Service)](https://docs.aws.amazon.com/ko_kr/AmazonECS/latest/developerguide/Welcome.html)  
- [Fargate](https://aws.amazon.com/ko/blogs/korea/aws-fargate/)  
### ECR
- [ECR(Elastic Container Repository)](https://aws.amazon.com/ko/ecr/)  
### Lambda
- [Lambda](https://aws.amazon.com/ko/lambda/features/)  
- [Lambda Function Versioning and Aliases](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html)
### EKS
- [Demo: Easy AWS EKS cluster provisioning and user access](https://www.youtube.com/watch?v=ITzAkaRAgG4)
- [HashiCorp AWS EKS Introduction](https://learn.hashicorp.com/terraform/aws/eks-intro)
## 스토리지
### S3
- [S3 Storage Classes](https://aws.amazon.com/ko/s3/storage-classes/)  
- [버킷 정책 예제 - 특정 IP 주소 액세스 제한](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-3)
- [버킷 정책 예제 - Amazon CloudFront 오리진 자격 증명에 권한 부여](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-6)  
### EFS
- [EFS(Elastic File System)](https://aws.amazon.com/ko/efs/)  
## 데이터베이스
### RDS
### Aurora
- [Aurora Serverless - Features, Limitations, Glitches](https://medium.com/searce/amazon-aurora-serverless-features-limitations-glitches-d07f0374a2ab)  
- [Aurora 로컬 스토리지 성능 테스트](http://woowabros.github.io/r-d/2019/03/22/localstorage.html)
### DynamoDB
### ElastiCache
### DocumentDB
- [Amazon DocumentDB 신규 출시](https://aws.amazon.com/ko/blogs/korea/new-amazon-documentdb-with-mongodb-compatibility-fast-scalable-and-highly-available/)  
### TimeStream
- [TimeStream](https://aws.amazon.com/ko/timestream/)  
## 마이그레이션, 전송
### DMS
- [DMS(Database Migration Service)](https://aws.amazon.com/ko/dms/)  
### Snowball
- [Snowball](https://aws.amazon.com/ko/snowball/)  
## 네트워킹
### VPC
- [만들면서 배우는 AWS VPC 입문](https://www.44bits.io/ko/post/understanding_aws_vpc)
### CloudFront
### Route 53
### API Gateway
### Direct Connect
## PaaS
### CodeStar
- [AWS CodeStar로 1인 DevOps 코스프레하기](https://www.holaxprogramming.com/2017/10/16/devops-aws-codestar/)
### CodeCommit
- [AWS CodeCommit](https://docs.aws.amazon.com/ko_kr/codecommit/latest/userguide/welcome.html#welcome-introducing)  
### CodeBuild
- [AWS CodeBuild](https://docs.aws.amazon.com/ko_kr/codebuild/latest/userguide/welcome.html)  
- [CodeBuild의 build spec reference](https://docs.aws.amazon.com/ko_kr/codebuild/latest/userguide/build-spec-ref.html)  
- [Environment variables not being set on AWS CodeBuild](https://stackoverflow.com/questions/50706276/environment-variables-not-being-set-on-aws-codebuild)  
### CodeDeploy
- [AWS CodeDeploy를 통한 배포 자동화](http://blog.dramancompany.com/2017/04/aws-code-deploy%EB%A5%BC-%ED%86%B5%ED%95%9C-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94/)  
## 관리
### CloudWatch
- [일정에서 트리거되는 CloudWatch 이벤트 규칙 생성](https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Scheduled-Rule.html)  
- [사용자 지정 메트릭 게시(put-metric-data)](https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
### Auto Scaling
## 분석
### Athena
### Redshift
### EMR
### ElasticSearch Service
### Kinesis
## 보안, 자격 증명
### IAM
- [AWS IAM](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/introduction.html)  
- [Difference between IAM role and IAM user in AWS](https://stackoverflow.com/a/48182754)  
### KMS
### WAF
- [AWS WAF](https://aws.amazon.com/ko/waf/)  
## 어플리케이션 통합
### Step Functions
### Amazon MQ
### SNS
### SQS

## 고객 참여
### SES
- [Amazon SES에서 이메일 전송 테스트](https://docs.aws.amazon.com/ko_kr/ses/latest/DeveloperGuide/mailbox-simulator.html)  

# 모바일
- [배달의민족 앱에 적용된 오프라인 모드에 대하여](http://woowabros.github.io/experience/2018/11/05/about_offline_mode.html)
- [회사나 고객에게 효과적으로 Flutter 소개하는 방법을 알려드립니다](https://developers-kr.googleblog.com/2019/01/pitching-flutter.html?fbclid=IwAR1b8eLPhcZDvXTTr_x0rhVWSOVP8gkJxBThmcHX2Ktvro0OKw5blX7PFM8)
## Android
- [Android 공식 가이드](https://developer.android.com/guide/index.html?hl=ko)
- [Android의 HTTP 클라이언트 라이브러리](http://d2.naver.com/helloworld/377316)
- [Using Retrofit 2.x as REST client](http://www.vogella.com/tutorials/Retrofit/article.html)
- [Retrofit 2와 함께하는 정말 쉬운 HTTP](https://academy.realm.io/kr/posts/droidcon-jake-wharton-simple-http-retrofit-2/)  
- [Firebase를 실제 모바일 백엔드로 사용하면 일어날 수 있는 일들](https://academy.realm.io/kr/posts/firebase-as-a-real-mobile-backend/)
- [Android의 ORM](http://d2.naver.com/helloworld/472196)
- [Android의 이미지로딩 라이브러리](http://d2.naver.com/helloworld/429368)
- [Android 앱 메모리 최적화](http://d2.naver.com/helloworld/539525)
- [안드로이드 BadTokenException의 원인과 해결방법](https://blog.sangyoung.me/2016/12/28/BadTokenException/)  
- [Android와 개발 패턴](https://tosslab.github.io/android/2015/03/01/01.Android-mvc-mvvm-mvp)
- [안드로이드의 MVC, MVP, MVVM 종합 안내서](https://academy.realm.io/kr/posts/eric-maxwell-mvc-mvp-and-mvvm-on-android/?fbclid=IwAR0aQa3j7nSTgB5TMsFt33iviV8ReW0oGvkvVBucWrBcgV0v6XWsKwjljhI)
- [AWS codebuild + codecov 로 저렴하게 android CI 구축하기](https://medium.com/@SungMinLee/aws-codebuild-codecov-%EB%A1%9C-%EC%A0%80%EB%A0%B4%ED%95%98%EA%B2%8C-android-ci-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-2a209651c4f7)
- [클린 아키텍처와 함께하는 배민앱 (Android)](http://woowabros.github.io/experience/2019/01/17/baeminapp-clean-architecture.html?fbclid=IwAR3GrdvlbN0uCcZJsGgh3jUpv6vF2T0rCBEZ7EdUIy-J3Hogio7XjhXr6jQ)
- [epoxy](https://github.com/airbnb/epoxy)
- [Use Android Jetpack to Accelerate Your App Development](https://android-developers.googleblog.com/2018/05/use-android-jetpack-to-accelerate-your.html?m=1)  
## iOS

# 웹 프론트엔드
## 코딩 없이 웹페이지 개발
- [Webflow](https://webflow.com/)
## 웹 프로그래밍 자체
- [웹 프로그래밍 튜토리얼 | PoiemaWeb](https://poiemaweb.com/)
- [Index fun](https://psuter.net/2019/07/07/z-index?utm_source=share&utm_medium=ios_app&fbclid=IwAR0NXcIo0R_qqEb6PZGK0nvx89ZO6mgf9A1FKiTabWQntAR7Fd-RdCHX5Hw)
## Deploy
- [Surge](https://surge.sh/)
- [Netlify](https://www.netlify.com/)
- [Vercel](https://vercel.com/)
## CSS
### PostCSS
- [PostCSS](https://medium.com/@FourwingsY/postcss-%EC%86%8C%EA%B0%9C-727310aa6505)
- [webpack3 + postcss 설정하기](https://medium.com/@FourwingsY/webpack-postcss-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0-34f9c486093a)
### Sass
- [Sass 강좌 - 한 눈에 보기](https://velopert.com/1712)
### FlexBox
- [(번역) CSS flex box 3분만에 배우기](https://joshuajangblog.wordpress.com/2016/09/19/learn-css-flexbox-in-3mins/)
- [플렉스 박스 레이아웃](https://poiemaweb.com/css3-flexbox)
- [flexbox로 만들 수 있는 10가지 레이아웃](https://d2.naver.com/helloworld/8540176)
## React
- [Learning React 예제 한국어 번역](https://github.com/enshahar/learning-react-kor)
- [한국어로 배우는 리엑트](https://github.com/reactkr/learn-react-in-korean)
- [React Bit](https://github.com/vasanthk/react-bits)
- [Awesome React Components](https://github.com/brillout/awesome-react-components)
- [네이버 메일 모바일웹 리엑트 적용기](http://d2.naver.com/helloworld/4966453)
- [React 인가 Vue 인가?](https://joshua1988.github.io/web_dev/vue-or-react/)
- [[번역] React를 본격적으로 하기 전 알면 좋은 6가지](https://jaeyeophan.github.io/2018/01/02/React-tips-for-beginners/)
- [React 프로젝트의 디렉토리 구조](https://medium.com/@FourwingsY/react-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%9D%98-%EB%94%94%EB%A0%89%ED%86%A0%EB%A6%AC-%EA%B5%AC%EC%A1%B0-bb183c0a426e)
- [카카오페이지 웹 React 포팅 후기](https://medium.com/@ljs0705/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%8E%98%EC%9D%B4%EC%A7%80-%EC%9B%B9-react-%ED%8F%AC%ED%8C%85-%ED%9B%84%EA%B8%B0-76402cc5e031)
- [When a rewrite isn’t: rebuilding Slack on the desktop](https://slack.engineering/rebuilding-slack-on-the-desktop-308d6fe94ae4)
## TypeScript
- [우리(Reddit)가 Typescript를 선택한 이유](https://medium.com/@constell99/%EC%9A%B0%EB%A6%AC%EA%B0%80-typescript%EB%A5%BC-%EC%84%A0%ED%83%9D%ED%95%9C-%EC%9D%B4%EC%9C%A0-b0a423654f1e)
- [Conditional types in Typescript](https://artsy.github.io/blog/2018/11/21/conditional-types-in-typescript/)
