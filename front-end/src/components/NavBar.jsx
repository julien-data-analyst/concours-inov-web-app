import { Link } from "react-router-dom"
import "../css/Navbar.css"
function NavBar() {
    return <nav className="navbar navbar-expand-sm bg-light">
    
  <div className="container-fluid">
    <Link to="/">Concours i-nov</Link>
    <ul className="navbar-nav">
      <li className="nav-item">
        <Link to="/" className="nav-link"> Accueil </Link>
      </li>
      <li className="nav-item">
         <Link to="/projects" className="nav-link"> Projets </Link>
      </li>
      {/* <li className="nav-item">
        <Link to="/favs" className="nav-link"> Favoris </Link>
      </li> */}
      {/* <li className="nav-item">
        <Link to="/api" className="nav-link"> API </Link>
      </li> */}     
      <li className="nav-item">
        <Link to="/dashboard" className="nav-link"> Tableau de bord </Link>
      </li>
    </ul>
  </div>
    </nav>
}

export default NavBar;
