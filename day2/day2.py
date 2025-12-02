def get_inputs(path: str) -> list:
    with open(path, "r") as f:
        return [x.strip() for x in f.read().split(',')]

def check_range(range_input: str) -> list:
    start = int(range_input.split('-')[0])
    end = int(range_input.split('-')[1])

    invalids = [x for x in range(start, end+1) if is_repeating_2(str(x))]
    return invalids

        
def is_repeating_2(s: str) -> bool:
    s_len = len(s)

    for i in range(1, s_len // 2 + 1): 
        if s_len % i == 0: 
            substring = s[:i]
            if substring * (s_len // i) == s:
                return True 
    return False


def is_repeating(s: str) -> bool:
    s_len = len(s)

    if s_len % 2 != 0:
        return False

    h = s_len // 2
    if s[:h] == s[h:]:
        return True

    return False


def main() -> None:
    inputs = get_inputs("./input.txt")
    invalids = []
    for x in inputs:
        invalids.extend(check_range(x))
    print(invalids)
    print(sum(invalids))

if __name__ == '__main__':
    main()
