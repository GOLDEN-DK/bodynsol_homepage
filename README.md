# 바디앤솔 홈페이지

바디앤솔 센터 및 아카데미의 공식 웹사이트 프로젝트입니다.

## 프로젝트 구조

```
bodynsol-homepage/
├── frontend/                # Next.js 프론트엔드
│   ├── public/              # 정적 파일 (이미지, 폰트 등)
│   ├── src/                 # 소스 코드
│   │   ├── app/             # Next.js App Router
│   │   ├── components/      # 리액트 컴포넌트
│   │   ├── lib/             # 유틸리티 함수, API 클라이언트 등
│   │   └── styles/          # 글로벌 스타일
│   └── ...                  # 기타 설정 파일
│
├── backend/                 # Django 백엔드
│   ├── config/              # 프로젝트 설정
│   ├── core/                # 메인 앱
│   ├── venv/                # 가상 환경 (git에 포함하지 않음)
│   └── ...                  # 기타 설정 파일
│
└── ...                      # 루트 설정 파일
```

## 기술 스택

### 프론트엔드
- Next.js (React)
- TypeScript
- Tailwind CSS

### 백엔드
- Django
- Django REST Framework
- PostgreSQL (Neon)

## 개발 환경 설정

### 프론트엔드

```bash
# 의존성 설치
cd frontend
npm install

# 개발 서버 실행
npm run dev
```

### 백엔드

```bash
# 가상 환경 활성화
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env  # 필요에 따라 .env 파일 수정

# 데이터베이스 마이그레이션
python manage.py migrate

# 개발 서버 실행
python manage.py runserver
```

## 배포

### 프론트엔드
- Vercel을 통한 배포

### 백엔드
- Heroku, AWS, 또는 Vercel Functions 등을 통한 배포

## 관리자 모드

관리자 모드에서는 다음과 같은 콘텐츠를 관리할 수 있습니다:
- 히어로 배너
- 교육 과정 카테고리 및 과정
- 수강생 후기
- 이벤트/프로모션
- 상담/문의 관리

```bash
# 관리자 계정 생성
python manage.py createsuperuser

# 관리자 페이지 접속
# http://localhost:8000/admin/
``` 