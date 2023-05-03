var time=60;
function spin() {
    if(time==60)
    currentTime()
    var x = 1024; //min value
    var y = 9999; //max value
    var deg = Math.floor(Math.random() * (x - y)) + y;
    e= document.getElementById('wheel').style.transform = "rotate("+deg+"deg)";
    console.log(e)
    document.getElementById('sp').disabled=true;
    
    setTimeout(()=> {
    show(deg)
    },3000)
}

function show(a){
    let i=["First Name","Email","Designation","Organization","Try Again","Message","Last Name","Try Again"]
    for(let it=ie; i<(i.length);i++){
        document
    } 

   
    const random = Math.floor(Math.random() * a);
     console.log(random, i[random]);
    if(i[random]!="Try Again"){
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
    document.getElementById('submit').disabled=true;
    }
     
  }

  