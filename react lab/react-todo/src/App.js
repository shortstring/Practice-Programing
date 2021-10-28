// import logo from './logo.svg';
// import './App.css';

import Todo from './components/Todo'
function App() {
    return (
        <div id = "container">
            <h1>My Todos</h1>
            <Todo text="Learn React"/>
            <Todo text="Master React"/>
            <Todo text="Practice React" />
        </div>
    );
}

export default App;