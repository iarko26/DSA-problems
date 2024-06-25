function printchar(str){
    str=str.split('').sort().join('');
    for(let i=0;i<str.length;i++){
        let c=1;
        while(i<str.length-1 && str[i]===str[i+1]){
            c++;
            i++;
        }
        if(c>1){
            console.log(c)
        }
    }

}

console.log(printchar("teeest carr"))