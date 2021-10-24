import React, { useState } from 'react';
import { render } from "react-dom";

const JsonData = ({param, setParam}) => {

  const [dataJson, setDataJson] = useState('');
  const [recomendations, setRecomend] = useState('');
  const [history, setHistory] = useState('');
  const updateCount = () => {
    setParam(param);
           fetch('https://libraryspprbackend.herokuapp.com/api/book/?user_id='+param)
           .then(response => response.json())
           .then(data => setDataJson(data));
            console.log(JSON.stringify(dataJson));
            setHistory(dataJson.history)
  }
  return (
      <div>
          <div>

            <i onClick={updateCount} style={{marginRight: "auto"}} ><i className="bi bi-search btn btn-primary col-1" style={{marginTop: 10 + 'px', marginRight: "auto"}}></i></i>

          </div>
          <label class="fs-4"  style={{marginTop: 10 + 'px'}}>Рекомендации по пользователю с ID {param}:</label>
          <div>
            <table class="table table-striped">
              <thead>
                <tr>
                  <th scope="col">ID</th>
                  <th scope="col">Название книги</th>
                  <th scope="col">Автор</th>
                </tr>
              </thead>
              <tbody>

              {dataJson?.recomendations?.map(book => {
                    return (
                      <tr>
                        <td> {book.id} </td>
                        <td> {book.title}</td>
                        <td> {book.author}</td>

                      </tr>
                    );
                  })}
              </tbody>
            </table>
          </div>
        <div class="b-example-divider"></div>
        <label class="fs-4"  style={{marginTop: 20 +'px', marginBottom: 20 +'px'}}>История пользователя:</label>
    <div>
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Название книги</th>
            <th scope="col">Автор</th>
          </tr>
        </thead>
        <tbody>

        {dataJson?.history?.map(book => {
              return (
                <tr>
                  <td> {book.id} </td>
                  <td> {book.title}</td>
                  <td> {book.author}</td>

                </tr>
              );
            })}
        </tbody>
      </table>
    </div>
      </div>
)};

function App() {
   const [current_user_id, setCurrentUser] = useState(0);
    const [json_txt, setJson] = useState(0);
    const [mounted, setMounted] = useState(true);
    const [param, setParam] = useState(0);
    const toggle = () => setMounted(!mounted);

   return (
     <div>
       <div>
       <input type="search" class="form-control" placeholder="Введите идентификатор пользователя..." aria-label="Search" id="input_id" onChange={e => setCurrentUser(e.target.value)}/>
        {mounted && <JsonData param={current_user_id} setParam={setParam}/>}
       </div>



      </div>
    );
  }

export default App;

const container = document.getElementById("app");
render(<App />, container);
