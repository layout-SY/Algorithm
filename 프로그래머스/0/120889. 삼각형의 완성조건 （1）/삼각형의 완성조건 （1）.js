function solution(sides) {
    return sides.sort((a, b) => a - b) && sides[2] < sides[0] + sides[1] ? 1 : 2;
}