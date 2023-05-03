var step=1
let cookieData={}


let formValue=[ ['firstName','lastName','email','phone','adhar','religion'],
                ['currentAdd','permanentAdd','city1','state1','pincode1','country1'], 
                ['institute','address','city2','state2','pincode2','country2'],
                ['course','branch','rollNu','percentage'],['bankName','branch1','account','ifsc']
              ]

let validationFormValue=[  ["^[A-Za-z][A-Za-z_]{3,29}$"  , "^[A-Za-z][A-Za-z_]{3,29}$",
                 "[A-Za-z0-9]{1,50}@gmail.com" , "^\\d{10}$",
                  "^\\d{12}$", "^[A-Za-z][A-Za-z_]{3,29}$" 
                 ],
                 
                 [
                  "^[A-Za-z0-9][A-Za-z ]{15,49}$",
                  "^[A-Za-z0-9][A-Za-z ]{15,49}$",
                  "^[A-Za-z]",
                  "^[A-Za-z][A-Za-z_]{4,20}$",
                  "^\\d{6}$",
                  "^[A-Za-z][A-Za-z_]{4,25}$"
                 
                 ],
                 
                 [
                  "^[A-Za-z][A-Za-z ]{4,29}$",
                  "^[A-Za-z0-9][A-Za-z ]{4,29}$",
                  "^[A-Za-z]",
                  "^[A-Za-z][A-Za-z ]{4,50}$",
                  "^\\d{6}$",
                  "^[A-Za-z][A-Za-z_]{4,35}$"
                 
                 ],
                 
                 [
                  "^[A-Za-z][A-Za-z_ ]{13,40}$",
                  "^[A-Za-z][A-Za-z_ ]{14,40}$",
                  "^\\d{10}$",
                  "^100(\.0{0,2})? *%?$|^\d{1,2}(\.\d{1,2})? *%?$",
                 
                 ],
                 
                 [
                  "^[A-Za-z][A-Za-z_ ]{4,29}$",
                  "^[A-Za-z][A-Za-z_ ]{4,29}$",
                  "^[0-9]{9,18}$",
                  "^[A-Z]{4}[0-9]{7}$"
                 
                 ]
                 ]
                 
$(document).ready(function(){
  let steps=["<li id='step11' class='is-active'>Personal Information</li>", 
             "<li id='step22'>Address Information</li>"  ,
             "<li id='step33'>Institute Information</li>",
             "<li id='step44'>Applicant Details</li>",
             "<li id='step55'>Bank Information</li>"
           ] 
    
  let religion=["<option value='' selected='selected' disabled='disabled'>-- select one --</option>",
             "<option value='African Traditional &amp; Diasporic'>African Traditional &amp;Diasporic</option>",
             "<option value='Agnostic'>Agnostic</option>",
             "<option value='Atheist'>Atheist</option>",
             "<option value='Baha'i'>Baha'i</option>",
             "<option value='Buddhism'>Buddhism</option>",
             "<option value='Cao Dai'>Cao Dai</option>",
             "<option value='Chinese traditional religion'>Chinese traditional religion</option>",
             "<option value='Christianity'>Christianity</option>",
             "<option value='Hinduism'>Hinduism</option>",
             "<option value='Islam'>Islam</option>",
             "<option value='Jainism'>Jainism</option>",
             "<option value='Juche'>Juche</option>",
             "<option value='Judaism'>Judaism</option>",
             "<option value='Neo-Paganism'>Neo-Paganism</option>",
             "<option value='Nonreligious'>Nonreligious</option>",
             "<option value='Rastafarianism'>Rastafarianism</option>",
             "<option value='Secular'>Secular</option>",
             "<option value='Shinto'>Shinto</option>",
             "<option value='Sikhism'>Sikhism</option>",
             "<option value='Spiritism'>Spiritism</option>",
             "<option value='Tenrikyo'>Tenrikyo</option>",
             "<option value='Unitarian-Universalism'>Unitarian-Universalism</option>",
             "<option value='Zoroastrianism'>Zoroastrianism</option>",
             "<option value='primal-indigenous'>primal-indigenous</option>",
             "<option value='Other'>Other</option>"
            ]

  for(let i=0;i<steps.length;i++){
    $(".multi-steps").append(steps[i])
  }
  
  for(let i=0;i<religion.length;i++){
    
    $("#browser1").append(religion[i])

  }

})

function personalInfoPage(){
    step="#step"+step
    $(step).show()

    step=1
    $("#next"+step).attr('disabled',true)
}
personalInfoPage()

function cookieSet(){
  for(let i=0;i<Object.keys(cookieData).length;i++){
    let preview=["#personalInfo","#addressInfo","#instituteInfo","#applicantInfo","#accountInfo"]
    
    let key=Object.keys(cookieData)[i]
    let   value= JSON.stringify(cookieData[ Object.keys(cookieData)[i]]) 
    document.cookie = key+ "=" + value + ";" + 1+ ";path=/";
     $(preview[step-1]).append("<b class='text-success'>"+key+"</b>"+"     =>        "+"<span class='text-dark'>"+JSON.parse(getCookie(key))+"</span>"+"<br>");
   }
}

function nextButton(e){
  e.preventDefault();
  if(e.pointerId==-1) {
    return false
  }

    cookieSet()

    cookieData={}
    let temp=step
    if(step<=4){
    temp="#step"+temp
    $(temp).hide()
    $(temp+step).removeClass("is-active");
    temp=""
    step=step+1
    temp="#step"+(step)
    $(temp).show()
    $(temp+step).addClass("is-active");
    debugger
    $("#next"+step).attr('disabled',true)
}
}

function previousButton(e){
    e.preventDefault();
    let temp=step
    temp="#step"+temp
    $(temp+step).removeClass("is-active");
    $(temp).hide()
    temp="#step"
    step=step-1
    temp=temp+(step)
    $(temp+step).addClass("is-active");
    $(temp).show()
}


function validation(){

 for(let i=0;i<formValue[step-1].length;i++){

 
    let search=formValue[step-1][i];
    $("input[name='"+search+"']").css("background-color", "white")
    let x = document.forms["formData"][search].value;
 
    if (x == "") {
      $("input[name='"+search+"']").css("background-color", "#ffefd5")
      debugger
      $(""+search+"").text("<label style='color:red'>Enter Valid Name</label>")
      $("#next"+step).attr('disabled',true)
      return false
    }
    else{
    let compare=new RegExp(validationFormValue[step-1][i])

     if(!compare.test(x)){
      $("input[name='"+search+"']").css("background-color", "#ffefd5")
      $("input[name='"+search+"']").text("<label style='color:red'>Enter Valid Name</label>")
      $("#next"+step).attr('disabled',true)
      return false
     }
     else{
      console.log(search)
      cookieData[search]=x
     }
   
    }
  
  }
  $("#next"+step).attr('disabled',false)


}


function preview(e){
  e.preventDefault();
  if(step==5){
  cookieSet()
  $("#step"+step).hide()
  $(".multi-steps").hide()
  $('#preview').show()
  step=4;
  }
  else
  {
    step=5
    $("#step"+step).show()
    $(".multi-steps").show()
    $('#preview').hide()

  }

}


function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}


async function loadNames() {
  const response = await fetch('state.json');
  const data = await response.json();
  for(let i=0;i<data.states.length;i++){
    $("#state").append("<option>"+data.states[i].state+"</option>")
   let city=data.states[i].cities.length;
   
   for(let j=0;j<city;j++){
    $("#city").append("<option>"+data.states[i].cities[j]+"</option>")
  }
}
}

loadNames()