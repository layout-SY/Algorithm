function solution(my_string, n) {
return [...my_string].map((num) => num.repeat(n)).join("")
}