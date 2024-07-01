/**
 * @param {string} s
 * @return {string}
 */

function reverse(s, b, e) {
    while (b < e) {
        [s[b], s[e]] = [s[e], s[b]];
        b++;
        e--;
    }
}
var reverseWords = function(s) {
let words = s.trim().split(/\s+/);
let n=words.length;
reverse(words,0,n-1);
return words.join(' ');

}