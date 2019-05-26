# Lets-Study
나만 읽기 아까운 글이나 문서를 모아두는 공간입니다. 어떤 주제를 공부하거나, 공부의 방향을 잡거나, 그냥 가볍게 읽기 위한 재밌는 글을 원하는 누군가가, 양질의 글에 쉽게 접근할 수 있도록 도와주는 것이 이 저장소의 목적입니다.

의식의 흐름으로 나눈 카테고리에, 링크로 이루어진 리스트 형태로 구성됩니다. 일단 링크 막 모아두고, 한번 읽고 나면 이게 어떤 글이고 왜 추천하는지를 간략하게 작성하고 있습니다.

여러분도 북마크에서 몇 개만 공유해 주세요. 레포 주인이 공부하는 분야가 넓지 않아서, 별 거 아닌 것처럼 보이는 기여더라도 큰 도움이 됩니다.

# 배경지식
## 프로그래밍
### 동시성 프로그래밍
- [파이썬과 비동기 프로그래밍 시리즈](https://velog.io/@sjquant/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B3%BC-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-1-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80)
- [멈추지 않고 기다리기(Non-blocking)와 비동기(Asynchronous) 그리고 동시성(Concurrency)](https://tech.peoplefund.co.kr/2017/08/02/non-blocking-asynchronous-concurrency.html)  
    파일이나 네트워크 등과 같은 I/O bound 작업에 대해 처리의 완료를 기다리지 않고, 후속 작업을 처리하는 부분만 콜백이나 await 등을 통해 따로 정의해둔 채 CPU를 다른데서 계속 써먹으며 자원 낭비를 줄이는 패턴을 Non-blocking IO라고 부르고, Non-blocking IO는 Async IO라고도 부른다고 한다. + 프로그램의 주 실행 흐름(메인 루틴)을 최대한 적게 멈추면서 뭐라도 계속 처리하는 걸 Async programming이라 부르고, 이를 위한 재료로서 Non-blocking IO를 활용할 수 있으나 둘은 관점이 다르기에 비교 대상이 되기는 어렵다는 내용. 비동기 IO에 비해 비동기 프로그래밍은 좀 더 추상적인 개념인 듯 하다.
### 함수와 관련된 얘기, 함수형 프로그래밍
- [함수형 프로그래밍이란?](https://medium.com/@lazysoul/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80-d881230f2a5e)
- [Higher-order-function(고차함수) with Kotlin](https://medium.com/@lazysoul/high-order-function-%EA%B3%A0%EC%B0%A8%ED%95%A8%EC%88%98-22b147d0c4a5)  
    인자로 함수를 취하거나, 결과로 함수를 반환하는 함수. HOF라고도 부른다. 이게 수학에서도 있는 개념이라고 함. Java에서 메소드에 overrided method가 포함된 익명 클래스를 만들며 그 객체를 넘겨주는 것도 HOF라고 부를 수 있을까?
- [Currying](http://planbs.tistory.com/entry/Currying)  
    f(x, y, z)를 f(x), g(y), h(z)와 같은 함수 체인으로 만드는 기법. '인자가 미리 채워진 함수'를 만들어 코드의 추상화 레벨을 높이기 위해 써볼만 하지만, 내 경우에는 currying의 주 목표인 '인자를 나누어 함수의 처리를 점차 진행시킨다'를 만족시킬만한 함수를 작성하는 경우가 거의 없었던 것 같다. 차라리 partial function을 쓰는 경우가 더 많은 듯.
- [함수형 프로그래밍: partial application과 curry](https://rhostem.github.io/posts/2017-04-20-curry-and-partial-application/)  
    partial application, currying의 소개와 둘의 차이를 설명한다. partial application은 특정 인자를 고정시킨 새로운 함수를 만드는 기법. 수학의 부분 정의 함수와 연관이 있는 것 같다.
- [람다, 익명 함수, 클로저](https://hyunseob.github.io/2016/09/17/lambda-anonymous-function-closure/)  
    람다, 익명 함수, 클로저를 연관지어 매우 깔끔하게 설명해 두었다. 클로저는 closer가 아니고 closure(폐쇄)이며, 함수형 트릭이 아니라 개념(함수와 그 함수가 선언된 lexical scope의 조합)이다. 클로저는 자신이 정의된 문맥에서 주변의 변수와 상수들을 캡처한다.
- [자바스크립트의 호이스팅(Hoisting)](http://asfirstalways.tistory.com/197)  
    웬만한 언어에서 declaration은 호이스팅되고, assignment는 호이스팅되지 않는 것 같다. 대부분 호이스팅이 '작성한 코드의 상단으로 옮겨지는' 것으로 설명되지만, 그냥 컴파일 단계에서 평가되기 때문에 그렇게 보여지는 것이다.
- [코루틴 소개](https://medium.com/@jooyunghan/%EC%BD%94%EB%A3%A8%ED%8B%B4-%EC%86%8C%EA%B0%9C-504cecc89407)  
    프로그램의 메인 실행 흐름을 메인루틴이라 부르고, 일반적인(call/return 형태의) 함수는 서브루틴이라 부른다. 여기서 이 함수가 suspend/resume 기능을 지원한다면 이를 코루틴이라 부른다. suspend로 제어를 양도하고, resume으로 다시 실행을 재개하는 형태. async/await도 사실상 이런 개념 기반이므로 비동기에 코루틴을 종종 써먹는 듯. 그래서 아무튼 함수는 서브루틴 형태와 코루틴 형태로 나뉘며 코루틴은 또다시 대칭/비대칭 코루틴으로 나눌 수 있다.
- [Function scopes and block scopes in JavaScript](https://edgecoders.com/function-scopes-and-block-scopes-in-javascript-25bbd7f293d7)  
    JavaScript에서 var는 function scope에서 보장되고, let는 block scope가 가능하다는 이야기인데, scope는 애초에 프로그래밍 언어 자체적인 이야기라 볼만 하다. function/block scope, lexical(static)/dynamic scope 등등..
- [What is a pure function?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976)  
    same input-same output과 외부 상태에 변화를 주지 않는(no side-effect) 함수를 순수 함수(pure function)라고 부른다.
### 테스팅
- [유닛테스트에 대한 생각](https://blog.outsider.ne.kr/1275?fbclid=IwAR1Z9DPi-JJns_bSccrNZIo8zFo-0B8nAvIEHen3tu0_jaIUS34hY90FVJ0)  
    '테스트를 작성하면 내가 작성한 메서드나 클래스의 사용자 입장이 되는 기분이 든다.'
- [코드 커버리지 80% 넘긴 썰 - 테스팅을 잘 하기 위한 8퍼센트 개발팀의 삽질기](https://brunch.co.kr/@leehosung/43)
- [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
- [Classical vs Mockist testing](https://agilewarrior.wordpress.com/2015/04/18/classical-vs-mockist-testing/)  
    `Mocks Aren't Stubs` 글의 요약본.
- [Testing Without Mocks: A Pattern Language](https://www.jamesshore.com/Blog/Testing-Without-Mocks.html)
- [단위 테스트 케이스와 테스트 더블(Test Double)](https://medium.com/@SlackBeck/%EB%8B%A8%EC%9C%84-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%BC%80%EC%9D%B4%EC%8A%A4%EC%99%80-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%8D%94%EB%B8%94-test-double-2b88cccd6a96)
- [Mock Object란 무엇인가?](https://medium.com/@SlackBeck/mock-object%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-85159754b2ac)  
    behavior verification과 state verification, 거기서 뻗어나오는 test double인 mock과 stub까지 잘 설명되어 있다.
- [What's the difference between a mock & stub?](https://stackoverflow.com/questions/3459287/whats-the-difference-between-a-mock-stub)
### 패턴
#### 디자인 패턴
- [So Singletons are bad, then what?](https://softwareengineering.stackexchange.com/questions/40373/so-singletons-are-bad-then-what)
- Repository Pattern
    - [Repository Design Pattern](https://medium.com/@pererikbergman/repository-design-pattern-e28c0f3e4a30)
    - [repository pattern vs ORM](https://stackoverflow.com/questions/10155517/repository-pattern-vs-orm)
    - [Stop using repository pattern with an ORM](http://hamidmosalla.com/2018/11/25/stop-using-repository-pattern-with-an-orm/)
    - [Don't use DAO, use Repository](https://thinkinginobjects.com/2012/08/26/dont-use-dao-use-repository/)
- Dependency Injection
    - [What is dependency injection?](https://stackoverflow.com/questions/130794/what-is-dependency-injection)
    - [Dependency Injection Demystified](https://www.jamesshore.com/Blog/Dependency-Injection-Demystified.html)
    - [DI 란?](https://gmlwjd9405.github.io/2018/11/09/dependency-injection.html)  
        DI 를 처음 만나 헤매는 사람들에게 매우 좋은 글이다. 코드와 다이어그램으로 적절한 예시를 들어서 쉽게 이해할 수 있다.
    - [Dependency Injection in Python](https://medium.com/@shivama205/dependency-injection-python-cb2b5f336dce) 
    - [Pinject](https://github.com/google/pinject)  
        구글이 만든 Python DI library  
        `"Dependency Injection" is a 25-dollar term for a 5-cent concept.`
#### 아키텍처 패턴
- [10가지 소프트웨어 아키텍처 패턴](https://mingrammer.com/translation-10-common-software-architectural-patterns-in-a-nutshell/)  
    서비스 관점에서의 패턴 이야기가 아니라, 그냥 아키텍처 자체에 대한 이야기. 역시 패턴 얘기는 재밌는 게 많다.
- [Circuit breaker 패턴을 이용한 장애에 강한 MSA 서비스 구현하기](https://bcho.tistory.com/1247)
### 언어론과 가까운 이야기
- [Exression verses Statement](https://stackoverflow.com/a/19224)  
    expression은 identifier, literal, operator만을 포함하며 value를 산출하는 식이고, statement는 동작을 수행하는 문이다.  
    - Python의 삼항 연산자는 expression이다. - `res = 1 if True else 0`
    - JavaScript에서 함수는 expression으로 사용할 수 있다. - `const sum = function(a, b) { return a + b; };`
    - Kotlin의 when 절은 expression과 statement로 모두 사용할 수 있다.
- [Static/Dynamic vs Strong/Weak](https://stackoverflow.com/a/2351203)  
    정적/동적 타입 검사와 강타입/약타입에 대한 이야기. static/dynamic typing은 'when type information is acquired', strong/weak typing은 'how strictly types are distinguished'로 요약하고 있다.
- [Runtime vs Compile time](https://stackoverflow.com/a/846421)  
    런타임과 컴파일 타임의 비교.
### 좋은 코드를 작성하기 위한 노력
- [DRY code vs. WET code](https://www.codementor.io/joshuaaroke/dry-code-vs-wet-code-89xjwv11w)  
    소프트웨어 개발 원칙 중 하나지만, DRY 원칙을 지키는 건 프로그래밍의 기본이 아닐까 싶다.
- [Red-Green-Refactor](https://www.jamesshore.com/Blog/Red-Green-Refactor.html)
- [객체지향 개발 5대 원리: SOLID](http://www.nextree.co.kr/p6960/)
### 정규 표현식
- [정규표현식의 개념과 기초 문법](https://soooprmx.com/archives/7718)
- [regexr - 정규표현식을 연습할 수 있는 playground](https://regexr.com/)
- [ignore case sensitivity](https://stackoverflow.com/questions/9655164/regex-ignore-case-sensitivity)
### 캐싱
- [What is difference between LRU and LFU?](https://stackoverflow.com/a/29225598)  
    캐시 구현 방법 중 LRU(Last Recently Used)와 LFU(Last Frequently Used) 캐시의 차이에 대한 설명이다. 이 외로 rr cache, ttl cache가 있다.
- [WTF is Memoization](https://medium.com/@chialunwu/wtf-is-memoization-a2979594fb2a)  
    'Avoid doing the same work repeatedly to avoid spending unnecessary running time or resource'
- [What is the difference between Caching and Memoization?](https://stackoverflow.com/a/6469470)  
    Caching은 'general term', Memoization은 'specific form of caching'
- [캐시가 동작하는 아주 구체적인 원리](https://parksb.github.io/article/29.html?utm_source=gaerae.com&utm_campaign=%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%8A%A4%EB%9F%BD%EB%8B%A4&utm_medium=social&fbclid=IwAR2QTpnMNc9fbjbnj6SQWf_VQwJznCBUQ_4NWovcGXXugl-Nd2hDj44JoXI)
### 기타
- [Why is global state so evil?](https://softwareengineering.stackexchange.com/questions/148108/why-is-global-state-so-evil)  
    전역 변수가 왜 나쁜지에 대한 이야기
- [Drop-in replacement](https://en.wikipedia.org/wiki/Drop-in_replacement)  
    적은 노력으로 보안/성능/기능/확장성을 향상시키는 것. 예로 Python의 빌트인 시간 라이브러리인 datetime의 drop-in replacement로 arrow, pendulum이 있다.
- [점진적인 레거시 웹 어플리케이션 개선 과정](https://www.slideshare.net/arawnkr/ss-115339631)
- [알아두면 좋은 이메일마케팅 지표](https://blog.stibee.com/%EC%95%8C%EC%95%84%EB%91%90%EB%A9%B4-%EC%A2%8B%EC%9D%80-%EC%9D%B4%EB%A9%94%EC%9D%BC-%EB%A7%88%EC%BC%80%ED%8C%85-%EC%A7%80%ED%91%9C-92161806525f0)  
    이메일의 반송(Bounce)와 관련된 이야기.

## 프로토콜, 표준
### HTTP
- [WebSocket과 Socket.io](https://d2.naver.com/helloworld/1336)  
    결국 웹소켓의 요지는 polling을 push 방식으로 만든다는 건데, HTTP/2.0의 server push 기능이 어느정도 웹소켓을 흉내낼 수 있지 않을까 싶었다.
- [웹 기술로 구현하는 Adaptive HTTP Streaming](https://meetup.toast.com/posts/1310)  
    웹 클라이언트에서의 스트리밍 관련 표준은 MSE(Media Source Extensions). DASH가 MSE에 잘 맞춰진 표준이며 널리 사용되고 있지만 모바일 safari는 MSE를 지원하지 않기 때문에 DASH와 HLS를 같이 지원해줘야 할듯? 토이 프로젝트 해봐야겠다.
#### REST
- [REST API 제대로 알고 사용하기](http://meetup.toast.com/posts/92)
- 그런 REST API로 괜찮은가
    - [그런 REST API로 괜찮은가 - 발표자료](http://slides.com/eungjun/rest#/)
    - [그런 REST API로 괜찮은가 - 영상](https://tv.naver.com/v/2292653)
- [REST 의 Uniform Interface에 대하여](http://midnightcow.tistory.com/entry/REST-What-is-REST-2)  
    Uniform Interface 는 REST 에서 가장 기본적인 제약이다. 이는 다음 4가지로 구성되어 있다.  
    - Resource Identifier  
    - Resource Representation
    - Self-Descriptive message
    - hypermedia as the engine of application state (HATEOAS)
- [바쁜 개발자들을 위한 REST 논문 요약](https://blog.npcode.com/2017/03/02/%EB%B0%94%EC%81%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%93%A4%EC%9D%84-%EC%9C%84%ED%95%9C-rest-%EB%85%BC%EB%AC%B8-%EC%9A%94%EC%95%BD/)  
    Uniform Interface 를 사용하여 클라이언트-서버간의 인터페이스를 일반화함으로써, 전체 시스템 아키텍처가 단순해지고, 상호작용의 가시성이 개선되며, 구현과 서비스가 분리되므로 독립적인 진화가 가능해진다. 이 스타일에 따르면, REST API는 기본 URI와 미디어 타입의 정의만 알면 이용할 수 있어야한다.
#### GraphQL
- [So what’s this GraphQL thing I keep hearing about?](https://medium.freecodecamp.org/so-whats-this-graphql-thing-i-keep-hearing-about-baf4d36c20cf)
- [GraphQL을 오해하다](https://medium.com/@FourwingsY/graphql%EC%9D%84-%EC%98%A4%ED%95%B4%ED%95%98%EB%8B%A4-3216f404134)
- [GraphQL 뮤테이션 디자인](https://dev-blog.apollodata.com/designing-graphql-mutations-e09de826ed97)
#### HTTP2/HTTPS
- [HTTPS는 HTTP보다 빠르다](https://tech.ssut.me/https-is-faster-than-http/)
- [나만 모르고 있던 HTTP2](http://www.popit.kr/%EB%82%98%EB%A7%8C-%EB%AA%A8%EB%A5%B4%EA%B3%A0-%EC%9E%88%EB%8D%98-http2/)  
    아니 뭐 이렇게까지 HTTP/1.1을 까고 HTTP/2를 찬양하나 싶었는데, 이유 있는 비판인 것 같다. HTTP/2가 SPDY를 기반으로 개발되었고, 구글이 HTTP/2가 SPDY를 대체할 것이라고 발표한 것은 처음 알았다.
- [HTTP/2 소개 - Google Developers](https://developers.google.com/web/fundamentals/performance/http2/?hl=ko)  
    SPDY가 비표준 프로토콜이라는 말을 듣고 굉장히 의문적이었는데, 실험용 프로토콜이었구나. HTTP/1.1의 성능 제한을 해결해 웹페이지의 레이턴시를 줄이는 것을 목표로 SPDY가 만들어지기 시작했고, HTTP/2의 새로운 기능과 제안을 테스트하기 위해 SPDY가 계속해서 실험 수단으로 사용되었다. 이제는 SPDY가 가지고 있던 대부분의 장점이 포함된 HTTP/2가 표준으로 받아들여지면서 SPDY는 deprecated되었다고 함. high level API는 HTTP/1.x와 동일하게 유지되고, low level의 변경이 성능 문제를 해결했다. 바이너리 프레이밍 계층, 요청/응답 멀티플렉싱, 스트림과 스트림 우선순위 지정, server push, 헤더 압축 등등 + HTTP/1.x의 image sprite, 도메인 샤딩과 같은 임시 방편을 제거하고 최적화하는 기능이 들어 있다.
- [HTTPS는 어떻게 다를까?](https://parksb.github.io/article/24.html)
#### API
- [API Security Checklist-ko](https://github.com/shieldfy/API-Security-Checklist/blob/master/README-ko.md)
- [API development tools](https://github.com/yosriady/api-development-tools)
- [HTTP 응답코드 결정 다이어그램](https://github.com/for-GET/http-decision-diagram)
### JSON 관련
#### NDJSON
- [Newline delemited JSON is awesome](https://medium.com/@kandros/newline-delimited-json-is-awesome-8f6259ed4b4b)  
    'ndJSON is a collection of JSON objects, separated by `\n`'이 핵심. 종단 간 통신 레벨에서 쓰일만한 건 아닌 것 같고, JSON으로 이루어진 data collection을 관리할 때 좋을 것 같다. MongoDB에서 특정 collection에 모여 있는 document 목록은 NDJSON으로 표현할 수 있을테니까.
#### JSONSchema
- [JSONSchema](http://tcpschool.com/json/json_schema_schema)  
    JSON payload를 검증하는 데에 쓸 수 있는 JSONschema. 처음 봤을땐 뭐 이런 TMI 스펙이 다있어? 싶었는데 이젠 이거 없으면 validation이 어렵다.
- [object - pattern properties](https://json-schema.org/understanding-json-schema/reference/object.html#pattern-properties)  
    property name이 dynamic한 경우, pattern properties를 사용해볼 수 있다.
- [object - Schema dependencies](https://json-schema.org/understanding-json-schema/reference/object.html#schema-dependencies)  
    JSONSchema object에서 dependency는 '프로퍼티 A가 있으면 프로퍼티 B도 있어야 한다'와 같은 개념이다. property dependencies를 사용할 수도 있으나, schema dependencies는 그 내부에 있는 dependecy들에 대해서도 스키마를 적용할 수 있어 확장성이 더 높다.
#### JWT
- [Introduction to JSON Web Tokens](https://jwt.io/introduction/)  
    사실 HTTP에서 authentication을 위해 JWT를 사용하는 것은 표준이 아니지만(Authorization 헤더의 value type중 JWT를 위한 것은 없다. - Bearer는 OAuth 2.0의 토큰을 사용해야 하고, JWT라는 타입은 없음) 이미 많이들 사용하고 있는 사용자 인증 프레임워크.
### Protobuf
- [Protobuf](https://developers.google.com/protocol-buffers/docs/proto3)  
    `.proto`라는 확장자를 가진 파일에 스키마를 명시하고, 이걸로 직렬화/역직렬화하는 데이터 직렬화 포맷. RPC에서 많이 쓰인다고 하며 타다가 Protobuf를 쓰고 있다고 한다. HTTP mimetype에선 `application/vnd.google.protobuf`나 `application/x-protobuf`같은 걸 쓴다는데, 그냥 protobuf message를 JSON으로 주기받기도 하는 것 같다.
- [Google Protocol Buffers and HTTP](https://stackoverflow.com/questions/1425912/google-protocol-buffers-and-http)  
    'Just write the bytes of the protocol buffer directly into the request/response, and make sure to set content type to "application/octet-stream"', 'ProtoBuf is a binary protocol.'
### Date & Time
- [협정 세계시(UTC)](https://ko.wikipedia.org/wiki/%ED%98%91%EC%A0%95_%EC%84%B8%EA%B3%84%EC%8B%9C)
- [유닉스 시간](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4_%EC%8B%9C%EA%B0%84)  
    Epoch(1970-01-01T00:00:00Z)로부터의 경과 시간을 초로 환산하여 정수로 나타낸 것. 그리고 timestamp는 '시각을 나타내는 문자열'이라는 다소 큰 범위의 정의를 가지고 있어서, 1256953732같이 생긴 건 [unix time](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4_%EC%8B%9C%EA%B0%84)이라고 부르는 것이 가장 정확하다. `Sat Jul 23 02:16:57 2018`같은 것도 타임스탬프라고 부르기 때문.
- [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)  
    시각을 표기하는 곳에서 KST, CST, EDT같이 timezone에 대해서는 약어만 마주치며 살다가, PrestoDB에서 `Asia/Seoul`같은 표현을 보고 이리저리 찾아보니 timezone의 약어는 표준이 따로 없다고 한다. 그래서 timezone 약어 목록으로 가장 유명한 [Time Zone Abbreviations](https://www.timeanddate.com/time/zones/)를 찾아봤더니 `CST`가 미국 중부 표준시, 중국 표준시, 쿠바 표준시를 모두 나타내는 등의 모호함이 있었다. tz database time zones라는 이름을 가진 해당 링크는 그 이름처럼 [IANA TZDB](https://www.iana.org/time-zones)에서 사용하는 타임존 목록을 그대로 가져와 정리한 것인데, 약어 대신 `Asia/Tokyo`, `Europe/Lisbon`처럼 지역명을 사용하고 있다. 이게 타임존을 다루는 데에 사실상 가장 현실적인 방안이라고들 생각하는 것 같다.
- [ISO 8601](https://ko.wikipedia.org/wiki/ISO_8601)  
    `2018-11-13T22:36:38+09:00`처럼 생겨먹은, 시간에 대한 i18n 처리를 할 때 거론되는 날짜와 시간에 관련된 국제 표준. format이 한가지 종류가 아니라는 점(날짜를 YYYY-MM-DD로 표현하는 경우도 있고, YYYYMMDD로 표현하는 경우도 있으며 시간이 UTC라면 +00:00 대신 Z를 쓸 수 있다.)과 timezone에 대한 표기 없이 UTC와의 시차만 표현한다는 점이 흥미로웠다. 동일한 시간대에서 통신 시 지역 시간을 가정하는 것이 편할지라도, 서로 다른 시간대 간의 통신에서는 애매할 수 있을테니 ISO 8601 포맷을 사용하여 UTC에서 얼마를 더해 이 시각이 나왔는지를 알려주는 것이 좋을 것이다.
- [What's the difference between ISO 8601 and RFC 3339 Date Formats?](https://stackoverflow.com/questions/522251/whats-the-difference-between-iso-8601-and-rfc-3339-date-formats)  
    'RFC 3339 is listed as a profile of ISO 8601. Most notably RFC 3339 requires a complete representation of date and time (only fractional seconds are optional).'
### DNS
- [Demystifying DNS for web developers](https://medium.com/@jgefroh/demystifying-dns-for-web-developers-ace5a3ae559f)  
    DNS에 대해 훑어보기에 좋은 글.
- [SOA Record](https://support.dnsimple.com/articles/soa-record/)
- [NS Record](https://support.dnsimple.com/articles/ns-record/)
- [A Record](https://support.dnsimple.com/articles/a-record/)
- [AAAA Record](https://support.dnsimple.com/articles/aaaa-record/)
- [MX Record](https://support.dnsimple.com/articles/mx-record/)
- [CNAME Record](https://support.dnsimple.com/articles/cname-record/)
- [Alias Record](https://support.dnsimple.com/articles/alias-record/)
### 기타
- [How does MQTT protocol work?](https://stackoverflow.com/a/9570898)  
    일반적으로 알고 있는 pub/sub 패턴처럼, publisher는 토픽을 발행하고 subscriber는 관심 있는 토픽을 구독한다. 메시지는 broker가 관리한다. Facebook Messenger가 MQTT를 사용하는 것으로 유명하지만 지금까지도 쓰고 있는지는 잘 모르겠다. 오픈소스 MQTT 브로커로 mosquito를 사용하곤 한다. Firebase Cloud Messaging(FCM)도 MQTT 구조인가? 싶었는데 얘는 웹소켓이라고 함.
- [RSS 2.0 specification](https://validator.w3.org/feed/docs/rss2.html)  
    웹 컨텐츠 제공 형식을 표준화한 것. XML로 이루어져 있고, 각 item들은 title, link, description, author, category 등의 속성을 가질 수 있다. 블로그 게시글들을 XML화시킨 것이라고 생각하면 된다. RSS를 읽어서 잘 파싱하고 보여주는 툴이 있다면 컨텐츠를 소비하기 위해 직접 페이지에 방문하지 않아도 됨.

## 웹 관련 이야기
- [Understanding CORS](https://medium.com/@baphemot/understanding-cors-18ad6b478e2b)
- [Understanding CORS - spring.io](https://spring.io/understanding/CORS)  
    의문 1. Same Origin Policy는 도대체 무엇을 방어하기 위해 있는 것인가?  
    의문 2. CORS는 브라우저의 입장에서 무엇을 해결하기 위해 생겨난 것인가?  
    의문 3. CORS가 server side에서 특정 Origin에게만 리소스를 허용하기 위함이라면, OPTIONS에서 단지 헤더 몇개 떨궈줄 게 아니라, 그거 무시하고 그냥 API Call해버리는 것도 방어해야 하는 것 아닌가? + 그냥 요청자가 Access-Control-Allow-Origin에 들어온 값으로 Origin 헤더 변경해버리면 어떡함?  
    의문 4. Same Origin Policy가 브라우저에게 있어서 신뢰할 수 없는 origin에서 리소스를 가져오는 것을 방어하기 위함이라면, CORS가 browser side에서 other origin의 리소스를 가져올 수 있게 만들어버리니 무용지물이 아닌가?(서버에서 Access-Control-Allow-Origin을 `*`로 둔다거나 하면 브라우저가 disallow하는 게 없을테니까)

### SEO
- [검색엔진최적화(SEO) 쉬운 가이드](https://blog.usefulparadigm.com/%EA%B2%80%EC%83%89%EC%97%94%EC%A7%84%EC%B5%9C%EC%A0%81%ED%99%94-seo-%EC%89%AC%EC%9A%B4-%EA%B0%80%EC%9D%B4%EB%93%9C-f003911b0a79)
### 렌더링
- [What are the differences between server-side and client-side programming?](https://softwareengineering.stackexchange.com/a/171210)  
    서버 사이드/클라이언트 사이드 렌더링에 대한 이야기. 외국권에선 보통 rendering보단 programming이라는 단어로 통하는 것 같다.

## 소프트웨어 공학

## Git
- [git blame](https://git-scm.com/book/ko/v1/Git-%EB%8F%84%EA%B5%AC-Git%EC%9C%BC%EB%A1%9C-%EB%B2%84%EA%B7%B8-%EC%B0%BE%EA%B8%B0)  
    `git blame` 명령어를 통해 소스 코드에서 특정 line을 지정한 후 그 일부에 대해서 commit history를 찾아볼 수 있다.
- [How to resolve merge conflict during pull request?](https://stackoverflow.com/a/45819784)  
    pull request를 날렸는데 conflict가 나면 어떻게 해결해야 되는지에 대한 질문. 'Merge origin/master into JohnMaster and push this to its remote (origin/JohnMaster).' 그냥 target branch에서 pull 땡기고 merge 해결한 후 push하면 된다.
- [How do I update a GitHub forked repository?](https://stackoverflow.com/a/7244456)  
    fork한 레포를 원본 저장소와 어떻게 sync하는지에 대한 질문. 'upstream'이라는 이름으로 remote를 등록하고 `fetch upstream`하면 된다.
- [What is .gitignore exactly?](https://stackoverflow.com/a/27850270)  
    '.gitignore tells git which files (or patterns) it should ignore.' 안드로이드 프로젝트 같은데서 맨날 .idea 하위 파일들 conflict났던 기억이 있는데 gitignore가 있으면 깔끔하게 해결 가능하다.
- [.gitignore is ignored by Git](https://stackoverflow.com/a/11451731)  
    Tracked file들은 .gitignore가 생겨도 제대로 먹히지 않는다. 'Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore.'
- [git rebase -i 사용하기](https://jupiny.com/2018/05/07/git-rebase-i-option/)  
    커밋 히스토리를 정리하기 위해, 또는 커밋의 메타데이터(커밋 날짜, author 등)를 변경하기 위해 사용하는 rebase. 여러모로 쓸만한 곳이 많다.
- [How can one change the timestamp of an old commit in Git?](https://stackoverflow.com/questions/454734/how-can-one-change-the-timestamp-of-an-old-commit-in-git)  
    과거의 커밋에서 commit time을 어떻게 변경하는지에 대한 질문. 이런저런 방법 많은데 나는 `rebase`해서 `commit --amend`하는게 깔끔해 보인다.
- [How to change the commit author for one specific commit?](https://stackoverflow.com/questions/3042437/how-to-change-the-commit-author-for-one-specific-commit)  
    과거의 커밋에서 commit author를 어떻게 변경하는지에 대한 질문. 여기서도 대부분 rebase하는 식으로 가이드한다.

## Linux
- [export, echo 명령어](http://keepcalmswag.blogspot.com/2018/06/linux-unix-export-echo_49.html)
- [lsof 사용법](https://www.lesstif.com/pages/viewpage.action?pageId=20776078)  
    Address bind 관련 문제가 있을 때마다 포트 점유하고 있는 프로세스 보려고 옛날에 자주 썼던 명령어. 그냥 list 관련된 모든 것에 대한 헬퍼인 것 같다.
- [grep 사용법](https://zzsza.github.io/development/2017/12/16/linux-4/)  
    결과를 필터링할 때 자주 사용하는 명령어.
- [awk 사용법](https://zzsza.github.io/development/2017/12/20/linux-6/)  
    입력된 라인들의 데이터들을 특정 기준으로 분리해서, 일부 column만 가져올 수 있게 해주는 명령어.
- [htop Explained Visually](https://codeahoy.com/2017/01/20/hhtop-explained-visually/)  
    짱 쩌는 프로세스 모니터. devops 하시는 분들이 항상 피벗 모니터에 ElasticSearch 클러스터같은 데서 htop 켜놓고 있더라.
- [Crontab 사용법](https://jdm.kr/blog/2)  
    특정 job을 스케줄하기 위해서 사용한다.
- [리눅스 명령어 sudo, su, su -](https://www.leafcats.com/168)

## CS
### 운영체제
- [컴퓨터가 코드를 읽는 아주 구체적인 원리](https://parksb.github.io/article/25.html)
- [Race condition 발생시키고 Mutex lock으로 해결하기](https://parksb.github.io/article/16.html)
### 자료구조
### 알고리즘
- [루프 불변성](http://egloos.zum.com/kuphy00/v/2475164)  
    반복 알고리즘의 무결성을 증명하기 위해 사용되는 방법이다. 루프 불변성과 반대되는 개념으로는 루프 변성이 있는데, 이는 루프를 '도는' 동안 변하는 성질을 가진 것들을 칭한다. 
- [시간 복잡도 빠르게 이해하기](https://joshuajangblog.wordpress.com/2016/09/21/time_complexity_big_o_in_easy_explanation/)  
    시간 복잡도란 어떤 알고리즘의 실행 시간이 얼마나 되는가? 라는 질문에 대한 대답을 할 수 있는 개념으로, 알고리즘이 입력에 대해 얼마나 오래 실행될 것인지 예측할 수 있다.
- [점근 표기법](https://ratsgo.github.io/data%20structure&algorithm/2017/09/13/asymptotic/)    
    상기한 시간 복잡도에 대해 조금 더 수학적으로 접근한 내용이다.
- [분할정복](https://ko.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort)    
    커다란 하나의 문제가 사실 '닮은꼴' 문제들로 쪼개질 수 있다면, 여러 부분문제들을 해결한 다음 해를 결합함으로서 원래 해결하고자 했던 문제를 해결할 수 있다.
- [힙 정렬](https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/)    
    최대 힙이나 최소 힙을 만들어 정렬하는 방식이다. 평균적인 시간복잡도는 퀵 정렬과 같지만(최악의 경우 퀵 정렬보다 빠르다) [트리를 만들어 정렬하는 특성 탓에 자료가 커질 수록 퀵 정렬보다 캐시 활용에 있어 모자란 면모를 보인다.](https://en.wikipedia.org/wiki/Heapsort#Variations) 
- [동적 계획법](https://www.zerocho.com/category/Algorithm/post/584b979a580277001862f182)   
    부분 해를 구하는 과정을 거듭해 최종 해를 구한다는 점은 분할정복과 비슷하지만, 분할정복과는 달리 한 번 구한 부분해가 여러 번 재활용되며 (중복되는 부분 문제가 존재하기 때문: n번째 피보나치 수는 n-1번째 피보나치 수와 n-2번째 피보나치 수를 더해서 구할 수 있다), 문제의 분할 자체가 속도 향상에 도움이 되는 분할정복과 달리 이전에 구한 해를 재활용하는 것이 속도 향상에 도움을 준다.
- [파이썬으로 정리하는 Quick-Sort](https://parksb.github.io/article/18.html)
### 네트워크
- [Top-Down으로 접근하는 네트워크](https://parksb.github.io/article/23.html)

## 데이터 엔지니어링

## Marketing
- [User Acquisition - appsflyer](https://www.appsflyer.com/mobile-attribution-glossary/user-acquisition/)  
    `The method of driving new users to a mobile app business through marketing activity`
- [User Acquisition - Adjust](https://www.adjust.com/glossary/user-acquisition/)  
    `User acquisition (often shortened to UA) is the act of gaining new users, whether it be on an app, platform, or another service.`
- [Re-Engagement](https://www.adjust.com/glossary/re-engagement/)  
    `Re-engagement is the practice of serving ads to people after who have shown interest without converting.`
- [What is a tracking link?](https://support.rebrandly.com/hc/en-us/articles/360007299393-What-is-a-tracking-link-)  
- [Single-Touch vs. Multi-Touch Marketing Attribution](https://www.rockerbox.com/blog/attribution-101-single-touch-versus-multi-touch)
- [Retargeting](https://retargeter.com/what-is-retargeting-and-how-does-it-work/)
- [Reattribution](https://www.adjust.com/glossary/reattribution/)

# 백엔드
## 백엔드 관련 배경지식
- [Microservices with gRPC](https://medium.com/@goinhacker/microservices-with-grpc-d504133d191d)
- [The Complete Guide to the ELK Stack - 2018](https://logz.io/learn/complete-guide-elk-stack/#intro)  
    Splunk라는 선택지를 두고 왜 ELK를 쓰는지, 왜 유명한지, 로깅은 왜 해야 하는지, 기본적인 ELK stack부터 중간에 redis나 kafka를 써서 버퍼링하는 구조까지 설명하고 있다. 글이 좀 많이 긴데 정말 읽어볼만 하다. ELK는 웬만하면 log shipper로 Beats가 껴 있어서, Elastic에서는 이를 Elastic Stack이라는 이름으로 브랜딩하고 있다.
- [What are the advantages and disadvantages of using a content delivery network(CDN)?](https://stackoverflow.com/a/2145389)  
    네트워크는 물리적으로 가까운 위치에 있을수록 응답 속도가 빠르다. hop count가 줄어들기 때문이다. CDN은 정적 데이터(css, js, 이미지 등)를 다른 리전의 서버에 캐싱해 둬서, 멀리 사는 사용자에게 컨텐츠를 제공하는 퍼포먼스를 향상시키는 기술. Amazon Cloudfront같은 서비스가 CDN을 제공한다.
- [Time Series Database and Tick Stack](https://www.slideshare.net/GianlucaArbezzano/time-series-database-and-tick-stack)  
    로그 collector로 Telegraf, 시계열 데이터베이스로 InfluxDB, 시각화로 Chronograf, Alerting&Anomarly Detection으로 Kapacitor를 사용하는 모니터링 스택.
- [Already learned DevOps? Great, now it’s time for GitOps](https://thenextweb.com/contributors/2018/12/08/all-you-need-to-know-about-gitops/)  
    `Everything as Code`
- [Failover & Disaster Recovery](https://stackoverflow.com/questions/120139/failover-disaster-recovery)
- [What is failover?](https://searchstorage.techtarget.com/definition/failover)  
    `Failover is a backup operational mode in which the functions of a system component (such as a processor, server, network, or database, for example) are assumed by secondary system components when the primary component becomes unavailable through either failure or scheduled down time.`
- [What is High Availability?](https://www.digitalocean.com/community/tutorials/what-is-high-availability)  
    `In computing, the term availability is used to describe the period of time when a service is available, as well as the time required by a system to respond to a request made by a user.`
- [Disater Recovery Strategies](http://www.computepatterns.com/517/disaster-recovery-strategies/)
## Docker
- [초보를 위한 도커 안내서 - 1. 도커란 무엇인가?](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
- [초보를 위한 도커 안내서 - 2. 설치하고 컨테이너 실행하기](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)
- [초보를 위한 도커 안내서 - 3. 이미지 만들고 배포하기](https://subicura.com/2017/02/10/docker-guide-for-beginners-create-image-and-deploy.html)
- [개발자가 처음 Docker 접할때 오는 멘붕 몇가지](https://www.popit.kr/%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B0%80-%EC%B2%98%EC%9D%8C-docker-%EC%A0%91%ED%95%A0%EB%95%8C-%EC%98%A4%EB%8A%94-%EB%A9%98%EB%B6%95-%EB%AA%87%EA%B0%80%EC%A7%80/)
- [도커를 이용한 웹서비스 무중단 배포하기](https://subicura.com/2016/06/07/zero-downtime-docker-deployment.html)  
    배포 자동화가 대체 왜 필요한지부터, 왜 무중단 배포인지, 왜 Docker인지를 하나하나 설명하며 orchestration 얘기까지 비교적 쉽게 잘 설명한다.
- [왜 굳이 도커(컨테이너)를 써야 하나요?](https://www.44bits.io/ko/post/why-should-i-use-docker-container)  
    여기서 얘기하는 '눈송이 서버'라는 걸 겪어보지 못한 상태에서 docker를 마주쳤다 보니 궁금한 게 많았는데, 이 글이 잘 해결해 주었다.
### Docker 커맨드 관련 지식들
- [Docker 데이터 볼륨 사용하기](http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter06/04)
- [How to mount a single file in a volume](https://stackoverflow.com/questions/42248198/how-to-mount-a-single-file-in-a-volume)
- [How to enter in a Docker container already running with a new TTY](https://stackoverflow.com/questions/20932357/how-to-enter-in-a-docker-container-already-running-with-a-new-tty)  
    `docker exec -it [container-id] bash`
- [Docker run vs create](https://stackoverflow.com/a/37745261)
### Dockerfile, docker-compose.yml 관련 지식들
- [Docker VOLUME vs COPY vs ADD](http://coderbro.com/docker/2017/10/24/docker-volumes-vs-copy.html)
- [Automation of container creation and creating image with DB packed](https://forums.docker.com/t/automation-of-container-creation-and-creating-image-with-db-packed/4982)  
    docker-entrypoint-initdb.d에 대한 내용이다. Docker image가 run되는 시점에 사전 정의된 sql 스크립트를 돌리도록 하고 싶다면 `docker-entrypoint-initdb.d`를 써먹을 수 있다.
### Docker 써먹기
- [kitematic](https://kitematic.com/)  
    'Run containers through a simple, yet powerful graphical user interface.'
- [아마존 엘라스틱 컨테이너 서비스(ECS) 입문](https://www.44bits.io/ko/post/container-orchestration-101-with-docker-and-aws-elastic-container-service)
- [ECS의 매니지드 컨테이너 AWS 파게이트 시작하기](https://www.44bits.io/ko/post/getting-started-with-ecs-fargate)
### Docker Compose
- [Docker (Compose) 활용법](http://raccoonyy.github.io/docker-usages-for-dev-environment-setup/)  
    사실상 docker-compose에 대한 이야기. production level에 영향을 주지 않고 어플리케이션을 테스트하려면, 로컬에 인프라를 모두 띄워야 하는데 이게 말처럼 쉽지가 않다. Docker 컨테이너 여러개를 훅 띄우는 데엔 docker-compose를 써먹을 수 있다. 'Compose is a tool for defining and running multi-container Docker applications.'
## Ansible
- [Ansible 101](https://medium.com/@denot/ansible-101-d6dc9f86df0a)  
    'Ansible allows your whole infrastructure to be defined as code, so it can be version controlled, easily replicated and tested, truly DevOps!'. 뭐 automate software provisioning 이러는데 'infrastructure provisioning'이라는 개념 자체가 좀 어려웠다. 걍 EC2에 druid 올리면 infrastructure provisioning이라고 부를 수 있는듯. 여기에 automate 개념이 붙는 건 Ansible이 호스트 여러개에 갖다가 똑같은 커맨드 뚝딱뚝딱 실행시켜줄 수 있어서. 근데 Ansible도 Infrastructure as Code로 분류됨.
## Terraform
- [테라폼(Terraform) 기초 튜토리얼 - AWS와 테라폼으로 구현하는 Infrastructure as Code](https://www.44bits.io/ko/post/terraform_introduction_infrastrucute_as_code)  
    대부분 DevOps 관련 컨텐츠를 연재하는 44Bits의 Terraform 튜토리얼. 진짜 잘 정리돼있다! Terraform으로 뭔가 해보기 전에 읽어보면 엄청 좋을듯.
- [Terraform을 이용한 Infrastructure as Code 실전 구성하기](https://www.slideshare.net/awskorea/configuring-practical-aws-based-infrastructure-as-code-using-terraform-byoun-jeonghun)  
    클라우드 인프라의 리소스들을 코드 형태로 구성할 수 있는 툴. 얘도 사실상 Ansible이랑 비슷한 맥락으로 infrastructure provisioning을 위한 것 같다. 써봐야 확실히 알 수 있을듯.
- [Ansible vs Terraform: Fight!](https://linuxacademy.com/blog/devops/ansible-vs-terraform-fight/)  
    'One of those key differences involves two very common DevOps concepts: configuration management and orchestration.
## 서버 아키텍처 관련 블로깅/발표자료
- [[야생의 땅: 듀랑고] SPOF 없는 분산 MMORPG 서버](https://www.slideshare.net/sublee/spof-mmorpg)
- [[야생의 땅: 듀랑고] 서버 아키텍처 Vol. 2 (자막)](https://www.slideshare.net/sublee/lt-vol-2)
- [DEVIEW 2016 참가 신청 기능 개발기](https://d2.naver.com/helloworld/5048491)  
    결론은 '신청자 수를 RDB에서 관리하지 않고 Redis 기반의 분산 메모리 저장소인 nbase-arc로 바꿨더니 잘 되더라'였다. 글만 보면 그냥 nbase 붙이고 나니까 너무나도 매끄럽고 쉽게 해결된 것만 같다. nbase-arc의 INCR 연산이 단순히 UPDATE 쿼리보다 속도가 빨라서 병목이 생기지 않았던 걸까? 이걸 조금 더 설명해줬으면 좋았을 것 같다. 무튼 캐시가 중요하긴 한가 보다. 2017, 2018 개발기도 올라왔으면 좋겠다.
- [타다 시스템 아키텍처](http://engineering.vcnc.co.kr/2019/01/tada-system-architecture/?fbclid=IwAR1TJy9RpUzM-iR0QZoF0W1pMNjCoZDDvs0tVf21uv01eCX59ulTI0QBT-8)  
    관리 코스트 때문에 메시지 브로커에 redis를 쓰고, HTTP/2에 Protobuf를 쓴다는 게 신기했다.
## Deployment
- [Blue/Green Deployment: What It Is and How it Reduces Your Risk](https://rollout.io/blog/blue-green-deployment/)  
    무중단 배포 전략 중 하나로, 기존의 어플리케이션을 green version이라고 부르고, 업그레이드하고자 하는 버전의 어플리케이션을 blue version이라고 이름짓는다. production에서 green version만 존재한 채 트래픽을 처리하다가 -> blue version이 새로 생겨나 트래픽을 둘이 함께 처리하고 -> blue version이 모든 트래픽을 처리하도록 만든 후 -> green version을 제거하고 blue version을 새로운 green version으로 만드는 방식이다. 잠시동안 두 버전의 어플리케이션을 동시에 띄워야 하니 비용 문제가 발생할 수는 있으나 대부분 이런 방식을 많이 쓰는 것 같다.
## 웹서버 이야기
- [What is the difference between application server and web server?](https://stackoverflow.com/a/936257)  
    web server는 static content에 적합하고, app server는 dynamic content에 적합하므로 web server는 app server의 리버스 프록시 역할을 할 수 있다는 설명이 있다.
- [Difference between proxy server and reverse proxy server](https://stackoverflow.com/a/366212)
## CI
- [Continuous Integration](https://www.martinfowler.com/articles/continuousIntegration.html)
- [About Travis CI](https://medium.com/hbsmith/about-travis-ci-65b04d3dead6)
## 도움되는 SaaS
- [runscope](https://www.runscope.com)  
    API 모니터링 SaaS. 정해둔 스케줄과 step에 따라 API를 호출하고 validation을 수행한다. pagerduty같은 on-call alert 서비스와의 integration을 지원해서, API에 500이 발생했을 때 내 핸드폰으로 전화가 오게 만들 수도 있다.
- [statuspage.io](https://www.statuspage.io/)  
    서비스의 상태를 공개하기 위한 status page를 호스팅해주는 서비스
- [Sonarqube](https://www.sonarqube.org/)  
    버그, 취약점, 코드 스멜이라는 3가지의 카테고리로 나누어 rule을 정의해 이를 기반으로 코드를 정적 검사해 주는 도구다.
- [Python 프로젝트에 Codecov 연동하기](https://cjh5414.github.io/codecov-python/)
- [codecov vs coveralls](http://text.youknowone.org/post/144201220021/codecov-vs-coveralls)
    커버리지 측정 도구로 유명한 codecov와 coveralls를 비교하는 글.
## 도움되는 툴
- [Facebook Account Kit](https://developers.facebook.com/docs/accountkit/)  
    SMS, 이메일을 통해 passwordless authentication을 할 수 있도록 도와주는 페이스북의 킷. SMS 인증이 한 달에 10만회까지 무료라길래 흠칫해서 알아보게 됨. Auth0라는 서비스도 이런 컨셉인 것 같은데, Auth0가 먼저고 Account Kit이 나중인듯.
- [ab - HTTP 서버 벤치마킹 툴](https://httpd.apache.org/docs/2.4/en/programs/ab.html)
- [wrk](https://github.com/wg/wrk)
## Serverless
- [Serverless Architecture](https://www.slideshare.net/awskr/serverless-architecture-78022209)
- [서버리스 아키텍쳐(Serverless)란?](https://velopert.com/3543)  
    서버리스는 직접 관리하는 인프라가 없다는 의미.
## 교양
- [채점 현황 속도 올리기 - 스타트링크](https://startlink.blog/2018/03/09/%EC%B1%84%EC%A0%90-%ED%98%84%ED%99%A9-%EC%86%8D%EB%8F%84-%EC%98%AC%EB%A6%AC%EA%B8%B0/)  
    백준 온라인 저지(BOJ)에서 채점 현황 페이지의 속도를 올리기 위한 경험이 담겨 있다. real world에서의 쿼리 튜닝에 관한 이야기라 재밌게 본 것 같다.
- [ipify: 300억 요청 처리, 그 너머로](http://www.haruair.com/blog/4108)  
    IP 주소 검색 서비스인 [ipify](https://www.ipify.org/)를 Node.js로 개발하고, 성능에 문제를 겪은 뒤, Go로 API를 다시 작성해 문제를 해결한 이야기. 월간 200 달러로 300억 요청 처리. Go에 뽐뿌가 오게 만드는 글이다. 근데 Node.js가 왜 훨씬 느렸는지가 구체적으로 안 나와 있어서 아쉬웠다. ab라는 벤치마킹 툴을 새로 알게 되어 좋았음.
## DB
### DB 자체에 대한 지식
- [What is an ORM and where can I learn more about it?](https://stackoverflow.com/a/1279678)  
    ORM이 무엇이고, 장점과 단점은 무엇인지에 대한 설명. ORM 라이브러리는 대부분 무겁고 러닝커브가 생기긴 하지만, 상황에 따라 동적으로 SELECT 쿼리를 빌드하는 머리아픈 경험을 해 봤다면 ORM이 이만큼 유연할 수가 없다. 복잡한 쿼리가 아니라면 성능 문제도 딱히 없는 것 같다. 이래저래 논쟁을 끌고 다니는 기술이긴 한데, 단점을 감당하지 않기 위해서 ORM으로 얻을 수 있는 메리트를 모두 포기하고 raw SQL을 쓸 이유가 딱히 없지 않을까 싶다. 물론 대용량 데이터를 다룰 때는 raw SQL을 쓰는 것이 마음 편한 듯.
- [DBMS는 어떻게 트랜잭션을 관리할까?](https://d2.naver.com/helloworld/407507)  
    CUBRID의 개발을 이끌고 있는 엔지니어가 쓴, 트랜잭션의 관리를 DBMS 레벨에서 설명한 글. ACID 성질부터 UNDO와 REDO, 상태 로깅과 전이 로깅, 커밋을 하면 어떤 일이 일어나는지, group commit과 트랜잭션 철회 등이 정말 잘 정리되었다. 역시 기술은 해본 사람이 잘 아는 것 같다.
- [A Detailed Guide to Database Denormalization with Examples](https://rubygarage.org/blog/database-denormalization-with-examples)  
    역정규화는 정규화된 데이터베이스에서 데이터를 묶거나 중복 적재하는 등 쓰기 작업을 더 많이 수행해서, 읽기 속도를 향상시키는 일이다. 많은 JOIN이나 aggregation이 이뤄지는 읽기 쿼리는 속도가 느려지기 마련인데, 데이터를 중복해서 적재하거나, pre-joined 구조의 스키마를 작성하는 등의 역정규화로 이를 해결하는 경우가 있다. 위 가이드는 역정규화의 몇가지 사례들을 쉬운 예제와 함께 잘 설명해주고 있다.
- [How does database indexing work?](https://stackoverflow.com/a/1130)  
    Index는 특정 레코드를 찾는 데에 linear search하던 걸, 레코드들을 정렬한 별도의 자료 구조를 만들어 여기에 range search하도록 만들고, 이를 통해 block access count를 줄이는 것이라고 보면 되는 것 같다. 너무 추상적인 것 같아 더 파보니 클러스터/비클러스터 인덱스 등등 더 깊게 뻗어나갈 수 있을듯.
- [What do Clustered and Non clustered index actually mean?](https://stackoverflow.com/a/1251652)  
    인덱스의 아키텍처는 클러스터형/비클러스터형 인덱스로 나뉜다. 클러스터형 인덱스는 unique row를 컬럼 순서에 맞춰 물리적인 레벨에서 ordering하여 적재하는 인덱스라고 한다. PK를 기준으로 판단하며 따라서 테이블 당 하나씩 가질 수 있음. PK를 만들면 알아서 클러스터형 인덱스가 생긴다. B-Tree 인덱스나 hash table이 클러스터형 인덱스에 주로 쓰인다고 한다. 비클러스터형 인덱스는 물리적으로 데이터를 정렬하진 않고, 인덱스만 정렬한다. JOIN, WHERE, ORDER BY 절에서 사용된 비 PK 컬럼 위에 만들어진다고 함. insert와 update, point query(한두개만 select) operation에 있어서는 클러스터형 인덱스보다 빠르다고 한다.
    
    \* [What are the differences between a clustered and a non-clustered index?](https://stackoverflow.com/a/91725)
- [Why do you create a View in a database?](https://stackoverflow.com/a/1278620)  
    두 테이블을 JOIN하는 복잡한 서브 쿼리를 제거하기 위해 처음으로 사용했었던 것 같다. 실제로 복잡성을 숨기기 위해 사용된다고도 한다. 테이블의 특정 컬럼을 보호하기 위한 메커니즘으로 사용할 수 있다는 DBA의 관점도 있다. View는 '쿼리를 캡슐화하여 aliasing한다'라고 이야기할 수 있을 것 같다.
- [Are soft deletes a good idea?](https://stackoverflow.com/questions/2549839/are-soft-deletes-a-good-idea/2549843)  
    데이터의 삭제에 대해 DELETE 쿼리를 날리는 것을 pysical delete, 삭제되었음을 나타내는 (is_deleted같은)컬럼을 두는 방식을 soft delete라고 부른다. 이래저래 논쟁이 많지만 'It depends on the circumstances.'와 'You can't do cascading deletions', 'it's a good idea to have a deleted_date field, instead of an is_deleted field.'가 팩트. 'a soft delete like this means you now have to include a WHERE IsDeleted = false clause in every query on this table'같은 휴먼 에러야 테스트 코드로 보완할 수 있는 부분일테고.
- [What are OLTP and OLAP. What is the difference between them?](https://stackoverflow.com/questions/21900185/what-are-oltp-and-olap-what-is-the-difference-between-them)  
    'In OLTP database there is detailed and current data, and schema used to store transactional databases is the entity model (usually 3NF).', 'OLAP applications are widely used by Data Mining techniques. In OLAP database there is aggregated, historical data, stored in multi-dimensional schemas (usually star schema).'
- [What are Covering Indexes and Covered Queries in SQL Server?](http://gywn.net/tag/covering-index/)  
    'all requested columns in a query without performing a further lookup into the clustered index.', 'A covered query is a query where all the columns in the query's result set are pulled from non-clustered indexes.'
- [What is a stored procedure?](https://stackoverflow.com/questions/459457/what-is-a-stored-procedure?lq=1)  
    'A stored procedure is a set of precompiled SQL statements that are used to perform a special task.', 'A benefit of stored procedures is that you can centralize data access logic into a single place that is then easy for DBA's to optimize.'
- [데이터베이스 분포도(Database Selectivity)](https://jdm.kr/blog/169)
- [What are the materialized views?](https://stackoverflow.com/questions/4463354/what-are-materialized-views)  
    'A view is basically a "named" SQL statement.', 'A materialized view is a view where the query has been executed and the results has been stored as a physical table.'
- [Are junction tables a good practice?](https://dba.stackexchange.com/questions/106001/are-junction-tables-a-good-practice)
### DB Vendor
- [InfluxDB](https://github.com/influxdata/influxdb)  
    TICK stack에서 time series 데이터베이스로 사용된다. 외부 의존성 없고, SQL-like한 InfluxQL이라는 질의 인터페이스를 지원하고, 클러스터링 지원하고, Grafana랑 연계하기 좋고, Go로 개발됐고, 원래 LSM(Log Structured Merge) Tree를 지원하는 LevelDB를 스토리지 엔진으로 쓰다가 이를 개량한 TSM(Time Structured Merge) Tree를 스토리지 엔진으로 사용해서 IO도 빠르고, 압축 알고리즘도 적용해서 스토리지 효율 면에서도 뛰어나다. Graphite는 퍼포먼스 문제가 꽤 많다고 하고, Prometheus는 클러스터링 기능이 없다. 그러나 시계열 데이터베이스에도 silver bullet은 없다 ㅜㅜ. 얼마 전에 나온 TimeStream이랑 비교하는 글이 곧 올라오지 않을까?
- [StatsD](https://github.com/etsy/statsd)  
    Node.js 런타임에서 동작하는 로그 aggregation 프록시. 단위 시간 안의 API 응답 시간 평균과 같은 것들은 일차적으로 aggregation을 해두면 로그 DB의 부하 방지에 좋을 것 같다. Mongo, Graphite, InfluxDB, Zabbix, CouchDB 등 백엔드 지원도 잘 되어 있다.
- [Reduce MySQL Memory Utilization with ProxySQL](https://medium.com/searce/reduce-mysql-memory-utilization-with-proxysql-multiplexing-cbe09da7921c)  
    'The main purpose of the multiplexing is to reduce the connections to MySQL servers. So we can send thousands of connections to only a hundred backend connections.' ProxySQL을 쓰는 걸 구경은 해봤는데 직접 써본 적은 없어서 유의미하게 뭔가 경험해본 적이 딱히 없다. ㅜㅜ 커넥션 관리에 확실히 좋다고는 들음.
- [druid](http://druid.io/druid.html)  
    OLAP를 위해 디자인된, lambda architecture 기반의 data store. 검색 엔진에서 사용하곤 하는 inverted index 구조를 가진다. realtime data에 대한 aggregation query가 매우 빠르다. Hadoop에서 하기 어려운 데이터의 빠른 접근과 실시간 쿼리를 만족한다. aggregating을 매우 빠르게 처리하는 데이터 스토어라고 보면 될 듯. 비슷한 것으로 Google BigQuery, Dremel, PowerDrill 등이 있다.
- [FluentD](https://blog.jonnung.com/system/2018/04/06/fluentd-log-collector-part1/)  
    Logstash 대용으로 사용할 수 있음.
### Common SQL
#### Common DML(INSERT, SELECT, UPDATE, DELETE)
- [Insert into a MySQL table or update if exists](https://stackoverflow.com/a/4205207)  
    key duplication이 없다면 insert하고, 있으면 update를 MySQL에서는 `ON DUPLICATE KEY UPDATE`로 표현한다. `UPSERT`나 `MERGE`라는 이름으로도 사용되고 있는 개념.
- [SELECT 결과를 INSERT 하기](https://zetawiki.com/wiki/SQL_SELECT_%EA%B2%B0%EA%B3%BC%EB%A5%BC_INSERT_%ED%95%98%EA%B8%B0)
#### JOIN
- [Review of SQL JOINS](https://medium.com/@josemarcialportilla/review-of-sql-joins-ac5463dc71c9)
- [LEFT JOIN vs. LEFT OUTER JOIN in SQL Server](https://stackoverflow.com/questions/406294/left-join-vs-left-outer-join-in-sql-server)  
    두번째 답변의 내용이 매우 좋다. JOIN은 top level에서 INNER, OUTER, CROSS로 나눌 수 있고, OUTER JOIN의 앞에는 LEFT, RIGHT, FULL이 들어갈 수 있다는 것.
- [MySQL ON vs USING?](https://stackoverflow.com/questions/11366006/mysql-on-vs-using)  
    'USING is useful when both tables share a column of the exact same name on which they join.'
#### Date, Time 연산 관련 쿼리
- [When is a timestamp (auto) updated?](https://stackoverflow.com/questions/18962757/when-is-a-timestamp-auto-updated)  
    `ON UPDATE CURRENT_TIMESTAMP`에 대한 이야기.
- [INTERVAL](http://www.mysqltutorial.org/mysql-interval/)  
    `INTERVAL [expr] [unit]` | new relic에서 since 3 days ago같은 쿼리 보면서 되게 신기하다 싶었는데, SQL에도 있었다.
### MySQL
- [Illegal mix of collations for operation 'like'](https://stackoverflow.com/a/18651057)  
    DATETIME 필드에 대해 유니코드가 아닌 문자열로 LIKE 쿼리 수행 시 문제가 생기는데, 이를 해결하는 방법. 그냥 질의하기 전에 date format validation 돌리는 게 마음 편하다.
- [MySQL 쓰면서 하지 말아야 할 것 17가지](https://blog.lael.be/post/370)  
    좀 오래된 글이긴 하지만 쉽사리 얻지 못할 지식들이 많이 들어 있다.
- [MySQL 중복 키 관리 방법](http://jason-heo.github.io/mysql/2014/03/05/manage-dup-key2.html)  
    INSERT 시 unique constraint에 관해 생길 수 있는 몇가지 문제들을 해결해줄 3가지 쿼리(INSERT IGNORE, REPLACE INTO, ON DUPLICATE KEY UPDATE)
### PrestoDB
- [Date and Time Functions and Operators](https://prestodb.io/docs/current/functions/datetime.html)  
    PrestoDB의 date/time 관련 함수와 operator가 정리된 문서. athena에서 view를 만들 때 시간에 관한 계산이 종종 필요한데, 대부분 이 문서 하나면 모두 해결 가능하다. timestamp ↔ unixtime은 `to_unixtime`, `from_unixtime` 함수를 사용하면 되고, 타임존 변경은 `AT TIME ZONE` operator, 포매팅과 파싱은 각각 `date_format`과 `date_parse`를 쓰면 된다. 
### Druid
#### Query
- [Querying - Overview](http://druid.io/docs/latest/querying/querying.html)
- [Transforming Dimension Values](http://druid.io/docs/latest/querying/dimensionspecs.html)  
    Lookup에 관한 이야기.
- [Querying - Aggregations](http://druid.io/docs/latest/querying/aggregations)
- [Querying - Aggregation Granularity](http://druid.io/docs/latest/querying/granularities.html)
### ElasticSearch
#### Query
- [Query and filter context](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html)  
    ElasticSearch docs에서 쿼리 부분에 들어가면 가장 처음 나오는 내용. ElasticSearch의 모든 쿼리는 context를 가지며 이는 query와 filter context로 나뉜다고 정리되어 있다. query context는 '얼마나 잘 일치하는가'같은 scoring의 느낌이고, filter context는 '이것과 일치하는가'같은 SQL의 WHERE절 같은 느낌이다.
- [Bool Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html)  
    bool은 must, should, filter같은 조건 쿼리들을 모아주기 위해 사용된다. 그냥 SQL에서 조건문을 정의하기 위해 WHERE 뒤에 조건식들을 나열하는 것처럼 ES에선 bool을 사용한다고 생각하면 됨.
- [ElasticSearch bool query combine](https://stackoverflow.com/a/40755927)  
    ElasticSearch에 쿼리할 때 조건식들을 나열하기 위해 bool query 내부에 should와 must같은 걸 쓰곤 하는데, 이들이 각각 어떤 condition으로 조건식들을 합치는지에 대한 질문. OR은 should, AND는 must와 대응된다.
- [What is the difference between must and filter Query DSL in ElasticSearch?](https://stackoverflow.com/a/43349478)  
    AND 쿼리를 위해 사용하는 must query와 filter query의 차이에 대한 질문. must는 스코어를 측정하고, filter는 스코어를 측정하지 않는다. score가 필요없는 쿼리의 경우 must 대신 filter를 쓰면 더 빠르다고 한다.
- [ElasticSearch match vs term query](https://stackoverflow.com/questions/23150670/elasticsearch-match-vs-term-query)  
    bool query 내에서, 특정 필드의 값에 대한 일치 연산을 위해 term이나 match를 대부분 사용하는데, 이 둘의 차이가 무엇인지에 대한 질문. term은 filter context, match는 query context에서 실행된다고 정리하면 된다. exactly equal을 보려면 term을 쓰는 것이 맞음.
- [Source filter](https://www.elastic.co/guide/en/elasticsearch/reference/2.4/search-request-source-filtering.html)  
    Source filter(_source)를 통해 ElasticSearch가 결과에 특정 필드만 포함시키도록 한다. includes/excludes를 두면 포함/제외를 별도로 둘 수 있다.
- [Terms Aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html)  
    DISTINCT SELECT/COUNT에 쓰이는 terms aggregation.
- [Term level query - range query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-range-query.html)  
    SQL의 between과 대응되는 쿼리.
#### Others
- [Elastic APM](https://www.elastic.co/guide/en/apm/get-started/current/overview.html)  
    Elastic에서 제공하는 APM 서비스. New Relic같은 거라고 보면 된다. 하드하게 써본 경험은 없어서 뭐라고 하진 못 하겠지만, 어차피 ES 쓰고 있다면 APM도 Elastic 인프라 내에서 처리해도 괜찮을 것 같다고 생각한다.
## 웹 프레임워크
### Python
#### Flask
- [Flask 1.0 Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)
- [Flask 1.0 공식 튜토리얼](http://flask.pocoo.org/docs/1.0/tutorial/)
- [Flask 1.0에서 달라진 점](https://winterj.me/flask-release/)
- [Patterns for Flask 1.0](http://flask.pocoo.org/docs/1.0/patterns/)
- [Pynash: Proxy objects in Flask (and elsewhere)](http://pynash.org/2013/02/12/proxy-objects/)
- [What is the purpose of Flask's context stacks?](https://stackoverflow.com/questions/20036520/what-is-the-purpose-of-flasks-context-stacks)
- [Output Fields - Flask-RESTful documentation](https://flask-restful.readthedocs.io/en/0.3.5/fields.html)  
    view function에 `@marshal_with`을 정의해 두면, flask-restful은 해당 view function이 return한 객체에 접근해서, 데코레이터 인자로 전달한 스키마를 토대로 속성들을 뽑아 간다. ORM으로 가져온 객체를 그대로 리턴하고, marshal과 관련된 것들은 별도로 수행되도록 하는 구조를 구성해볼 수 있다.
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

# 프로그래밍 언어
## Python
### 언어 자체에 대한 이야기
- [제너레이터와 코루틴](https://soooprmx.com/archives/5622)
- [파이썬 언더스코어(_)에 대하여](https://mingrammer.com/underscore-in-python/)
- [Python __getitem__과 slice의 이해](https://item4.github.io/2015-10-26/Understanding-Python-__getitem__-and-slice/)  
    getitem 과 slice 에 대한 내용 뿐만아니라, "Ellipsis" 라는 개념이 등장한다. Ellipsis 는 null statement로 pass 대신 쓰이는 경우도 있다.
- [Python equivalent of golang's defer statement](https://stackoverflow.com/a/34625254)  
    Go에서 defer는 function call stack의 맨 위에 해당 함수를 push한다. 이걸 Python에선 어떻게 해야 할까?라는 질문. contextlib.ExitStack을 써먹으면 된다.
- [What is \_\_pycache__?](https://stackoverflow.com/questions/16869024/what-is-pycache)
#### collections
- [Removing duplicates in lists](https://stackoverflow.com/a/7961390)  
    리스트에서 중복된 요소를 제거하는 방법에 대한 이야기다. 알아두면 요긴하게 써먹을 수 있음.
- [Difference between append vs. extend list methods in Python](https://stackoverflow.com/a/252711)  
    list를 확장하는 메소드로 append와 extend가 있는데, 이 둘의 차이. 3번째 답변이 오버로딩된 연산자와 timeit을 통한 시간 복잡도까지 잘 설명하고 있다.
#### 파이썬 공부 자료
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
- [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/)
#### 성능
- [Python GIL](https://medium.com/@mjhans83/python-gil-f940eac0bef9)
- [Python GC가 작동하는 원리](https://winterj.me/python-gc/)
- [\_\_slots__ magic](http://book.pythontips.com/en/latest/__slots__magic.html)
#### Python 3.7
- [dataclasses](https://docs.python.org/ko/3/library/dataclasses.html)
- [Python 3.7’s new builtin breakpoint — a quick tour](https://hackernoon.com/python-3-7s-new-builtin-breakpoint-a-quick-tour-4f1aebc444c)
#### type hint
- [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)  
    Python 3.5부터 사용 가능한 type definition. typing 모듈의 overload 데코레이터로 오버로딩도 가능하다.
- [PEP 526 -- Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)
- [pyright](https://github.com/Microsoft/pyright)
- [mypy](http://mypy-lang.org/)
- [Type hinting in Python 2](https://stackoverflow.com/questions/35230635/type-hinting-in-python-2)
### 개발 환경
- [가상 환경 및 패키지](https://docs.python.org/ko/3/tutorial/venv.html)
- [Black](https://github.com/ambv/black)  
    엄청 잘 만들어진 코드 포매터.
### 테스팅
#### nose
- [Basic usage : Options](https://nose.readthedocs.io/en/latest/usage.html#options)
#### coverage.py
- [Configuration files](https://coverage.readthedocs.io/en/coverage-4.4.2/config.html)  
    `.coveragerc`에 대한 내용
- [Coverage.py command line usage](https://coverage.readthedocs.io/en/coverage-4.2/cmd.html)

#### pipenv
- [pipenv란 무엇인가](https://medium.com/@erish/python-pipenv-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-961b00d4f42f)  
    virtualenv+pyenv+pip가 합쳐진 형태의, Python계의 npm인 pipenv에 대한 소개. pyenv가 설치되어 있으면 알아서 필요한 버전을 설치하고 가상 환경을 열어준다는 게 정말 맘에 든다. pyenv 설치하고, pyenv-virtualenv 설치하고, requirements.txt를 dev와 production에 나눠 만들 필요가 없으니 정말 편한 도구.
- [pipenv로 Python 프로젝트 관리하기](https://cjh5414.github.io/how-to-manage-python-project-with-pipenv/)  
    글 자체가 깔끔하게 정리되어 있기도 하고, pipenv가 제공하는 명령어들에 대한 구체적인 설명이 들어 있어서 초심자에게 더 좋은듯.
- [Force pipenv to create a new virtualenv](https://stackoverflow.com/a/49258323)  
    pipenv install 시 이미 대응되는 venv가 존재하면 에러가 나는데, 무시하고 그냥 새 venv를 덮어씌우기 위한 방법. 'you can set the environment variable PIPENV_IGNORE_VIRTUALENVS to avoid reusing an already activated virtualenv'
- [How to get pipenv running in docker?](https://stackoverflow.com/a/49705601)  
    Docker container에선 굳이 venv를 쓸 필요가 없다. 시스템 파이썬에 pipenv 의존성을 다 설치해버려도 됨. 'You need to use --system flag, so it will install all packages into the system python, and not into the virtualenv. Since docker containers do not need to have virtualenvs'
### 비동기 프로그래밍
- [비동기 파이썬](https://mingrammer.com/translation-asynchronous-python/)  
    Hackernoon에 작성된 [Asynchronous Python](https://hackernoon.com/asynchronous-python-45df84b82434)을 번역한 글. 멀티스레딩에서 경쟁 상태나 데드락 등등은 어떻게든 해결할 수 있으나 context switching의 자원 낭비는 어째 해결할 수 없어서 비동기 프로그래밍이 설계되었다는 내용을 시작으로, Python을 기준으로 해서 그린 스레드부터 콜백 스타일, Python 3.3부터 제공된 `yield from`, asyncio의 빌트인화와 async/await 문법까지 차근차근 설명되어 있다.
- [asyncio : 단일 스레드 기반의 Nonblocking 비동기 코루틴 완전 정복](https://soooprmx.com/archives/6882)  
    asyncio를 조금 더 큰 그림에서 바라본다. `결국 이는 NodeJS가 밀고 있는 non-blocking 비동기 처리에 더 근접하는 개념이다.`와 같은 내용처럼.
- [What does the “yield from” syntax do in asyncio and how is it different from “await”](https://stackoverflow.com/a/44273861)  
    파이썬에서 비동기 IO를 위해 사용하는 두 키워드.
    - Python 3.3부터 generator가 다른 generator에게 연산의 일부를 위임하도록 하는 yield from이라는 expression을 사용할 수 있게 되었다. 이는 generator가 generator를 호출하고, 서로의 실행을 중지시킬 수 있는 방법이 생긴 것이기 때문에 비동기 프로그래밍이 원활히 가능하도록 만들어 주었다.
    - 이러한 generator들을 실행하는 이벤트 루프를 asyncio 라이브러리가 제공해주기 시작했다.
    - Python 3.5부턴 asyncio가 빌트인 라이브러리로 지원되며 `async` 키워드가 `@asyncio.coroutine`를 대체하고, `await` 키워드가 `yield from`을 대체하게 되었다.
### 표준 라이브러리
#### Data Types
- [datetime](https://www.programiz.com/python-programming/datetime)
    - [Find Monday's date with Python](https://stackoverflow.com/a/1622052)  
- [collections.OrderedDict](https://pymotw.com/2/collections/ordereddict.html)  
    내 생각엔 OrderedDict를 써볼만한 case가 그리 많진 않을 것 같은데, OrderedDict를 써야 하는 적은 case 입장에서는 정말 개이득인 컨테이너 타입인 것 같다.(메인 언어로 파이썬 쓴지 1년 넘는 동안 딱 2번 써봤지만, 그때마다 OrderedDict 덕분에 정말 편-안했음) 단지 넣은 순서대로 dictionary가 유지된다는 것 뿐이지, 자동으로 sort는 해주지 않는다는 것을 인지하고 있어야 한다.
- [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)  
    dict를 상속받은 dictionary-like한 객체를 반환한다. 이 객체는 함수에 전달된 optional argument인 default_factory를 인스턴스 변수로 가지고 있고, `__getitem__` 메소드를 오버라이딩한다. getitem 시 key가 존재하지 않으면 `__missing__` 메소드를 호출하고, 이 메소드는 `default_factory`를 호출해 반환한다. default_factory가 None이면 `KeyError`를 raise한다. invalid key에 대해 default value를 정의해 두어 KeyError를 방어하기 위해 사용된다.
- [얕은 복사(shallow copy) vs 깊은 복사(deep copy)](https://blueshw.github.io/2016/01/20/shallow-copy-deep-copy/)  
    복사 개념을 잘 모르면 이상한 걸로 삽질하게 된다. Python에서는 복사 작업을 돕기 위해 copy 모듈이 존재한다.
- [enum](https://docs.python.org/3/library/enum.html)  
    enum이야 뭐 클래스 변수로 쓰면 되지 않나? 싶었는데, 모듈에서 제공해주는 기능이 생각보다 엄청나게 많고 유용하다. enum 정의하려면 일단 Enum 클래스 상속받고 시작하는 게 좋을듯. ㅎ
#### Structured Markup Processing Tools
- [xml.etree.ElementTree](https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2)  
    svg 파싱할 때도 유용하다.
#### Data Persistence
- [pickle](https://www.datacamp.com/community/tutorials/pickle-python-tutorial)  
    객체를 그대로 binary string으로 직렬화하는 것을 pickling이라 부른다. 큰 틀은 serialization인데, Python에서만 pickling이라 부름. 아무튼 이런 pickling을 위해 pickle이라는 모듈을 사용할 수 있다. use case는 잘 모르겠다(내 기준에선 객체 직렬화라고 해봤자 웬만하면 dictionry/list인데, 이건 그냥 JSON으로 직렬화하면 되는 이슈라서). 이 아티클에서는 머신러닝 알고리즘에서 피클링이 '매우 유용'하다고 한다.
#### Python Runtime Services
- [abc](https://velog.io/@city7310/abc)  
    'Abstract Base Classes'
#### Generic Operating System Services
- [logging](https://realpython.com/python-logging/)
    - [logging.info doesn't show up on console but warn and error do](https://stackoverflow.com/questions/11548674/logging-info-doesnt-show-up-on-console-but-warn-and-error-do/11548754)  
        'The root logger always defaults to WARNING level.'
#### Functional Programming Modules
- [functools](https://www.journaldev.com/17550/python-functools)
    - [What does functools.wraps do?](https://stackoverflow.com/questions/308999/what-does-functools-wraps-do)
    - [How does the functools partial work in Python?](https://stackoverflow.com/questions/15331726/how-does-the-functools-partial-work-in-python)
#### Debugging and Profiling
- [timeit](https://docs.python.org/3/library/timeit.html)  
    짧은 Python statement에 대해 실행 시간을 측정해준다. 문제를 해결하기 위한 방법이 여러가지일 때, 시간복잡도 면에서 better way를 찾기 위해 종종 쓰게 된다.
- [Python Debugging with Pdb](https://realpython.com/python-debugging-pdb/)  
    사실 옛날엔 그냥 매 줄마다 print 찍어보면서 디버깅하곤 했었는데, 확실히 디버깅 툴을 직접 쓰는 게 러닝커브를 감안하더라도 훨씬 더 나은 것 같다.
#### Concurrent Execution
- [Intro to Threads and Processes in Python](https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b)  
    multi threading, multi processing과 파이썬의 GIL problem까지 잘 요약해 주었다.
- [파이썬의 새로운 병렬처리 API – Concurrent.futures](https://soooprmx.com/archives/5669)
#### Networking and Interprocess Communication
- [asyncio : 단일 스레드 기반의 Nonblocking 비동기 코루틴 완전 정복](https://soooprmx.com/archives/6882)
#### Data Compression and Archiving
- [gzip](https://docs.python.org/3/library/gzip.html)  
    'This module provides a simple interface to compress and decompress files just like the GNU programs gzip and gunzip would.'
#### Internet Data Handling
- [JSON - The Hitchhiker's Guide to Python](https://docs.python-guide.org/scenarios/json/)  
    'The json library can parse JSON from strings or files. The library parses JSON into a Python dictionary or list. It can also convert Python dictionaries or lists into JSON strings.'
#### Internet Protocols and Support
- [UUID objects according to RFC 4122](https://docs.python.org/3/library/uuid.html)

### 외부 라이브러리
#### CLI
- [zappa](https://github.com/Miserlou/Zappa)  
    WSGI 웹 어플리케이션을 AWS Lambda에 올려서 서버리스 어플리케이션을 잘 배포할 수 있게 도와주는 CLI 툴. maintainer가 완전 착하다..
- [twine](https://pypi.org/project/twine/)  
    Python 패키지를 PyPI(python Pacakge Index)에 쉽게 배포할 수 있도록 해주는 CLI 툴.
- [aws-cli](https://github.com/aws/aws-cli)  
    AWS 서비스를 관리하기 위한 CLI 툴. management console에서 안되고 CLI에서만 되는 것도 종종 있다. 예를 들어 CodeBuild에 hook다는 것?
- [click](https://github.com/pallets/click)  
    CLI 어플리케이션을 개발하는 걸 도와주는 라이브러리. 'Python composable command line interface toolkit'
#### Schema Validation
- [jsonschmea](https://github.com/Julian/jsonschema)  
    JSONSchema를 통한 validation 라이브러리.
- [schema](https://github.com/keleshev/schema)  
    schema validation 라이브러리. Pythonic하다고 하는데 이거 쓰려면 러닝커브가 좀 생길 것 같다. 아이디어는 괜찮은 것 같은데, 컨셉 자체가 너무 그들만의 세계같은 느낌.
- [schematics](https://github.com/schematics/schematics)  
    schema validation은 이게 제일 나은듯 ㅎ StringType()처럼 데이터의 스키마를 객체로 정의하게 되면 required, default와 같은 rule들이 생성자의 인자로 전달되기 때문에 자동완성의 도움을 받을 수 있어서 IDE 바깥으로 나가는 일이 줄어들어서 좋은 것 같다.
- [cerberus](http://docs.python-cerberus.org/en/stable/usage.html#basic-usage)  
    스키마 작성 방식이 JSONSchema와 꽤 닮아 있는 validation 라이브러리. 다만 이걸 쓴다면 자동완성의 도움을 받긴 어려울 것 같다. 나는 오타를 자주 내는 편이라, 이렇게 리터럴이 많은 것과 친해지기 쉽지 않다.
- [voluptuous](https://github.com/alecthomas/voluptuous)  
    schema와 비슷하게 생긴 validation 라이브러리인데, 비교적 잘 정리되어 있는 편. 클래스 스타일이 싫다면 이걸 써봐도 괜찮을 것 같다.
- [pydantic](https://pydantic-docs.helpmanual.io/)  
    나는 pydantic을 쓸 수 있는 환경이라면 무조건 이거 쓸 것 같다.
#### DB Driver
- [What's the difference between MySQLdb, mysqlclient and MySQL connector/Python?](https://stackoverflow.com/questions/43102442/whats-the-difference-between-mysqldb-mysqlclient-and-mysql-connector-python)  
    MySQLDB1, MySQLDB2, mysqlclient, mysql-connector-python, pymysql의 차이에 대한 이야기. CPython을 쓴다면 mysqlclient만한게 없는 것 같다.
- [mongo-python-driver(pymongo)](https://github.com/mongodb/mongo-python-driver)
- [motor](https://github.com/mongodb/motor)  
    'full-featured, non-blocking MongoDB driver for Python Tornado and asyncio applications.'
- [redis-py](https://github.com/andymccurdy/redis-py)
    'Redis Python Client'
- [pymemcache](https://github.com/pinterest/pymemcache)  
    'A comprehensive, fast, pure-Python memcached client.'
#### DB Helper
- [mongoengine](https://github.com/MongoEngine/mongoengine)  
    Node.js의 mongoose와 대응할 수 있는 ODM 라이브러리. 고딩 시절의 거의 반을 함께한 친구 ㅜㅜ
- [pypika](https://github.com/kayak/pypika)  
    SQL query builder. ORM같은 쿼리 인터페이스는 아니고, 단순히 쿼리 문자열을 만들어주는 라이브러리라서 접근 방식이 좀 다르다.
- [SQLAlchemy 시작하기 - Part 1](https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-1/)  
    짱 좋은 ORM 라이브러리 ^&^
- [peewee](https://github.com/coleifer/peewee)  
    'Peewee is a simple and small ORM.' API 자체가 '예쁘기'는 한데, SQLAlchemy를 두고 이걸 쓸 메리트가 있을런지 싶기도 하고, 당장은 트랜잭션 생각을 안해도 돼서 괜찮은 것 같기도 하고..
- [peewee-async](https://github.com/05bit/peewee-async)  
    Peewee를 async하게 쓸 수 있게 해주는 라이브러리. Sanic같은 데서 ORM 쓸 때 많은 도움을 준다.
#### HTTP
- [requests](https://github.com/requests/requests)  
    HTTP request 잘 할 수 있게 도와주는 라이브러리. 내장 라이브러리인 urllib.request를 wrapping함.
- [yarl](https://github.com/aio-libs/yarl)  
    'Yet another URL library'. URL 파싱 관련 작업을 도와준다. 내장 라이브러리인 urllib.parse 위주로 wrapping함.
- [furl](https://github.com/gruns/furl)
- [gunicorn으로 flask에서 동시에 여러 요청 처리하기](https://winterj.me/flask-concurrency-test/)
#### Async
- [uvloop](https://github.com/MagicStack/uvloop)  
    'Ultra fast asyncio event loop.'
- [aiohttp로 하는 비동기 HTTP 요청](https://item4.github.io/2017-11-26/Asynchronous-HTTP-Request-with-aiohttp/)
- [aiocache](https://github.com/argaen/aiocache)  
    async 함수에 대한 캐싱을 도와주는 라이브러리.
#### Excel Processing
- [xlrd](https://github.com/python-excel/xlrd)
- [xlwd](https://github.com/python-excel/xlwt)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [xlsxwriter](https://xlsxwriter.readthedocs.io/)
- [pyexcelerate](https://github.com/kz26/PyExcelerate)
- [파이썬 엑셀 쓰기 라이브러리 비교](https://libsora.so/posts/python-excel-library/)
#### Drop-in Replacements
- [Arrow](https://arrow.readthedocs.io/en/latest/)  
    datetime으로 타임존과 싸우는 건 사람이 할 짓이 아니다. arrow는 기본적으로 시간을 ISO 8601 format으로 다루기 때문에 타임존 conversion이 쉽고, time shifting이나 humanize 기능도 잘 준비되어 있다.
- [ultrajson(ujson)](https://github.com/esnme/ultrajson)  
    'Ultra fast JSON decoder and encoder written in C with Python bindings'
#### SaaS Helpers
- [pyfcm](https://github.com/olucurious/PyFCM)  
    'Python client for FCM - Firebase Cloud Messaging'
- [python-firebase](https://github.com/ozgur/python-firebase)  
    'Python interface to the Firebase's REST API'. pyfcm은 FCM에 한정되어 있고, 얘는 firebase 전체.
- [firebase-admin-python](https://github.com/firebase/firebase-admin-python)  
    Python용 firebase admin SDK. Firebase에서 가장 권고하는 방식이며 official로 관리된다.
- [elasticsearch-py](https://github.com/elastic/elasticsearch-py)  
    'Official Python low-level client for Elasticsearch.'
- [elastic-apm](https://github.com/elastic/apm-agent-python)  
    'Official Python agent for the Elastic APM'
- [slacker](https://github.com/os/slacker)  
    'Full-featured Python interface for the Slack API'
- [boto3](https://github.com/boto/boto3)  
    'AWS SDK for Python'
#### Crawling
- [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/)  
    'Beautiful Soup is a Python library for pulling data out of HTML and XML files.'
#### Others
- [pyjwt](https://github.com/jpadilla/pyjwt)  
    'JSON Web Token implementation in Python'
- [cachetools](https://github.com/tkem/cachetools)  
    functools.lru_cache 데코레이터의 변형을 포함하여 자주 쓰이는 캐싱들을 데코레이터 형태로 지원하는 라이브러리. LFU, LRU, RR, TTL cache를 지원한다.
- [blinker](https://pythonhosted.org/blinker/)  
    object-to-object signaling을 도와주는 라이브러리. 일종의 옵저버 패턴이라 event driven한 어플리케이션을 잘 만들 수 있도록 해줄 것 같은데, use case는 딱히 생각이 나지 않는다. 최근에 signal을 활용하는 걸 봤던 건, Elastic APM Python agent에서 Flask의 request_started, request_finished signal에 각각 트랜잭션 시작과 종료 함수를 할당해둔 것 정도.
- [apscheduler](https://github.com/agronholm/apscheduler)  
    'Task scheduling library for Python'

### 테스팅
### SQLAlchemy
- [SQLAlchemy 시작하기 - Part 1](https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-1/)
- [SQLAlchemy 시작하기 - Part 2](https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-2/)  
    SQLAlchemy 공식 튜토리얼을 번역한 글. 좋은 내용 다 담겨 있고, 이것만 정독해도 SQLAlchemy 수준있게 쓸 수 있다.
- [Flask-SQLAlchemy docs - Multiple Databases with Binds](http://flask-sqlalchemy.pocoo.org/2.3/binds/#binds)  
    Flask-SQLAlchemy에선 `SQLALCHEMY_BINDS` 설정과 모델 클래스의 `__bind_key__` 속성으로 여러 데이터베이스에 쉽게 연결할 수 있다. 그러나 일반적인 경우 read/write db를 나누어 접근하는 식이라, bind 설정 따로 안하고 그냥 db마다 engine 만들고 따로 session을 관리하는 식의 practice가 더 많다.
#### ORM
- [Basic Relationship Patterns](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html)  
    relationship에 관한 이야기. 튜토리얼에도 포함되어 있는 내용이므로 튜토리얼을 보는 게 첫 이해에는 더 좋을 수도 있다.
- [SQLAlchemy's "Lazy" Parameter](https://medium.com/@ns2586/sqlalchemys-relationship-and-lazy-parameter-4a553257d9ef)  
    relationship을 어떤 방식으로 불러올지를 lazy 속성을 통해 설정할 수 있다. 이것도 튜토리얼에 포함되어 있는 내용.
- [Column and Data Types](https://docs.sqlalchemy.org/en/latest/core/type_basics.html)  
    데이터 타입이 Generic Types/SQL Standard and Multiple Vendor Types/Vendor-Specific Types로 나뉜다는 것을 알게 됐다. Vendor-Specific Types는 한번쯤 써볼만한 것 같음.
#### Query
- [Literal SELECT](https://stackoverflow.com/a/7546802)  
    UNION 쿼리 등에서 자주 사용되는 literal SELECT를 SQLAlchemy에서는 어떻게 표현하는지에 대한 질문이다.
- [Query 객체로 WHERE절 작성하기(Common filter operators)](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators)  
    SQLAlchemy의 Query 객체에서는 WHERE 절을 filter 메소드로 표현하는데, 여기에 들어가는 일반적인 operator들에 대한 정리다.
- [How to pass a not like operator in a sqlalchemy ORM query](https://stackoverflow.com/a/5019427)  
    Bitwise not operator가 아니라, `sqlalchemy.not_` 함수를 사용해서도 NOT을 표현할 수 있다.
- [sqlalchemy.orm.query.Query.slice(start, stop)](https://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.slice)  
    Query 객체에서 LIMIT 쿼리를 표현하려면, slice 메소드를 사용하거나, __getitem__에 슬라이싱이 지원되므로 빌트인 슬라이싱 연산을 사용할 수 있다. 이건 [all 메소드의 코드](https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/orm/query.py#L2835-L2841)와 [\_\_getitem\_\_ 메소드의 코드](https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/orm/query.py#L2666-L2690), 그 바로 밑에 있는 [slice 메소드의 코드](https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/orm/query.py#L2693-L2732)를 살펴보면 도움이 많이 된다.
- [How to union two subqueries in SQLAlchemy](https://stackoverflow.com/a/20032394)  
    Query 객체의 union이나 union_all 메소드를 통해 UNION, UNION ALL 쿼리를 표현할 수 있다.
- [How to execute raw SQL in SQLAlchemy](https://stackoverflow.com/a/17987782)  
    raw SQL을 실행하는 방법
- ['select as' in SQLAlchemy](https://stackoverflow.com/a/9187589)  
    Column.label 메소드로 aliasing(SELECT AS)를 표현하는 방법
- [SQLAlchemy simple example of sum, average, min, max](https://stackoverflow.com/a/11832380)  
    sqlalchemy.sql.functions 모듈의 함수를 이용해 aggregation을 하는 방법
- [Get the number of rows in table using SQLAlchemy](https://stackoverflow.com/a/10822842)  
    쿼리에 대한 row count를 어떻게 반환받는지에 대한 질문이다. 답변의 내용처럼, 그냥 `query.count()`는 wrapped select 꼴의 쿼리를 생성하기 때문에 `session.query(func.count(...)).scalar()`같은 방식을 사용하기도 한다.
- [What's the difference between filter and filter_by in SQLAlchemy?](https://stackoverflow.com/a/2128558)  
    'filter_by is used for simple queries on the column names using regular kwargs'
- [How to implement a default condition in all SQLAlchemy's queries](https://stackoverflow.com/questions/40193259/how-to-implement-a-default-condition-in-all-sqlalchemys-queries)
- [SQLAlchemy Docs - ORM Events - Query Events](https://docs.sqlalchemy.org/en/latest/orm/events.html#query-events)
#### Engine, Connection, Session
- [SQLAlchemy: engine, connection and session difference](https://stackoverflow.com/a/34364247)  
    engine, connection, session의 차이가 무엇이고 각각 언제 써먹어야 할지를 알 수 있다.
- [Avoiding boilerplate session handling code in SQLAlchemy functions](https://stackoverflow.com/a/29805305)  
    contextlib.contextmanager를 통해 session을 다루는 보일러플레이트를 with-as 문으로 관리하도록 만드는 패턴
- [Contextual/Thread-local Sessions](https://docs.sqlalchemy.org/en/latest/orm/contextual.html)  
    context에 의존하는 어플리케이션에 적용하기 적합한 scoped_session에 대한 가이드. 하나의 스레드에서 동일한 세션을 이용해 여러 작업을 처리하는 경우, 함수에 session을 파라미터로 넘겨줘서 session을 유지하는 경우가 많은데 scoped_session을 사용하면 이러한 문제가 줄어든다.
- [Dealing with duplicate primary keys on insert in SQLAlchemy](https://stackoverflow.com/a/11620706)  
    질문이 굉장히 세세한데, 결론은 `session.add` 대신 `session.merge` 메소드를 사용하면 primary key duplicate 시 알아서 update하도록 만들 수 있다는 것이다.
- [SQLAlchemy Transaction 관리 Practice 공유](https://blog.qodot.me/post/sqlalchemy-transaction-%EA%B4%80%EB%A6%AC-practice-%EA%B3%B5%EC%9C%A0/)  
    데이터베이스에 접근할 때마다 context를 열지 않고, 데코레이팅된 함수 단위로 세션을 발급하는 식으로 트랜잭션을 관리하는 practice다. Flask에 SQLAlchemy를 엮어서 쓸 때마다 단지 'with문 쓰는게 좀 번거롭다' 정도만 생각했지, 더 나은 방법을 생각하려고 하지 않았던 게, 내 머리에서 이런 아이디어가 나오지 않았던 이유인 것 같다.
- [Unbind object from session](https://stackoverflow.com/questions/11213665/unbind-object-from-session/11213780)  
    'Expunge removes an object from the Session, sending persistent instances to the detached state, and pending instances to the transient state.' contextmanager로 세션을 쓰다 보면, with문 바깥에서 객체 접근 시 session bind 문제가 발생한다. 이를 해결하기 위해 객체를 session에서 unbind해주는 session.expunge()를 쓸 수 있다.
- [Session Management - Refreshing / Expiring](https://docs.sqlalchemy.org/en/latest/orm/session_state_management.html#refreshing-expiring)
- [How to close sqlalchemy connection in MySQL](https://stackoverflow.com/questions/8645250/how-to-close-sqlalchemy-connection-in-mysql)  
    SQLAlchemy에서 active되어 있는 connection들을 어떻게 닫는지에 대한 질문.
### Peewee
- [Dynamically defining a database](http://docs.peewee-orm.com/en/latest/peewee/database.html#dynamically-defining-a-database)  
    Peewee는 모델을 정의할 때 `Meta`라는 inner class를 정의하고 `database` 속성에 데이터베이스 객체를 명시해놓아야 한다. 데이터베이스 명시를 동적으로 정의하려면 Proxy 객체를 그 자리에 넣어두고, `initialize` 메소드로 lazy하게 바인딩해 준다. 동일한 모델에 대해 read/write db 세션을 나누어 접근하기 위해 `UserReadModel`, `UserWriteModel`처럼 나누는 건 너무 아닌 것 같아서 proxy 개념을 써먹어보고 있는데, 좋은 practice인지는 모르겠다.
- [How to custom the table name in peewee?](https://stackoverflow.com/a/48024676)  
    peewee는 모델 클래스 이름을 그대로 lowercase해서 테이블을 찾는데, Meta 클래스의 `db_table` 속성을 통해 테이블 이름을 별도로 명시할 수 있다.
- [Performing simple joins](http://docs.peewee-orm.com/en/latest/peewee/relationships.html#performing-simple-joins)  
    peewee로 기본적인 join 쿼리를 작성하는 방법이다. join에서 `ON` 쿼리를 작성하려면 join 메소드에 on 인자로 criterion을 넘겨줘야 한다.
- [Joining multiple tables](http://docs.peewee-orm.com/en/latest/peewee/relationships.html#joining-multiple-tables)  
    peewee 가이드에서 여러 테이블의 join에 대한 부분이다. join type에 대한 명시 방법, join context에 대한 이야기, `join_from` 메소드에 대한 가이드가 들어 있다.
### MongoEngine
### Zappa
- [Enabling CORS](https://github.com/Miserlou/Zappa#enabling-cors)  
    웹 어플리케이션에서 CORS를 처리하기 위해 Flask-CORS같은 extension을 사용하곤 하는데, 사실 API Gateway 단에서도 CORS를 지원한다. `zappa_settings.json`에서 `cors` 속성을 `true`로 설정하면 반영된다.
- [Scheduling](https://github.com/Miserlou/Zappa#scheduling)  
    CloudWatch Events 기능을 통해 lambda function을 스케줄링할 수 있는데, `zappa_settings.json`에서 `events` 속성을 정의하는 것으로 편하게 설정 가능하다. 따로 분리된 cronjob 함수를 WAS와 함께 관리하기 좋음.
- [X-Ray Tracing](https://github.com/Miserlou/Zappa#aws-x-ray)  
    이것도 사실 API Gateway 기능인데, 대시보드 들어가서 켜기 귀찮을까봐 zappa 단에서 지원해준다. X-ray는 어플리케이션 성능 데이터들을 트레이싱해서 서비스맵으로 시각화해주는 도구인데, APM 용도로도 써먹을 수 있어서 요긴하게 써먹기 좋다.
### boto3
- [When to use a boto3 client and when to use a boto3 resource?](https://stackoverflow.com/a/39273710)  
    boto3.resource는 단지 boto3.client를 wrapping한 high level API이며, boto3.resource는 boto3.client의 모든 API를 래핑하지 않으므로 어쩔수 없이 boto3.client나 boto3.resource.meta.client를 사용해야 한다는 것을 잘 요약해준 것 같다.
- [boto3 - credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#configuring-credentials)  
    boto3가 credential을 어디서 가져오는지, 우선순위는 어떤지에 대한 문서.
- [Upload-Download File From S3 with Boto3](https://qiita.com/hengsokvisal/items/329924dd9e3f65dd48e7)  
    boto3로 S3에 객체를 업로드하고, 다운로드하는 기본적인 인터랙션에 대한 가이드.
- [How do I get the file/key size in boto S3?](https://stackoverflow.com/a/5498841)  
    버킷에서 특정 객체의 size를 얻어오기 위한 방법. s3 client 객체의 head_object로 객체에 HEAD 요청을 보내면 된다.
## Golang
### 언어 자체에 대한 이야기
- [고루틴은 어떻게 동작하는가?](https://stonzeteam.github.io/How-Goroutines-Work/)

# AWS
- [AWS 101 : Regions and Availability Zones](https://blog.rackspace.com/aws-101-regions-availability-zones)  
    Region과 AZ(Availability Zones)에 대한 설명. 물리적 데이터 센터인 Availability Zone들을 지리적 위치에 따라 Region 개념으로 묶고, 각 Region은 다른 Region들과 물리적으로 격리되어 있다.
## 컴퓨팅
### EC2
- [EC2(Elastic Compute Cloud)](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/concepts.html)  
    컴퓨팅 엔진. 말 그대로 그냥 컴퓨터 하나 대여해 주는거라 EBS(Elastic Block Storage)를 붙여서 Druid를 올리거나, ProxySQL, VPN 서버 등 AWS에서 관리형으로 제공하지 않는 것들을 올리는 데에도 쓰고, 웹 어플리케이션 서버를 통으로 올리는 경우나, ECS(Elastic Container Service)가 컨테이너를 동작시키는 컴퓨팅 엔진, 마인크래프트 서버 구축 등 여러 용도로 사용할 수 있다.
- [인스턴스 수명 주기](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html)
- [인스턴스 유형](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/instance-types.html)  
    instance family라고도 부른다. 하드웨어 스펙이 어디에 최적화되도록 설계되었는지에 따라 다르게 분류함. EC2에 올리려는 컴포넌트의 특징에 따라 인스턴스 유형을 잘 선택하면 남는 리소스도 줄이고 비용 최적화에도 좋을 것 같다. ElasticSearch 올릴 때 D2나 I3 쓴다거나..
- [인스턴스 구입 옵션](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/instance-purchasing-options.html)  
    온디맨드, 스팟, 예약 인스턴스만 알고 있었는데 몇가지 더 있었다. 스팟, 예약 인스턴스 잘 써먹으면 비용 최적화에 도움 많이 될듯.
- [Application Load Balancer 서비스 공개](https://aws.amazon.com/ko/blogs/korea/new-aws-application-load-balancer/)  
    AWS 블로그의 글이다. 일반적으로 로드밸런싱은 OSI 모델 기준 layer 4(transport layer)나 layer 7(application layer)에서 처리한다. ELB(Elastic Load Balancer)는 layer 4 로드 밸런싱을 제공하는데, layer 7 로드 밸런싱을 위해 ALB를 사용할 수 있다. application layer에서는 transport layer에서 할 수 없었던 패킷 접근이 가능한데, 이 덕분에 HTTP 요청의 내용(헤더, URL 등)을 가지고 rule을 만들어서 패킷 전송 위치를 지정할 수 있다. ELB를 세팅할 때 application load balancer와 classic load balancer가 선택지로 제공된다.
- [배치 그룹(Placement Gorup)](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/placement-groups.html)  
    placement group을 설정해 두면 group에 있는 인스턴스들이 '물리적으로 가까운 위치'에 할당된다. latency 확보에 도움을 준다고는 하는데, 유의미한 수준인지는 모르겠다.
#### EBS
- [EBS(Elastic Block Storage)](https://aws.amazon.com/ko/ebs/?nc=sn&loc=1)  
    EC2 인스턴스에 마운트해 사용할 수 있는 블록 스토리지. 데이터를 다루는 클러스터를 직접 운영(ex - ElasticSearch, Druid, ...)하는 경우 extra storage가 필요한데, EBS가 그걸 해결해 준다.
- [EBS 최적화 인스턴스](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/EBSOptimized.html#enable-ebs-optimization)  
    인스턴스에 EBS 전용 대역폭을 만들어서 EBS에 대한 처리량과 IOPS를 늘리는 것. 현재 세대 인스턴스들은 기본적으로 EBS 최적화되어 있는 상태.
#### ELB
- [Application Load Balancer 시작하기](https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/application/application-load-balancer-getting-started.html)  
    나같은 WAS돌이들은 ALB를 자주 쓰게 된다. target group 만들고, target group에 target 등록하고, LB에 타겟(listener) 등록해주면 된다.
- [Application Load Balancer를 통한 경로 기반 라우팅 사용](https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/application/tutorial-load-balancer-routing.html)  
    ALB에는 rule이라는 게 있어서, URL을 기반으로 포워딩할 listener를 설정해둘 수 있다.
### ECS
- [ECS(Elastic Container Service)](https://docs.aws.amazon.com/ko_kr/AmazonECS/latest/developerguide/Welcome.html)  
    어플리케이션을 docker 등으로 컨테이너화 하면, 독립된 실행 환경이 보장되고 빌드 스크립트가 파일 형태로 관리되어 배포 과정이 깔끔해진다. 가장 문제는 이러한 컨테이너를 orchestration하는 일인데, 이 일을 ECS가 대신 해준다. ECS는 Kubernetes같은 Docker 컨테이너 orchestration 서비스. EC2를 기반으로 동작시키거나, EC2 인스턴스를 직접 관리하기 부담스러운 경우 Fargate를 사용할 수도 있다.
- [Fargate](https://aws.amazon.com/ko/blogs/korea/aws-fargate/)  
    서버리스 컨테이너 컴퓨팅 엔진. 컨테이너를 위한 인스턴스를 EC2 등으로 직접 관리할 필요 없이, 컨테이너 자체만 제공하면 알아서 잘 관리해 준다.
### ECR
- [ECR(Elastic Container Repository)](https://aws.amazon.com/ko/ecr/)  
    말 그대로 Docker 컨테이너 저장소를 제공한다. ECS와 잘 통합되므로 배포 프로세스에도 도움을 많이 준다.
### Lambda
- [Lambda](https://aws.amazon.com/ko/lambda/features/)  
    '이벤트에 응답하여 코드를 실행'하는 서버리스 컴퓨팅 서비스. Event Driven한 거라면 뭐든 붙여볼 수 있다. API Gateway랑 엮어서 API 서버 용도로도 사용할 수 있고, 뭔가 스케줄링하는 용도로 사용할 수도 있고 등등.
- [Lambda Function Versioning and Aliases](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html)  
    Lambda function에는 버전과 alias(별칭) 개념이 있다. 세상에. Lambda function을 업데이트할 때마다 버전이 하나씩 올라가고, 최초 생성된 lambda function의 기본 별칭인 `Unqualified`는 `$LATEST`라는 와일드카드 표현식으로 항상 가장 최신 버전을 가리킨다. 버전과 별칭으로 나뉜 lambda function들은 각기 다른 unique한 ARN(Amazon Resource Name)을 가진다. 함수 이름이 `test`라면, 버전 7의 함수는 `arn:aws:lambda:<region>:<acct-id>:function:test:7`, 별칭이 PROD인 함수는 `...:test:PROD`같은 식. serverless나 zappa 등의 툴킷으로 lambda에 서버리스 웹 어플리케이션을 배포하면, 함수가 업데이트될 때마다 알아서 새 버전을 가르키도록 Unqualified alias에 API Gateway를 매핑해 둔다.
## 스토리지
### S3
- [S3 Storage Classes](https://aws.amazon.com/ko/s3/storage-classes/)  
    S3에도 종류가 있다. 웹페이지 리소스나 콘텐츠 저장 용도로는 대부분 검색 요금이 따로 발생하지 않는 S3 Standard를 사용하고, 오래된 로그 데이터같이 액세스 빈도가 낮은 데이터는 비용 최적화를 위해 S3-IA(Infrequent Access)나 RRS(Reduced Redundancy Storage)를 고려해볼 수 있다. Intelligent Tiering과 Glacier Deep Archive는 처음 알았다.
- [버킷 정책 예제 - 특정 IP 주소 액세스 제한](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-3)
- [버킷 정책 예제 - Amazon CloudFront 오리진 자격 증명에 권한 부여](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-6)  
    보안 주체(principal)를 cloudfront canonical user id에 한정해서 CloudFront에게만 권한을 부여하는 방식.
### EFS
- [EFS(Elastic File System)](https://aws.amazon.com/ko/efs/)  
    EBS와의 차이는, 여러 EC2 인스턴스에 동시 마운트할 수 있다는 점이다. 엄청 비쌈. 클러스터 환경에서 데이터 처리할 때 써먹을 수도 있지 않을까 싶다.
## 데이터베이스
### RDS
### Aurora
- [Aurora Serverless - Features, Limitations, Glitches](https://medium.com/searce/amazon-aurora-serverless-features-limitations-glitches-d07f0374a2ab)  
    Serverless 형태의 완전 관리형 Aurora 인스턴스. 정확히는 RDS에서 Aurora를 띄울 때 serverless 타입을 선택할 수 있다. Auto Scaling이 제공되고, Aurora가 자체적으로 multi-AZ에 데이터를 복제한다. VPC 내에서만 동작하고 별도로 VPC peering도 불가능하지만 Direct Connect로 해결 가능한데, 비용이 RDS 프로비저닝과 얼마나 차이날 지 궁금하다.
- [Aurora 로컬 스토리지 성능 테스트](http://woowabros.github.io/r-d/2019/03/22/localstorage.html)
### DynamoDB
### ElastiCache
### DocumentDB
- [Amazon DocumentDB 신규 출시](https://aws.amazon.com/ko/blogs/korea/new-amazon-documentdb-with-mongodb-compatibility-fast-scalable-and-highly-available/)  
    MySQL 호환 데이터베이스인 Aurora를 알았을 때, 뭔가 Document-Oriented NoSQL DB도 하나쯤 만들지 않을까 싶었는데 진짜 만들었다. MongoDB 호환 가능하고, AWS답게 replication 짱짱하고 스토리지 auto scaling 잘 되고, 역시나 완전 관리형이다. 나중에 한 번 써봐야지.
### TimeStream
- [TimeStream](https://aws.amazon.com/ko/timestream/)  
    2018 AWS re:invent때 공개된 완전 관리형 time series 데이터베이스. 완전 좋아 보이는데 일단 써봐야 알 것 같다. 1000X faster at 1/10th the cost 뭐 이러는데 일단 SQL-like 쿼리 인터페이스가 있다는 거랑 서버리스로 구성돼 있어서 관리 포인트가 줄어든다는 게 좋은 것 같다. ELK는 비싸고 대안이 딱히 없는 것 같아서 InfluxDB 쓰는데 이제 이거 EC2에 프로비저닝 안해도 되겠당. 물론 써봐야 알겠지만. grafana같은 time series visualize 툴들이 timestream 대응하느라 바빠질듯.
## 마이그레이션, 전송
### DMS
- [DMS(Database Migration Service)](https://aws.amazon.com/ko/dms/)  
    데이터베이스 마이그레이션 서비스. 동종 데이터베이스 마이그레이션 뿐만이 아니라, 이기종 데이터베이스 플랫폼 간 마이그레이션(예를 들면, Oracle Database -> AWS Schema Conversion Tool -> Aurora Database)도 가능하다. 물론 소스 데이터베이스가 RDS 또는 EC2에 있어야 한다.
### Snowball
- [Snowball](https://aws.amazon.com/ko/snowball/)  
    데이터를 네트워크로 전송하는 것은, 대용량 데이터 관점에서 매우 느리다. Snowball은 대용량 데이터를 물리적으로 마이그레이션하는 것을 돕는다. AWS Management Console에서 작업을 생성하면 AWS가 물리적인 스토리지 디바이스(Snowball)를 본인에게 배송하고 -> Snowball 클라이언트를 통해 이 디바이스에 연결해 데이터를 업로드한 후 -> AWS에게 Snowball 디바이스를 반송 -> AWS가 이를 S3에 업로드하는 방식이다.
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
    private git repository 호스팅 서비스! 외부 이슈 트래커랑 연동도 되는 듯.
### CodeBuild
- [AWS CodeBuild](https://docs.aws.amazon.com/ko_kr/codebuild/latest/userguide/welcome.html)  
    완전 관리형 빌드 서비스! VPC 내에 속하고, security group을 가질 수 있다는 게 정말 큰 메리트.
- [CodeBuild의 build spec reference](https://docs.aws.amazon.com/ko_kr/codebuild/latest/userguide/build-spec-ref.html)  
    CodeBuild가 레포를 clone해서 빌드를 위해 buildspec.yml을 찾는데, 여기에 들어갈 수 있는 것들을 정리한 문서. 여타 CI들과 다르지 않게 phase 기반으로 동작한다.
- [Environment variables not being set on AWS CodeBuild](https://stackoverflow.com/questions/50706276/environment-variables-not-being-set-on-aws-codebuild)  
    CodeBuild에서 buildspec.yml에 명시한 export 명령어가 제대로 먹히지 않는 현상에 대한 트러블슈팅. 버전을 0.2로 올리면 된다고 한다.
### CodeDeploy
- [AWS CodeDeploy를 통한 배포 자동화](http://blog.dramancompany.com/2017/04/aws-code-deploy%EB%A5%BC-%ED%86%B5%ED%95%9C-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94/)  
    EC2, ECS 등의 인스턴스에 대한 배포 자동화에 도움을 주는 착실한 친구. 그런데 뭔가 '배포 자체'에 대해 많이 챙겨줘서, Canary Test/Blue-Green Deploy, 롤백 등의 지원이 필요 없으면 안 쓰게 될 것 같기도 하다.
## 관리
### CloudWatch
- [일정에서 트리거되는 CloudWatch 이벤트 규칙 생성](https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Scheduled-Rule.html)  
    모니터링 도구인 CloudWatch에는 Events라는 하위 기능이 있다. 이벤트 패턴이나 일정을 이벤트 소스로 선택하고, 이벤트가 발생했을 때 lambda, step function, EC2 인스턴스 재부팅 등 타 AWS 서비스를 호출할 수 있다. 이 문서는 일정을 이벤트 소스로 트리거하는 CloudWatch 이벤트 규칙을 생성하는 방법을 다룬다. Linux의 cron과 비슷한 용도로 사용할 수 있다.
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
    IAM 알못이 읽으면 엄청 많은 것을 습득할 수 있는 설명서. 영어 버전으로 보는 게 더 나을 것 같다.
- [Difference between IAM role and IAM user in AWS](https://stackoverflow.com/a/48182754)  
    'IAM controls: Who (authentication) can do What (authorization) in your AWS account.', 'Roles - are used to grant specific permission to specific actors for a set of duration of time. **These actors can be authenticated by AWS or some trusted external system.**'
### KMS
### WAF
- [AWS WAF](https://aws.amazon.com/ko/waf/)  
    이걸로 CloudFront에 특정 IP만 접근할 수 있도록 할 수 있다.
## 어플리케이션 통합
### Step Functions
### Amazon MQ
### SNS
### SQS

## 고객 참여
### SES
- [Amazon SES에서 이메일 전송 테스트](https://docs.aws.amazon.com/ko_kr/ses/latest/DeveloperGuide/mailbox-simulator.html)  
    이메일 전송과 관련된 테스트를 수행하는 것을 돕기 위해, AWS SES에서 자체적으로 지원하는 시뮬레이션용 메일.

# 모바일
- [배달의민족 앱에 적용된 오프라인 모드에 대하여](http://woowabros.github.io/experience/2018/11/05/about_offline_mode.html)
- [회사나 고객에게 효과적으로 Flutter 소개하는 방법을 알려드립니다](https://developers-kr.googleblog.com/2019/01/pitching-flutter.html?fbclid=IwAR1b8eLPhcZDvXTTr_x0rhVWSOVP8gkJxBThmcHX2Ktvro0OKw5blX7PFM8)
## Android
- [Android 공식 가이드](https://developer.android.com/guide/index.html?hl=ko)
- [Android의 HTTP 클라이언트 라이브러리](http://d2.naver.com/helloworld/377316)
- [Using Retrofit 2.x as REST client](http://www.vogella.com/tutorials/Retrofit/article.html)
- [Retrofit 2와 함께하는 정말 쉬운 HTTP](https://academy.realm.io/kr/posts/droidcon-jake-wharton-simple-http-retrofit-2/)  
    Realm academy같은 게 백엔드에는 없는게 너무 아쉽다. 내가 못 찾는건가..
- [Firebase를 실제 모바일 백엔드로 사용하면 일어날 수 있는 일들](https://academy.realm.io/kr/posts/firebase-as-a-real-mobile-backend/)
- [Android의 ORM](http://d2.naver.com/helloworld/472196)
- [Android의 이미지로딩 라이브러리](http://d2.naver.com/helloworld/429368)
- [Android 앱 메모리 최적화](http://d2.naver.com/helloworld/539525)
- [안드로이드 BadTokenException의 원인과 해결방법](https://blog.sangyoung.me/2016/12/28/BadTokenException/)  
    context알못에게 큰 시련과도 같은 BadTokenException. 내 경우 retrofit의 onResponse에서 다이얼로그를 띄울 때 ContextWrapper.getApplicationContext()의 반환을 전달했더니 났던 오류다.
- [Android와 개발 패턴](https://tosslab.github.io/android/2015/03/01/01.Android-mvc-mvvm-mvp)
- [안드로이드의 MVC, MVP, MVVM 종합 안내서](https://academy.realm.io/kr/posts/eric-maxwell-mvc-mvp-and-mvvm-on-android/?fbclid=IwAR0aQa3j7nSTgB5TMsFt33iviV8ReW0oGvkvVBucWrBcgV0v6XWsKwjljhI)
- [AWS codebuild + codecov 로 저렴하게 android CI 구축하기](https://medium.com/@SungMinLee/aws-codebuild-codecov-%EB%A1%9C-%EC%A0%80%EB%A0%B4%ED%95%98%EA%B2%8C-android-ci-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-2a209651c4f7)
- [클린 아키텍처와 함께하는 배민앱 (Android)](http://woowabros.github.io/experience/2019/01/17/baeminapp-clean-architecture.html?fbclid=IwAR3GrdvlbN0uCcZJsGgh3jUpv6vF2T0rCBEZ7EdUIy-J3Hogio7XjhXr6jQ)
- [epoxy](https://github.com/airbnb/epoxy)
- [Use Android Jetpack to Accelerate Your App Development](https://android-developers.googleblog.com/2018/05/use-android-jetpack-to-accelerate-your.html?m=1)  
    Google의 Single Activity Architecture 권고의 시작을 알리는 Jetpack
## iOS

# 웹 프론트엔드
## CSS
- [PostCSS](https://medium.com/@FourwingsY/postcss-%EC%86%8C%EA%B0%9C-727310aa6505)
- [webpack3 + postcss 설정하기](https://medium.com/@FourwingsY/webpack-postcss-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0-34f9c486093a)
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
## TypeScript
- [우리(Reddit)가 Typescript를 선택한 이유](https://medium.com/@constell99/%EC%9A%B0%EB%A6%AC%EA%B0%80-typescript%EB%A5%BC-%EC%84%A0%ED%83%9D%ED%95%9C-%EC%9D%B4%EC%9C%A0-b0a423654f1e)
