function solution(my_string) {
return my_string.split("").filter((str) => str !== 'a' && str !== 'e' && str !== 'i' && str !== 'o' && str !== 'u').join('');
}