import React from 'react';
import './App.css';
import ProjectsList from './components/Projects';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Project Management App</h1>
      </header>
      <main>
        <ProjectsList />
      </main>
    </div>
  );
};

export default App;