function getRanges(array) {
    var ranges = "", rstart, rend;
    for (var i = 0; i < array.length; i++) {
        rstart = array[i];
        rend = rstart;
        while (array[i + 1] - array[i] == 1) {
            rend = array[i + 1];
            i++;
        }
        if (i == array.length - 1){
            ranges += (rstart == rend ? rstart: rstart + '-' + rend);
        }
        else{
            ranges += (rstart == rend ? rstart + ', ' : rstart + '-' + rend + ", ");
        }
    }
    return ranges;
}

console.log(getRanges([1,3,5,6,7,12,13,14,15,78]))