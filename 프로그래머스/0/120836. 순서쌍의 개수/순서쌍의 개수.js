function solution(n) {
    let i = 1;
    let answer = 0;
    while(n !== i){
        if(n % i === 0) {
            answer++;
        }
        i++;
    }
    return answer+1;
}