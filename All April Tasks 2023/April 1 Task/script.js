
var padding = {top:20, right:40, bottom:0, left:0},
    w = 500 - padding.left - padding.right,
    h = 500 - padding.top  - padding.bottom,
    r = Math.min(w, h)/2,
    rotation = 0,
    oldrotation = 0,
    picked = 100000,
    oldpick = [],
    color = d3.scale.category20();
 
var time=0;
pr=1;
var data = [
            {"label":"First Name",  "value":1,  "question":"Congratulation First Name Field is Enabled"},
            {"label":"Try Again",  "value":1,  "question":"Spin Again"}, // padding
            {"label":"Last Name",  "value":1,  "question":"Congratulation Last Name Field is Enabled"},
            {"label":"Try Again",  "value":1,  "question":"Spin Again"}, //font-family
            {"label":"Email",  "value":1,  "question":"Congratulation Email Field is Enabled?"}, //color
            {"label":"Try Again",  "value":1,  "question":"Spin Again"}, 
            {"label":"Organization",  "value":1,  "question":"Congratulation Organization Field is Enabled?"}, //font-weight
            {"label":"Designation",  "value":1,  "question":"Congratulation Designation Field is Enabled"}, //font-size
            {"label":"Message",  "value":1,  "question":"Congratulation Message Field is Enabled"}, //background-color             
];


var svg = d3.select('#chart')
    .append("svg")
    .data([data])
    .attr("width",  w + padding.left + padding.right)
    .attr("height", h + padding.top + padding.bottom);


var container = svg.append("g")
    .attr("class", "chartholder")
    .attr("transform", "translate(" + (w/2 + padding.left) + "," + (h/2 + padding.top) + ")");


var vis = container
    .append("g");
   
    
var pie = d3.layout.pie().sort(null).value(function(d){return 1;});


var arc = d3.svg.arc().outerRadius(r);

var arcs = vis.selectAll("g.slice")
    .data(pie)
    .enter()
    .append("g")
    .attr("class", "slice");
    

arcs.append("path")
    .attr("fill", function(d, i){ return color(i); })
    .attr("d", function (d) { return arc(d); });


arcs.append("text").attr("transform", function(d){
        d.innerRadius = 0;
        d.outerRadius = r;
        d.angle = (d.startAngle + d.endAngle)/2;
        return "rotate(" + (d.angle * 180 / Math.PI - 90) + ")translate(" + (d.outerRadius -10) +")";
    })
    .attr("text-anchor", "end")
    .text( function(d, i) {
        return data[i].label;
    });


    container.on("click", spin);

function spin(d){
    if(time==0)
    currentTime()
    //all slices have been seen, all done

    if(oldpick.length == data.length||time==30){
        console.log("done");
        container.on("click", null);
        alert("Time Over")
        return;
    }

    var  ps       = 360/data.length,
         pieslice = Math.round(1440/data.length),
         rng      = Math.floor((Math.random() * 1440) + 360);

    let rotationTime = 0;
    if(document.getElementById("vol-control").value <= 20){
             rotationTime = -600;
         }else if(document.getElementById("vol-control").value <= 40){
             rotationTime = -300;
         }if(document.getElementById("vol-control").value <= 60){
             rotationTime = -155;
         }if(document.getElementById("vol-control").value <= 80){
             rotationTime = -75;
         }else{
             rotationTime = 0;
         }
        
    rotation = (Math.round(rng / ps) * ps)-rotationTime;



    
    picked = Math.round(data.length - (rotation % 360)/ps);
    picked = picked >= data.length ? (picked % data.length) : picked;


    if(oldpick.indexOf(picked) !== -1){
        d3.select(this).call(spin);
        return;
    } else {
        oldpick.push(picked);
    }

    rotation += 90 - Math.round(ps/2);

    vis.transition()
 
        .duration(2000)
             
        .attrTween("transform", rotTween)
        .each("end", function(){
            //mark question as seen
            // d3.select(".slice:nth-child(" + (picked + 1) + ") path")
            //     .attr("fill", "white");
            show(data[picked].question)
            alert(data[picked].question)
            //populate question
            oldrotation = rotation;
    
        });
}

//make arrow
svg.append("g")
    .attr("transform", "translate(" + (w + padding.left + padding.right) + "," + ((h/2)+padding.top) + ")")
    .append("path")
    .attr("d", "M-" + (r*.15) + ",0L0," + (r*.05) + "L0,-" + (r*.05) + "Z")
    .style({"fill":"black"});

//draw spin circle
container.append("circle")
    .attr("cx", 0)
    .attr("cy", 0)
    .attr("r", 60)
    .style({"fill":"white","cursor":"pointer"});

//spin text
container.append("text")
    .attr("x", 0)
    .attr("y", 15)
    .attr("text-anchor", "middle")
    .text("SPIN")
    .style({"font-weight":"bold", "font-size":"30px"});


function rotTween(to) {
  var i = d3.interpolate(oldrotation % 360, rotation);
  return function(t) {
    return "rotate(" + i(t) + ")";
  };
}


function currentTime() {
    
    let time1 =time++;
   
    if(time1<=30){
       document.getElementById('time').style.width = 3*pr+"%";  
       document.getElementById('time').innerHTML= "Time :"+time1+" seconds " 
       pr++;
    let t = setTimeout(function(){ currentTime() }, 1000);
    }
    else{
    alert("Time Over")
    

    }
     
  }

  function show(d){
    let i=["First","Last","Email","Designation","Organization","Message"]
  for(let ch=0;ch<i.length;ch++){
    if(d.includes(i[ch])){
      
         document.getElementById(i[ch]).disabled=false;
         break;
    }
  }

}


function thisVolume()
{  
  spin(data)
        
}







