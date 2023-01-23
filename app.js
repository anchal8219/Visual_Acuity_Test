function imagefun1() {
    var Image_Id = document.getElementById('getImage');
    var letter = document.getElementsByClassName('btn1').value;
    if (Image_Id.src.match("img1.png")) {
        Image_Id.src = "img2.png";
    }
    else {
        Image_Id.src = "img1.png";
    }
}  
function img() {
  alert("You choose wrong value!!");
}


