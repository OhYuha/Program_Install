프로그램이름 = "프로그램이름"
exename = "exe이름"
import os
import sys
import shutil
import time
import os
import win32com.client

def create_desktop_shortcut(target_path, shortcut_name):
    """
    바탕화면에 바로가기를 생성하는 함수
    :param target_path: 원본 파일의 절대 경로
    :param shortcut_name: 생성될 바로가기 파일의 이름 (확장자 .lnk 제외)
    """
    
    # 1. 현재 사용자의 바탕화면 경로를 자동으로 가져오기
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # 한국어 윈도우 환경에서 'Desktop' 폴더가 '바탕 화면'으로 매핑되어 있어도 
    # 내부 시스템 경로는 'Desktop'으로 처리되므로 위 코드가 정상 작동합니다.
    shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")

    try:
        # 2. WScript.Shell 객체를 통해 윈도우 쉘 기능 호출
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)

        # 3. 바로가기 속성 설정
        shortcut.TargetPath = target_path  # 연결할 원본 파일의 경로
        shortcut.WorkingDirectory = os.path.dirname(target_path)  # 시작 위치 (원본 파일이 있는 폴더)
        
        # (선택) 아이콘을 특정 이미지나 실행 파일의 아이콘으로 지정하고 싶다면 아래 주석을 해제하세요.
        # shortcut.IconLocation = target_path 

        # 4. 바로가기 파일 저장
        shortcut.save()
        
    except Exception as e:
        pass
def md(path):
    if not os.path.exists(path):
        os.makedirs(path)

def rp(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
### 아래 주석을 풀어 사용권 계약 관련 코드를 쓰세요
# print("""이 프로그램을 설치하신다면 아래의 사용권 계약에 뭐 어쩌고저쩌고하는것을 동의합니다
# 제 1항
# 뭐 어쩌꼬쩌쩌꼬""")
sore = str(rp("data"))
t1 = input("설치 폴더 입력(기본은 엔터)")
if t1 == "":
    t = f"C:/Program Files/{프로그램이름}"
else:
    t = t1
shutil.copytree(sore, t, dirs_exist_ok=True)
qkxkd = input("바탕화면에 바로가기를 만드시겠습니까?")
if qkxkd == "":
    create_desktop_shortcut(f"{t}/{exename}", 프로그램이름)
else:
    pass
print("완료. 5초 후 종료")
time.sleep(5)
exit()
