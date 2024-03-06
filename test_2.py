def eh_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

def main():
    try:
        import random

        for _ in range (10):
            number_input = random.randint(1, 100)
            if eh_fibonacci(number_input):
                print(f" {number_input} pertence a sequência de Fibonacci")
            else:
                print(f" {number_input} não pertence a sequência de Fibonacci")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
        



