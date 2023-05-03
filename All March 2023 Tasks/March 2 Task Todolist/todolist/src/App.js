import TaskData from './components/TaskData';
import { useState } from 'react';
import './App.css';


function App() {
  const [todoData,setTodoData]=useState(TaskData);
  const level=[{level:"low",priority:1},{level:"Medium",priority:2},{level:"High",priority:3}];
  const [taskName,setTasKName] = useState("");
  const [levelName,setLevelName] = useState(1);
  const [disable,setDisable]=useState("true");
  const [Active,setActive]=useState("true");
  const [Deactive,setDeactive]=useState("false");    
  
  const AddTask=()=>{
  alert(taskName);
  const obj=[{name:taskName,level:levelName,status:"Active",Date:'3/03/2023'}];
  const data=[...todoData,...obj];
  setTodoData(data);
 }
 
const setData=(e)=>{
   const le=e.currentTarget.value;
setLevelName(le=="High"?3:le=="Medium"?2:1);

}

const DeleteTask=(e)=>{
  const arr= [...todoData];
 console.log(e);

    arr=arr.splice(e, 1);
    setTodoData({todoData: arr});
  

  console.log(e);

}
return (
      <div class="container">
        <h1><div className='font-weight-bold text-center'>TodoList</div></h1>
        <div>
     <div className="col-md-4 ml-3 "  style={{marginTop:'2vh'}}>
      <input type="text" class="form-control"  onChange={(e)=>{setTasKName(e.currentTarget.value); const di=e.currentTarget.value==""?true:false; setDisable(di)}} placeholder='Enter Task Name'/>
     </div>
     <div className="col-md-4 ml-3"  style={{marginTop:'2vh'}}>
      <select className="form-control"  onClick={(e)=>setData(e)} >
        {level.map(data=><option>{data.level}</option>)}
    </select> 
    </div>
       <div className="col-md-4" style={{marginTop:'2vh'}}>
       <button type="button" class="btn btn-success" disabled={disable} onClick={AddTask}>Add Task</button>
    </div>
    </div>
    <div className="col-md-2" style={{marginTop:'2vh',marginBottom:'2vh'}}>
       <button type="button" class="btn btn-success"  onClick={AddTask}>Add Task</button>
    </div>
    <div className="col-md-2" style={{marginTop:'2vh',marginBottom:'2vh'}}>
       <button type="button" class="btn btn-success" disabled='false' onClick={AddTask}>Add Task</button>
    </div>
   <table class="table table-striped pd-'40px'">
    <thead>
      <tr>
        <th>S.No</th>
        <th>Task</th>
        <th>Level</th>
        <th>Status</th>
        <th>Date</th>
        <th>Edit</th>
        <th>Remove</th>
      </tr>
    </thead>
    <tbody>
    {todoData.sort((a,b)=>a.level-b.level).map((data,index)=>{
        const myobj={background:data.level===1 ? "lightYellow" : data.level===2 ? "lightgreen" : "orange"};
         return  <tr style={myobj}>
           <td>{index+1}</td>
          <td>{data.name}</td>
          <td>{level.map(res=>res.priority==data.level?res.level:"")}</td>
          <td>{data.status}</td>
          <td>{data.Date}</td>
          <td><button type="button" class="btn btn-info" >Edit Task</button></td>
          <td><button type="button" class="btn btn-danger" onClick={()=>DeleteTask({data})}>Delete  Task</button></td>

        </tr>
        })}

    </tbody>
  </table>
    </div>
  );
}

export default App;
