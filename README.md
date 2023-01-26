# Machine Translation Application with mBART50

## Folder structure:

    /machine-translation-application
    ├── /backend
    │   ├── app.py            # Flask app
    │   ├── Dockerfile        # Dockerfile for backend
    │   ├── download_model.py # Download mBART model
    │   ├── requirements.txt  # Python dependencies
    │   └── st_app.py         # Streamlit app
    │
    ├── /frontend
    │   ├── /src
    │   │   ├── /controllers
    │   │   ├── /public
    │   │   ├── /routes
    │   │   └── index.ts      # Express app
    │   │   └── server.ts     # Server
    │   │
    │   ├── .dockerignore    # Dockerignore for frontend
    │   ├── .gitignore       # Gitignore for frontend
    │   ├── Dockerfile       # Dockerfile for frontend
    │   ├── nodemon.json     # Nodemon config
    │   ├── package.json     # Node dependencies
    │   └── tsconfig.json    # TypeScript config
    │
    ├── docker-compose.yml   # Docker-compose for frontend and backend
    └── README.md            # This file

## How to build and run the project:

To run the project locally, you need to have [Docker](https://docs.docker.com/get-docker/) and run the following command:

    docker-compose -f docker-compose.yml up

Then, open the browser and go to [http://localhost:8333](http://localhost:8333) to use the application.

## References:

-   Repo [nodejs-openai-image](https://github.com/bradtraversy/nodejs-openai-image/blob/main/public/js/main.js) for the frontend
-   Repo [mt_demo](https://github.com/thangdduong/mt_demo) for the backend
-   [Writing docker-compose.yml file](https://milanwittpohl.com/projects/tutorials/Full-Stack-Web-App/dockerizing-our-front-and-backend)
-   [Setup TypeScript project](https://khalilstemmler.com/blogs/typescript/node-starter-project/)
-   [Copying none ts files when building project](https://vccolombo.github.io/blog/tsc-how-to-copy-non-typescript-files-when-building/)
-   [Docker Build Typescript Node.js Server](https://www.youtube.com/watch?v=82gwumVIXFo)
