# Nuxt 3 Minimal Starter

Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install the dependencies:

```bash
# yarn
yarn install

# npm
npm install

# pnpm
pnpm install --shamefully-hoist
```

## Development Server

Start the development server on http://localhost:3000

```bash
npm run dev
```

## Production

Build the application for production:

```bash
npm run build
```

Locally preview production build:

```bash
npm run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.


### to run the backend server 
cd to the root directory of the whole project, then:
- pipenv install --python 3.10 (or 3.8)
- *if it was successfull: * 
- pipenv shell
- python manage.py makemigrations
- python manage.py migrate 
- *delete the db.sqlite3 file from the root directory of the whole project, then download the correct one (shared on dis) to the same place*
- python manage.py runserver

*if errors:* send on discord with a screenshot 


#### then: you can sign in on the website using : 

|username | password|
|-------|-------|
|root | toor|
|dina | password!@#|
|yaroslav | password!@#|
|asser | password!@#|
|youssef | password!@#|
|andrii | password!@#|

#### and now you have data to work with like books in shelves and stuff 

GOOD LUCK 