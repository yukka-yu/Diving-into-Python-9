import csv
import json
import random
from typing import Callable

N = 101 # csv strings amount
csv_path = 'csv_coefficients.csv'
json_path = 'json_roots.json'


def csv_to_three_coeffs(path: str = csv_path):
    def deco(func: Callable):
        result = []
        def wrapper(*args, **kwargs):
            with open (path, 'r', encoding='utf-8') as c:
                csv_read = csv.reader(c, dialect='excel', delimiter=' ')  
                for line in csv_read:
                    coef_list = list(map(int, line))
                    result.append(f'Square equation with coeffs: {line} has roots:')
                    result.append(func(coef_list[0], coef_list[1], coef_list[2]))
            return result
        return wrapper
    return deco


def coeffs_and_roots_to_json(path:str = json_path):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            with open(path, 'a', encoding='utf-8') as j:
                res = func(*args, **kwargs)
                json.dump(res, j, separators=('\n', ':'))
            return None
        return wrapper
    return deco

                       
@coeffs_and_roots_to_json()
@csv_to_three_coeffs()
def square_equation_roots(a: int, b: int, c: int) -> list[float] | float | str:
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = -(b + discriminant ** 0.5) / 2 * a
        x2 = -(b - discriminant ** 0.5) / 2 * a
        return [x1, x2]
    elif discriminant == 0:
        return -b / 2 * a
    else:
        return 'There is no real roots for this equation'
    

def csv_generator(path: str) -> None:
    with open(path, 'w', encoding='utf-8') as c:
        csv_write = csv.writer(c, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for _ in range(N):
            line = []
            for i in range(3):
                line.append(random.randint(1, 100))
            csv_write.writerow(line)



if __name__ == '__main__':
    square_equation_roots()

