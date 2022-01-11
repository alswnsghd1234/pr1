# 사용 설명서


1. setting.py 안의
	installed_app에 생성한 디렉토리(게시판 , 유저) 입력

2. user 디렉토리에서
	models.py 작성

3. pr_community안에 vs code 안의 git bash로 들어감
	python manage.py migrations  입력 실행
	user 
4. models.py에 클래스 선언
	models.py 파일 예시

	from django.db import models


	class Bookmark(models.Model):
		title = models.CharField(max_length=100, blank=True, null=True)
		url = models.URLField('url', unique=True)

		class Meta:
			verbose_name = '북마크'
			verbose_name_plural = '북마크 모음'
			ordering = ['title', ]

		def __str__(self):
			return self.title
			
verbose_name 옵션
사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시된다. 영어를 기준으로 단수형이다.

verbose_name 옵션을 지정하지 않으면 CamelCase 클래스 이름을 기준으로 camel case 이와 같이 모두 소문자로 변경한다.

5. python manage.py makemigrations
   python manage.py migrate
   setting지에 있떤 앱들을 자동으로 생성!!
   ㄴ db.sqlite3 생성됨!! setting.py DATABASE 클래스에 상세 내용이 적혀있따!
   
    (vs code 안의 git bash로 sqlite 연결하려면
    extension으로 sqlite 설치 후, 음... 컨톨 쉬프 피 누른담에.. 열고 싶은 db 클릭!
	ㄴ 그 후 탐색기가서 맨아래 보면 sqlite explorer 생성되어 있음.\) <- 이건 ㄹㅇ 최후의 수단..
	

6. vs code 안의 git bash로 sqlite 연결하려면 **
	https://5-ssssseung.tistory.com/52 들어가서 따라하기!!
	
	sqlite3 db.sqlite3 
	.tables <- table 확인
	.schema 여기는 테이블 조회시 오른쪽 맨아래 만들어놓은 테이블명으로!! <- table생성
	** 변경사항이 있다면. 변경 후
	python manage.py makemigrations
	python manage.py migrate 실행
	sqlite 상태가 아닌 기본 가상환경 상태에서 python manage.py runserver 실행 후
	주소가 뜨면 url에 입력 후 / 뒤에 admin 입력하면 관리창이 뜬다.
	창을 닫고 계정을 만들 때는 python manage.py createsuperuser
	
7. 새로운 아이디 생성 관리하기
	admin.py안으로 입장
	
	from django.contrib import admin
	from .models import Pruser
	 Register your models here.

	class PruserAdmin(admin.ModelAdmin):
		pass

	admin.site.register(Pruser, PruserAdmin)
	
------------알면 유용한 꿀팁 -----------
html 파일이 dj로 나올 때 설정에 들어가서 파일 > Files: Associations > dic key = *.html value = html 추가!
if emet이 안 될 경우 설


8. templates 에 register.html 작성
	부트스트랩 사용..
	부트스트랩 홈 > doc > css html 복붙
	meta 부분도 헤드에 복붙
	body 부분에 그리드를 사용하기 때문에 div class='container'사용 , row, col-12 입력
	부트스트랩 홈> forms 에서  forms 형식 가져온다.
	
9. models 는 DB 관리하는곳
	views 는 API 역할
	views 의 회원가입 로직 꼭 알아놓기!!
	if db에 목록 추가 시 . views, models,html 변경 필수!!
	변경 후 makemigration , migrate 
	
10. bootstrap css 적용방법은
  기존에 사용하던 CDN 방식을 주석처리 후 bootstrap 5.1 themes free 이런식으로 치면
  사이트 나오고 거기서 quat? click > boot.min.css 다운받아서 static 폴더 만든거에 저장
  setting 들어가서 경로 세팅 해줘야된다.
  for example) STATIC_URL = 'static/'
              STATICFILES_DIRS = [
              os.path.join(BASE_DIR,'static'), # static 파일은 css, js 보관용 디렉토리
              이런식으로.

	
