#!/usr/bin/python3

def main() -> int:
    '''
    This function calculates affine transform
    from ellipse to basic ellipse
    Data is retrieved from user
    @return Exit code
    '''
    x0, y0, a0, b0 = map(int, input("x0 y0 a0 b0 = ").split())
    while (True):
        x, y, a, b = map(int, input("x y a b = ").split())
        print(str(a / a0) + "\t\t0\t\t" + str(x - x0 * a / a0))
        print("0\t\t" + str(b / b0) + "\t\t" + str(y - y0 * b / b0))
        print("matrix(" + str(round(a / a0, 5)) + "," + str(0) + "," + str(0) 
                + "," + str(round(b / b0, 5)) + "," + str(round(x - x0 * a / a0, 5))
                + "," + str(round(y - y0 * b / b0, 5)) + ")")
        print()
    return 0

if (__name__ == "__main__"):
    main()
