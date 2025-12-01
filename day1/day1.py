def spin(input_list: list) -> tuple:
    position = 50
    zero_clicks = 0
    zero_endings = 0

    for i in input_list:
        rotation = -1 if i[0] == "L" else 1
        distance = int(i[1:])

        for _ in range(distance):
            position += rotation
            position %= 100
                
            if position == 0:
                zero_clicks += 1

        if position == 0:
            zero_endings += 1
    
    return (zero_endings, zero_clicks)

def main() -> None:

    inputs = []
    with open("input", "r") as f:
        inputs = f.readlines()

    result = spin(inputs)
    print(f"Password: {result[0]}, Clicks: {result[1]}")

if __name__ == "__main__":
    main()