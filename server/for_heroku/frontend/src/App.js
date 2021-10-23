import React, { useState } from 'react';
import { render } from "react-dom";

const JsonData = ({param, setParam}) => {
  const [dataJson, setDataJson] = useState('');
  const updateCount = () => {
    setParam(param);
           fetch('https://libraryspprbackend.herokuapp.com/api/book/?user_id='+param)
           .then(response => response.json())
           .then(data => setDataJson(data));
            console.log(JSON.stringify(dataJson));

  }
  return (
      <div>
         <div>
            <label>response: {JSON.stringify(dataJson)}</label>
         </div>
          <div>
            <button type="button" onClick={updateCount}><i className="fa fa-search"></i></button>
          </div>
      </div>
)};

function App() {
   const [current_user_id, setCount] = useState(0);
    const [json_txt, setJson] = useState(0);
    const [mounted, setMounted] = useState(true);
    const [param, setParam] = useState(0);
    const toggle = () => setMounted(!mounted);

   return (
     <div>
        <p>Current user: {current_user_id} </p>
        <input type="text" placeholder="Please input user id.." id="input_id" onChange={e => setCount(e.target.value)} />
        {mounted && <JsonData param={current_user_id} setParam={setParam}/>}
      </div>
    );
  }

export default App;

const container = document.getElementById("app");
render(<App />, container);
