function solution(numbers) {
    return numbers.reduce((acc, number) => acc + number, 0)/numbers.length
}