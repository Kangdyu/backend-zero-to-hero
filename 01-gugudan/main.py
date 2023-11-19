class Gugudan:
    def __init__(self, dan: int):
        self.dan = dan
    
    def print(self):
        for i in range(1, 10):
            print(f"{self.dan} * {i} = {self.dan * i}")


def main():
    print("Hello World!")

    while True:
        try:
            dan = int(input("출력할 구구단 입력: "))
            gugudan = Gugudan(dan)
            gugudan.print()
        except ValueError:
            print("입력하신 값이 숫자인지 확인해주세요.")


if __name__ == "__main__":
    main()