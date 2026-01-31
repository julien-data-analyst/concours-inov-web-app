import "../css/ProjectCard.css"

function ProjectCard({project}){
    // /assets
    const url_icon = `/${project.theme.general_theme}_icon.png`
    return <div className="project-card">
        <div className="project-poster">
            <img src={url_icon} alt={project.theme.general_theme} />
        </div>
        <div className="project-info">
            <h3>{project.name}</h3>
            <h4>{project.company.name}</h4>
            <p>Vague : {project.vague}</p>
            <p> Année de réalisation : {project.beginning_year} - {project.ending_year}</p>
            <p> Montant du projet : {project.project_amount} € / Montant de l'aide : {project.project_allowance} € </p>
        </div>
    </div>
};

export default ProjectCard;