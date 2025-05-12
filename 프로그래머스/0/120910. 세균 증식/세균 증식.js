function solution(n, t) {
    let i = 0;
    while(t !== i){
        n = n * 2;
        i++;
    }
    return n;
}