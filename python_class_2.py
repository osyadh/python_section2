import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")

f = SelfTest() # 인스턴스 생성해서
print(id(f)) #4399854032

f.function2() # self매개변수 통해 메소드 실행. print(id(self))도 print(id(f))와 같은 값(4399854032) 나옴.

SelfTest.function1() # 클래스 직접 실행. self매개변수 없어야함.
