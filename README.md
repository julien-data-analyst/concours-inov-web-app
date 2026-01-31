# concours-inov-web-app

This is the repository for the web app on the Inov Competition created by the french governement which we can find multiple projects. The problem is all the project presentation is in PDFs which make the search quite difficult. This web app is here to solve the problem with a PostGreSQL Database which contains the data concerning these differents projects.

The stack that is used is :
- Python : FastAPI for the backend, SQLAlchemy for communicate with the PostGreSQL
- HTML, CSS, JS : base stack to develop web pages with library like Bootstrap or Chart.js
- React : for the front-end to create web pages (framework : vite)

The app will be composed of five pages :
- Home : present what is the goal of this competition
- Projects : present all the projects that was made this far from all competitions with possibility to filter by many modalities
- Project/{id_proj} : present the project selected from the user in the Projects/Favourites pages 
- Favourites : the one that you put into favourites
- Dashboard : will represent graphics visualization and metrics to analyze these competitions
- API : to use the API to get the Data from the Database (FastAPI docs and more)

if you want to run it for yourself, it's still being made so you gotta wait for that.
