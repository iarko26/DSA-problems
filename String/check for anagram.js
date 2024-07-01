function checkanagram(s,t){
    let n=s.length,m=t.length;
    if(n!==m){
        return false;
    }
let count={};
    for(let leter of s ){
        count[leter]=(count[leter] || 0)+1;

        
    }
    
    for(let leter of t){
     if(!count[leter]){
            return false;
     }
     count[leter]--

    }
    return true;
    
  

}
checkanagram("anagram","nagaram")