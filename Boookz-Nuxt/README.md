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


#to run json server :
json-server -w -p 4000 ./data/books.json 

### to run the backend server 
pipenv uninstall -all;pipenv install;pipenv uninstall python-magic;pipenv uninstall python-magic-bin;pipenv install python-magic;pipenv install python-magic-bin

pipenv shell
python manage.py runserver