function solution(n) {
    let i = 1;
    let result = 0;
    while (i<n+1) {
        if(i%2 === 0){
            result += i;
        }
        i++;
    }
    return result
    
}