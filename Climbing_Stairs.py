def climbStairs(n: int) -> int:
    first = 1
    second = 1
    for _ in range(1, n):
        temp = second
        second = first + second
        first = temp