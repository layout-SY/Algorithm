function solution(n) {
    return Number.isInteger(n/7) ? n/7 : Math.trunc(n/7 + 1 )
}