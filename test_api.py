import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. 환경변수 로드
load_dotenv()
api_key = os.getenv("NANOBANANA_API_KEY")

print(f"🔑 로드된 API 키: {api_key[:10]}... (뒤는 생략)")

if not api_key or "AIzaSyCbbvdem" in api_key:
    print("❌ [경고] API 키가 예시용(Placeholder)이거나 비어있습니다!")
    print("   -> .env 파일에 본인의 실제 Google API 키를 넣어주세요.")
    exit()

# 2. 모델 연결 테스트
genai.configure(api_key=api_key)
model_name = 'gemini-3-pro-image-preview' # 혹은 'gemini-2.0-flash'

print(f"🤖 모델 연결 테스트 중 ({model_name})...")

try:
    model = genai.GenerativeModel(model_name)
    response = model.generate_content("Hello! Are you working?")
    
    if response.text:
        print(f"✅ 성공! 모델 응답: {response.text}")
    else:
        print("⚠️ 응답은 왔지만 텍스트가 없습니다.")
        
except Exception as e:
    print(f"❌ 연결 실패! 에러 로그를 확인하세요:\n{e}")