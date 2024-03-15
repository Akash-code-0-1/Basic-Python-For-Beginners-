if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max_score = -101
    runner_up = -101  
    for score in arr:
        if score > max_score:
            runner_up = max_score
            max_score = score
        elif score > runner_up and score < max_score:
            runner_up = score
    print(runner_up)