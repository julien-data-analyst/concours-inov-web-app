import React, { useEffect, useState } from "react";
import api from "../api.js";

const ProjectsList = () => {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchProjects = async () => {
    try {
      const response = await api.get("/projects/");
      setProjects(response.data);
    } catch (err) {
      setError("Failed to load projects");
      console.error("Axios error:", err);
      console.error("Response:", err.response);
      console.error("Message:", err.message);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProjects();
  }, []);

  if (loading) {
    return <p>Loading projects...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  if (projects.length === 0) {
    return <p>No projects found.</p>;
  }

  return (
    <div>
      <h2>Projects List</h2>
      <ul>
        {projects.map((project) => (
          <li key={project.id}>{project.name} / {project.beginning_year} - {project.ending_year}</li>
        ))}
      </ul>
    </div>
  );
};

export default ProjectsList;
