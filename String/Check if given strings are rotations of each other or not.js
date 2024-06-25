function checkrotate(s1,s2){
    if(s1.length===s2.length && s1.length>0){
        let temp=s1+s2;
        return temp.includes(s2)
        
    
    }
    return false
}
console.log(checkrotate("AACD","AACD"))