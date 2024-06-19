def validate_id(id_number):
    id_map = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17,
              'I':34, 'J':18, 'K':19, 'L':20, 'M':21, 'N':22, 'O':35, 'P':23,
              'Q':24, 'R':25, 'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30,
              'Y':31, 'Z':33}
    first_char = id_number[0]
    if first_char not in id_map:
        return "fake"
    num = id_map[first_char]
    total_sum = (num//10) + (num%10)*9
    weights = [8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(1, 9):
        total_sum += int(id_number[i]) * weights[i-1]
    total_sum += int(id_number[9])
    if total_sum % 10 == 0:
        return "real"
    else:
        return "fake"
def main():
    id_number = input().strip()
    result = validate_id(id_number)
    print(result)
if __name__ == "__main__":
    main()
