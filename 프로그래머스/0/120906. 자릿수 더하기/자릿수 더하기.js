function solution(n) {
    return [...(n.toString())].map((str) => Number(str)).reduce((acc, num) => acc + num);
}