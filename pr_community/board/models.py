from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,
                                verbose_name='제목')# vorbose_name의 의미 정의는 노트 4번 참고!
    contents = models.TextField(verbose_name='내용') 
    writer = models.ForeignKey('pruser.Pruser',on_delete=models.CASCADE,              # 사용자가 탈퇴하면 사용자의 모든 기록을 삭제하겠다는 코드
                                verbose_name='작성자')    # dttm은 datetime의 약자로 사용!
    registered_dttm = models.DateTimeField(auto_now_add=True,  # auto_now_add=True 자동으로 현시간 저장! /Flask에 비해 편리
    verbose_name='등록시간')
    
    def __str__(self):
        return self.title # 새로 만든 유저 문구는 클래스를 문자열로 변환했을때 나오는값이지만
                            # __str__ 이라는 내장함수를 파이썬은 갖고 있다

    class Meta:
        db_table = 'pr1_board' # 기본적으로 추가되는 앱들과 구분하기 위해 생성
        verbose_name = '프로젝트 게시글'
        verbose_name_plural = '프로젝트 게시글'# 복수형도 표시되게 하는 코드
                

