function solution(array) {
  const arr = array.sort((a, b) => a-b);
    return arr[Math.trunc(array.length/2)];
    
}