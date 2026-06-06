class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if (strs.length===0) return '';
        let res=[];
        for (let s of strs){
            res.push(s.length+',')
        }
        res.push('#',...strs);
        console.log(res)
        return res.join('')
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if(str.length===0) return [];
        let sizes=[];
        let res=[];
        let i=0;
        while(str[i]!='#'){
            let j=i;
            while(str[j]!==','){
                j++;
            }
            sizes.push(parseInt(str.substring(i,j),10));
            i=j+1;
        }
        i++;
        console.log(str[i])
        for(let sz of sizes){
            res.push(str.slice(i,sz+i))
            i+=sz;
        }
        console.log(res)
        return res
    }
}
