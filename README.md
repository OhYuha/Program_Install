# Program_Install
파이썬 기반의 프로그램 설치 프로그램

---

프로그램 인스툴은 파이썬 기반의 설치 프로그램입니다. 개발자라면 아래의 사항을 따라 프로그램 설치 프로그램을 만드시길 바랍니다.

먼저 프로그램 인스툴을 설치하기 위해

* pyinstaller (`pip install pyinstaller`)
* Python
* 설치될 프로그램의 exe파일과 폴더 및 프로그램의 이름

## 설치

1. dev 브렌치의 파일들을 다운로드합니다.
2. `main.py`의 1, 2 번 라인에 있는 변수를 프로그램의 맞게 수정합니다.
3. `main.py`와 `data`가 포함된 폴더에서 cmd를 열고 `pyinstaller --onefile --uac-admin --icon="icon.ico" --add-data "data;data" --hidden-import win32com --hidden-import win32timezone main.py`를 실행합니다.


이 프로그램은 BSD-3 라이센스로 배포됩니다.
dev 브렌치는 README.md와 라이센스 등 개발의 필요없는 파일을 제거한 것이며 main 브렌치와 같은 라이센스를 적용합니다 
