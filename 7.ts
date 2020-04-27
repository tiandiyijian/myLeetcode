let reverse: (x:number) => number = function(x:number): number {
    let flag = 1;
    if (x < 0) {
        flag = -1;
        x = -x;
    }
    let ans: number = 0, tmp: number = 0;
    while (x) {
        tmp = x % 10;
        x = Math.floor(x/10);
        ans = ans * 10 + tmp;    
    }
    return ans * flag;
}

console.log(reverse(-123));