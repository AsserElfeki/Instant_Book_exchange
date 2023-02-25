# Book Exchange web application
🌐 [visit the deployed website](https://boookzexchange.store/) 

🖥 (desktop viewport)
check other viewports below

![welcome section](./assets/home_page.gif)

**This was a Software Engineering University project** Developed by a team of 7 using Agile methodologies.
it's a portal where book readers can exchange books they already read with new books from other users. It also suggests offerd books in your area.
As a registered user, when adding a book, the application automatically suggests titles of the book while you are typing it, and once chosen it fetches from Google Books API information about the book such as Authors and description (if available). 
****
## Front-End: 
### Tech stack & external libraries: 
- Vue.Js 3 
- Nuxt.js 3 
- TailwindCSS
- Pinia (Store library for vue)
- vuetify
- vue-toastification
- vue3-carousel
- swiper
- iso-638-1 (for languages)
- fontAwesome
- sass

### Integrations:
- the webApp integrates with Google Books API to automatically search for books in a specified langauge and fetch its info. (e.g: Authors of the book)
![adding book example](./assets/adding_book.gif)

## 🐙 Responsiveness and compatibility:
The website is fully responsive for all viewports and compatibale with all major browsers, and have been tested on *Chrome*, *Firefox*, *Opera*, *Edge*.

*📱in mobile viewport*

![scrolling gif in mobile dimension](./assets/mobile_vp.gif)

*in tablet viewport*

![scrolling gif in tablet dimension](./assets/tablet_vp.gif)

****

## Back-End: 
### Tech stack & external libraries: 
- Python
- Django/REST
- PostgresSQL
- Django - postgrespool 2.0 (used to connect to the database in pooling mood)

## deplopyed website: 
The backend engine is running on Apache server, and the front-end is running on a node.js server that is proxied by the apache server. 
🌐 [visit the deployed website on OVHCloud](https://boookzexchange.store/) 
or [visit the deployed website on Netlify](https://boookzexchange.store/) 

****

# How To Use
## 1-Git
Clone the repository (to clone you have to use githubtoken or ssh connection), if you want to do any work on your local version always do:
```sh
git pull
```
## 2- Back-End
### Python
In terminal move to your cloned directory then:
```sh
sudo pipenv install
```
It will install all needed pip packeges (they are in Pipfile).
Next:
```sh
sudo pipenv shell
```
This will put you into virtual environment shell from where you can run commands like:
```sh
python manage.py runserver #starts the server
python manage.py makemigrations #makes migrations, run it after changes to your models.py files
python manage.py migrate #run it after makemigrations
```
## Dependencies
* pipenv 
* python3 at least 3.8

```sh
pip3 install pipenv
```

## 3- Front-End

- **navigate to Boookz-Nuxt** 
``` bash
cd Boookz-Nuxt   
```

- Make sure to install the dependencies:
```bash
# yarn
yarn install

# npm
npm install

# pnpm
pnpm install --shamefully-hoist
```

### Development Server
Start the development server on http://localhost:3000

```bash
npm run dev
```

### Production
Build the application for production:

```bash
npm run build
```

Locally preview production build:
```bash
npm run preview
```



