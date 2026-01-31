import ProjectCard from "../components/ProjectCard";
import "../css/Home.css";

function Home() {
    return (
        <>
        <h1> Bienvenue sur le site web du concours i-nov</h1>
        <p>
            Ce site web est à but de recherche sur les projets lauréats des différentes vagues de ce concours et d'observer les innovations par les entreprises.
            Il est composé de plusieurs onglets dont :
        </p>
            <ul>
                <li> <strong>Accueil :</strong> la page actuelle qui sert à la présentation de ce concours </li>
                <li> <strong> Projets : </strong> onglet de rechercher permettant de regarder tous les projets avec la possibilité de filtrer par plusieurs critères</li>
                <li> <strong> API : </strong> onglet permettant d'accéder à l'utilisation de l'API pour récupérer les données de la base de données</li>
                <li> <strong> Tableau de bord : </strong> onglet permettant la consultation d'un tableau de bord pour observer des indicateurs et visuels graphiques sur les concours</li>
            </ul>
        <p>
            Si vous voulez observer un peu plus en détails le contenu de ce projet, vous pouvez aller regarder le dépôt <a href="https://github.com/julien-data-analyst/concours-inov-web-app" target="_blank">github</a> à cet effet.
            Maintenant, je vais expliquer ce qu'est le concours i-nov. 
        </p>
        <h2> C'est quoi le concours i-nov ?</h2>
        <p>
            Le concours i-Nov soutient des projets d'innovation au potentiel particulièrement fort pour l'économie française portés par des start-up et des PME, afin de favoriser l'émergence d'entreprises leaders dans leur domaine et pouvant prétendre à une envergure mondiale.
            Sont concernés les projets de recherche, développement et innovation, dont les coûts totaux se situent entre 1M € et 5 M€ et d'une durée de 12 à 36 mois.
            À travers le Programme d'investissements d'avenir, il mobilise jusqu'à 80 millions d'euros par an autour de thématiques comme la révolution numérique, la transition écologique et énergétique, la santé ou la sécurité.
            À la clé, une aide financière jusqu'à 45 % du coût du projet sous forme de subventions et avances récupérables.
            i-Nov, c'est 692 lauréats depuis la création du dispositif en 2017.
        </p>
            <br />
            <p>Source : <a href="https://www.enseignementsup-recherche.gouv.fr/fr/le-concours-i-nov-49817" target="_blank">enseignementsup-recherche.gouv.fr</a></p>


        <h2> L'objectif de ce projet </h2>
        <p>
            L'objectif de ce projet était d'offrir un moyen moderne de consulter tous les projets dans un seul endroit que d'aller chercher dans 12 PDF. 
            Il y a eu bien sûr énornément de travail notamment au niveau de l'extraction, la préparation et le chargement de ces données dans la base.
            Si vous êtes intéressées comment j'ai fait cette extraction, je vous invite à consulter mon dépôt <a href="https://github.com/julien-data-analyst/concours-inov-web-app" target="_blank">github</a> concerné.
        </p>

        <h2> L'avenir de ce projet </h2>
        <p>
            Ce projet sera maintenu et versionné afin de le rendre plus efficace au fur et à mesure que j'y travaillerais dessus. 
            L'objectif étant d'avoir une maîtrise assez avancée sur mon stack Python/React/HTML/CSS/JS pour mon job de Data Analyst.
            Il y aura l'ajout de nouvelles fonctionnalités (API, IA, etc) que je travaillerais dans un cadre futur après que l'application soit
            assez mature et performant dans ses premières versions.
        </p>
        </>
    )

}

export default Home;