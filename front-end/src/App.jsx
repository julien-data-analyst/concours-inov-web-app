import React from 'react';
import './css/App.css';
import Home from './pages/Home';
import Projects from './pages/Projects';
//import Dashboard from './pages/Dashboard';
//import API from './pages/API';
import {Routes, Route} from "react-router-dom"
import NavBar from './components/NavBar';

/* Routes, Route : pour créer les différentes routes
   Link : Pour créer les liens pour les routes (NavBar.jsx) */
const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <NavBar />
      </header>
      
      <main className='main-content'>
        <Routes>
          <Route path='/' element={<Home />}/>
          <Route path='/projects' element={<Projects />}/>
          
        </Routes>
      </main>
    </div>
  );
};

/* To understand the components concepts */
// function Text({display}){
//   return(
//     <>
//     <div>
//       <p>{display}</p>
//     </div>
//     <div>
//       <p>{display}</p>
//     </div>
//     </>
//   )
// }

          // <ProjectCard project={{name: "personnalisation", theme: "numeric", beginning_year: 2024, ending_year: 2026}}></ProjectCard>
          // <ProjectCard project={{name: "tim", theme: "numeric", beginning_year: 2024, ending_year: 2026}}></ProjectCard>
/*<Route path='/dashboard' element={<Dashboard />}/>
          <Route path='/api' element={<API />}/> */
export default App;