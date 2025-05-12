function solution(numbers) {
    return numbers.sort((a, b) => a - b).slice(-2).reduce((acc, num) => acc * num);
}