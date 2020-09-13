# Tim Holmes - Phillies Submission

The following are answers to the Phillies' questionnaire. The answer to Question 1 can be found under [palindrome.md](./palindrome.md) 

This application consists of two parts: a Python + Flask server and a Node + React server.

At the end of this process, you should be able to access the UI at [localhost:3000](http://localhost:3000). The API will live on port 5000, the docs can be found at [localhost:5000/v1/ui](http://localhost:5000/v1/ui).

## Build and Run with Docker

This application can be built and ran with `docker-compose`. Docker, compose, and all of its depdencies can be found in a single downlaod via [dockerhub](https://docs.docker.com/desktop/).

With docker-compose, it's as simple as:

```zsh
cd ./phillies-submission
docker-compose up
```

The servers will start up after the build process is completed.

## Build and Run from Source

### Required Tools

Building from source requires Python and Node environments with package managers installed on the machine. For Python, I recommend [pyenv](https://github.com/pyenv/pyenv) managing versions and [poetry](https://python-poetry.org/) for a package manager.

```zsh
# install pyenv
brew update
brew install pyenv

# install poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

For node management, [`nvm` is awesome](https://github.com/nvm-sh/nvm) This tool allows you to easily switch between node versions and comes with supported pairings of `npm`.

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```

### Backend

Now we can build and run the application, starting with the backend. 

Run server:
```zsh
cd ./backend/

poetry install # install our dependencies

API_HOST=localhost API_PORT=5000 poetry run python server/main.py
```

OpenAPI documentation is found at [localhost:5000/v1/ui](http://localhost:5000/v1/ui).

### Frontend

```zsh
cd ./frontend/
nvm use # skip this step if you don't use nvm, 
        # but make sure your node version matches 
        # that listed in ./.nvmrc
npm install
npm start
```

The UI should now be running on port 3000.