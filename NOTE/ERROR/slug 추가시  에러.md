It is impossible to add a non-nullable field 'slug' to post without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null 
value for this column)
 2) Quit and manually define a default value in models.py.


"post" 모델에 null이 허용되지 않는 필드 'slug'를 추가할 수 없습니다.
데이터베이스는 기존 행(데이터)에 이 필드를 채울 어떤 값이 필요하기 때문입니다.
다음 중 하나를 선택하세요:

1. 지금 임시 기본값을 입력하세요. (이 값이 기존 데이터의 null인 컬럼에  모두 적용됩니다)

2. 종료하고 models.py에서 기본값을 직접 지정하세요.

---
## 해결
'''
    slug = models.SlugField(max_length=200, unique=True, null=try)
'''