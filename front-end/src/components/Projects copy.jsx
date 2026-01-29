import React, { useEffect, useState } from "react";
import api from "../api.js";

const ProjectsList = () => {

    const [projects, setProjects] = useState([]);

    const FetchProjects = async() => {

        try {
        const response = await api.get('/projects/');
        setProjects(response.data.projects)
        } catch (error) {
            console.error("Error fetching projects", error);
        }
    };


    useEffect(() => {
    FetchProjects();
  }, []);

  return (
    <div>
      <h2>Projects List</h2>
      <ul>
        {projects.map((project, index) => (
          <li key={project.id}>{project.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default ProjectsList