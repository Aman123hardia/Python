var time=60;
function spin() {
    var x = 1024; //min value
    var y = 9999; //max value
    var deg = Math.floor(Math.random() * (x - y)) + y;
    document.getElementById('wheel').style.transform = "rotate("+deg+"deg)";
   
    setTimeout(()=> {
    show()
    },5000)
}

function show(){

    let i=["First Name","Last Name","Email","Contact","Address","Try Again","Organization","Message","Try Again"]
    const random = Math.floor(Math.random() * i.length);
     console.log(random, i[random]);
    if(i[random]!="Try Again"){

    alert(" Congratulation "+i[random]+" Field is Enabled")
    document.getElementById(i[random]).setAttribute("disabled", false);
    }
    else
    alert(" Spin Again ")


}


function currentTime() {
    let time1 =time--;
    if(time1>0){
       console.log(time1)
       document.getElementById('time').innerHTML= "Time :"+time1+" seconds " 
    let t = setTimeout(function(){ currentTime() }, 1000);
    }
    else
    document.getElementById('spin').innerHTML= "Time :"+time1+" seconds "
     
  }

currentTime()