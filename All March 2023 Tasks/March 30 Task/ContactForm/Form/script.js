var time=60;
function spin() {
    if(time==60)
    currentTime()
    var x = 1024; //min value
    var y = 9999; //max value
    var deg = Math.floor(Math.random() * (x - y)) + y;
    document.getElementById('wheel').style.transform = "rotate("+deg+"deg)";
    document.getElementById('sp').disabled=true;
    
    setTimeout(()=> {
    show()
    },3000)
}

function show(){

    let i=["First Name","Last Name","Email","Designation","Try Again","Organization","Message","Try Again"]
    const random = Math.floor(Math.random() * i.length);
     console.log(random, i[random]);
    if(i[random]!="S Again"){
    document.getElementById(i[random]).disabled=false;
    alert(" Congratulation "+i[random]+" Field is Enabled")
    document.getElementById('sp').disabled=false;
    }
    else{
    alert(" Spin Again ")
    document.getElementById('sp').disabled=false;
    }

}


function currentTime() {
    let time1 =time--;
    if(time1>=0){
       console.log(time1)
       document.getElementById('time').innerHTML= "Time :"+time1+" seconds " 
    let t = setTimeout(function(){ currentTime() }, 1000);
    }
    else{
    alert("Time Over")
    document.getElementById('spin').innerHTML= "Time :"+time1+" seconds "
    document.getElementById('sp').disabled=true;

    }
     
  }

  