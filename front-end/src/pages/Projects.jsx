import ProjectCard from "../components/ProjectCard";
import { useEffect, useState } from "react";
import {fetchProjects} from "../service/api";
import "../css/Home.css"
function Home() {

    // create a usestate to make the research constant
    const [searchQuery, setSearchQuery] = useState("");
    const [projects, setProjects] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    // create a useeffect to make the API call once
     useEffect(() => {
        const loadProjects = async() => {
            try {
                const  projects_details = await fetchProjects() // Appel à l'API en asynchrone
                setProjects(projects_details) // On le mets dans notre constante projects d'usestate
            }catch(error){
                console.error("Error fetching projects : ", error);
                setError("Failed to load projects...")
            }finally{
                setLoading(false);
        }
           
        }
        loadProjects();
     }, [])


    // C'est ici que tu vas gérer le submit
    const handleSearch = (e) => {
        e.preventDefault(); // Eviter qui recharge la page
        alert(searchQuery);
    };

    /* Pour le forms : ajouter des filtrages plus élaborées */
    return (
    <div className="home">
        <form onSubmit={handleSearch} className="search-form">
            <input
                type="text"
                placeholder="Search for projects..."
                className="search-input" 
                value={searchQuery} // To get the research value
                onChange={(e) => setSearchQuery(e.target.value)} // target représente le input
            />
            <button type="submit"> Search </button>
        </form>

        <div className="project-grid">
            {projects.map(
                (project) => 
                project.name.startsWith(searchQuery) && 
                    (<ProjectCard project={project} key={project.id}></ProjectCard>) // Condition to get the search results
            )}
        </div>
    </div>)

}

export default Home;