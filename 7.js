var reverse = function (x) {
    var flag = 1;
    if (x < 0) {
        flag = -1;
        x = -x;
    }
    var ans = 0, tmp = 0;
    while (x) {
        tmp = x % 10;
        x = Math.floor(x / 10);
        ans = ans * 10 + tmp;
    }
    return ans * flag;
};
console.log(reverse(-123));
