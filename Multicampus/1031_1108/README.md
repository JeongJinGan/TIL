## 📝프로젝트 개요

| 프로젝트 목적 | 웹 프레임워크 Django와 HTML / CSS / JavaScript를 활용한 콘텐츠 기반 커뮤니티 웹 플랫폼 개발 |
| ------------- | ------------------------------------------------------------ |
| 프로젝트 기간 | 10.31 (월) ~ 11.07 (월)                                      |
| 발표 날짜     | 11.08 (화)                                                   |
| 팀명          | CafeMaster                                                   |
| 주제          | 맛집 정보 및 후기 공유 커뮤니티 서비스                       |
| 팀장          | 박선영                                                       |
| 발표자        | 문재윤                                                       |
| PPT 제작자    | 간정진                                                       |
| PPT 제작자    | 이현성                                                       |



## 주제 사전 조사 & 분석

🔎 선택한 주제와 유사한 서비스를 조사하고 분석합니다. 참고할 사이트와 자료를 기록

[망고플레이트: 나만의 맛집 검색](https://www.mangoplate.com/)

https://www.siksinhot.com/

⚙️서비스 주요 기능

- 회원관리
  - 회원가입
  - 로그인
  - 로그아웃
  - 회원 프로필
  - 위치 정보
  - 팔로우
  - 맛집 좋아요
- 리뷰 작성 CREATE
  - 해시태그
  - 별점
  - 글 작성
  - 사진
  - 이어쓰기
- 리뷰 목록 READ
  - 카테고리별로 맛집 보여주기
  - 위치 정보 기반으로 맛집 보여주기
    - 크게크게
    - 로그인X: 서울 기준 맛집 보여주기
    - 로그인O: 회원 위치 기준 맛집 보여주기
  - 랜덤 맛집
  - 신상 카페
- 검색
  - 지역
  - 카페 이름
  - 드롭다운 → 지역

**해시태그**

\#감성이충만한 #디저트가맛있는 #힙한 #커피가맛있는 #풍경이예쁜 #공부하기좋은 #데이트하기좋은 #이색적인

## DB 모델링(ERD)

🧾 서비스를 구현하기 위한 데이터베이스의 ERD를 작성

![cafemaster](../Markdown.assets/cafemaster.png)



## 화면설계(피그마)

🎨 PPT / 피그마 / 카카오 오븐 등의 도구를 활용해서 화면을 설계 합니다. 최소 페이지의 레이아웃은 설계

![index.html](../Markdown.assets/index.html.png)

![search.html](../Markdown.assets/search.html.png)

![detail.html](../Markdown.assets/detail.html.png)

![create.html](../Markdown.assets/create.html.png)

![user_detail.html](../Markdown.assets/user_detail.html.png)



## 실제 웹사이트 화면

![image-20221112010834219](../Markdown.assets/image-20221112010834219.png)



![image-20221112010844175](../Markdown.assets/image-20221112010844175.png)



![image-20221112010848506](../Markdown.assets/image-20221112010848506.png)



![image-20221112010852325](../Markdown.assets/image-20221112010852325.png)



![image-20221112010856890](../Markdown.assets/image-20221112010856890.png)

![image-20221112010900408](../Markdown.assets/image-20221112010900408.png)

![image-20221112010907313](../Markdown.assets/image-20221112010907313.png)

<img src="../Markdown.assets/image-20221112010923635.png" alt="image-20221112010923635" style="zoom:50%;" />





<img src="../Markdown.assets/image-20221112010936050.png" alt="image-20221112010936050" style="zoom:50%;" />

<img src="../Markdown.assets/image-20221112010940218.png" alt="image-20221112010940218" style="zoom: 50%;" />

[헤로쿠배포](https://calm-waters-53067.herokuapp.com/articles/)



## 프로젝트 후기

1.박선영: 먼저 처음으로 프론트와 백으로 나누어서 해보았는데 각자 맡은 분야만을 집중할 수 있어서 너무 좋았습니다. 특히 브랜치를 나누어서 공동 개발을 하면서 시간을 효율적으로 사용할 수 있어서 좋았습니다. 그리고 팀장을 맡았는데 다른 분들도 너무 잘 따라주시고 같이 이끌어 주셔서 감사했고, 처음으로 긴 시간 프로젝트를 함께 하면서 혼자 자바스크립트를 공부할 시간도 있어서 도움이 많이 됐습니다.

2.문재윤: 처음으로 일주일동안 진행되는 긴 프로젝트를 통해 협업의 중요성을 깨달았고 팀원들과의 호흡과 화합이 중요하다는 것을 다시 한번 느꼈습니다.

3.이현성: 깃 협업에 대하여 많이 배우고 내가 모르는 부분이 무엇인지 알 수 있는 좋은 시간이었습니다. 또 팀원들과의 단합의 중요성을 느꼈습니다.

4.간정진: 프로젝트 시작하기에 전에 많은 걱정이 있었지만 좋은 팀원분들을 만나, 긍정적인 환경에서 어려움없이 개발을 진행할 수 있는 좋은 기회였습니다.
