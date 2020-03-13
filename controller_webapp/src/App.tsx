import React, { useRef } from 'react'
import { connect } from 'mqtt'
import './App.css';

function App() {
  const client = useRef(connect("ws://gx1:9001"));
  client.current.on("connect", () => {
    client.current.subscribe('scanner', function (err) {
      if (!err) {
        client.current.publish('scanner', 'Hello mqtt test', { qos: 2 })
      } else {
        console.log(err);
      }
    })
  });
  client.current.on("message", (topic, message) => {
    console.log(message.toString());
  });
  return (
    <>
      <div>Auslösen:</div>
      <button style={{ width: "200px", height: "200px" }} onClick={function () {
        client.current.publish("scanner", "shoot", { qos: 2 });
      }
      }>shoot</button>
      <p></p>
      <button style={{ width: "200px", height: "200px" }} onClick={function () {
        client.current.publish("scanner", "copy", { qos: 2 });
      }
      }>copy</button>
    </>
  );
}

export default App;
