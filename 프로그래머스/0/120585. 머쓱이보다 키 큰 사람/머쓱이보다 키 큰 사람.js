function solution(array, height) {
  return array.reduce((acc, num) => (num > height) ? ++acc : 0, 0);
}