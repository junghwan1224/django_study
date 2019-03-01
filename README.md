django study

2월 A팀 프로젝트 레퍼지토리

중고 거래 플랫폼 토이 프로젝트

프로젝트 명: djungo

1차적인 기능 구현은 완료했으나, 디테일한 부분은 아직(css, 예외처리 등등..)



accounts: 계정 관련 앱, 소셜 로그인 테스트 코드 및 djungo 회원가입/로그인 기능

blog: 1월 장고 스터디 때 장고 기본 공부했던 앱

category: djungo 주요 기능관련 담당 앱

- 게시글 작성 - 구매/판매글 선택, summernote로 본문 작성, 섬네일 이미지 첨부
- 댓글
- 거래 신청
  - 게시글 모델인 Post 모델에서 apply_user 필드를 만들었다.
  - ManyToMany 필드로 선언을 했고, 거래 신청 버튼 클릭 시
  - add 메서드로 apply_user에 추가
- 거래 매치
  - 유저가 프로필 페이지로 들어가면
  - 내가 작성한 글에 거래 신청한 유저의 아이디 표시, 그리고 옆에 거래매치 버튼 추가
  - 내가 거래 신청한 글도 있음
  - (프로필 관련 템플릿은 accounts 앱에 있으나 관련 로직은 category 앱에 있음)
  - 거래 매치 버튼 클릭 시, send_mail 메서드를 통해 거래매치가 성사되었다는 내용의 메일 전송(단순 html의 a태그로만 메일 본문 작성)
  - 메일 본문의 링크 누르면 다시 해당 사이트로 넘어가짐

edit: summernote 에디터 테스트를 위한 app
