import sys

def testare(n):
    x = 0
    for i in range(n+1):
        x += i
    print(x)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Utilizare: python search_images.py variabila n")
        sys.exit(1)

    n = sys.argv[1]
    n = int(n)
    testare(n)