
document.body.style.backgroundColor = 'red';
function increaseValue(name) {
    c=parseInt(document.getElementsByClassName(name)[0].innerHTML);
    console.log(typeof(c));
    c++;
    updateCounter(name,c);
}

function decreaseValue(name) {
    c=parseInt(document.getElementsByClassName(name)[0].innerHTML);
    if (c>0){
        c--;
        updateCounter(name,c);
    }
}

function updateCounter(name,c) {
    document.getElementsByClassName(name)[0].innerHTML=c
}

