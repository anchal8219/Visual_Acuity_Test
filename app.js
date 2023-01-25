function imagefun1() {
    var Image_Id = document.getElementById('getImage');
    var letter = document.getElementsByClassName('btn1').value;
    if (Image_Id.src.match("/img/img1.png")) {
        Image_Id.src = "/img/img2.png";
    }
    else {
        Image_Id.src = "/img/img1.png";
    }
}  
function img() {
  alert("You choose wrong value!!");
}


