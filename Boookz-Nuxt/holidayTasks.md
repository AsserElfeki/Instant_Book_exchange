# Merry Christmas everyone

### but we have work :(  I'm so sorry

## Tasks:

- [ ] 1. "~/components/profile/(transactions.vue and ratings.vue)" : HTML , TailwindCSS 
--> **Dina & Yaroslav** 
- [ ] 2. "~/pages/books/[id].vue" : HTML , TailwindCSS, datafetching and rendering --> **Youssef** 
          it should display the cover of the book (by default) and ability to view other images 
          and all info on the book including owener and condition and bla bla bla.
          below the info, there should be a form where the user chooses a book from HIS OWN giveaway shelf to exchange with the book we are seeing. and then a button "trade" that submits the form with a post request to an endpoint that is yet to be done with some info that we yet to determine. 
- [ ] 3. navar should be sticky at the top of the page without overlapping the content. 
         its background should span the full width of the screen while the elements can not span more than 1200 px (like footer) note: this might need editing the >template> part in the "~/layouts/default.vue"--> **Andrii** 
- [ ] 4. settings page (simple) design and according html and tailwindCSS --> **andrii**         
- [ ] 5. Nuxt error and warnings --> **Asser & Michał**
- [ ] 6. settings page data fetching --> **Asser**
- [ ] 7. route guarding --> **asser** 
- [ ] 8. settings page data fetching --> **me / youssef**

*backend guys : break a leg!*


## NOTES: 
1- TailwindCSS is designed to work as "mobile-first-development" which means you should put the classes according to what you want it to look like in the mobile viewport, then different style for the tablet (medium) vp then the pc 
it can look something like this : 
    <div class="w-full md:w-1/2 lg:w-1/3"> 
        <!-- content -->
    </div>
so this element is having the full width of its parent in mobile vp, then half in the tablet (md:) then 1 third in the pc (lg:)

2- complexity is better (and makes your life easier) to be in the HTML part not in the css part 
so whenever you need containers, don't be shy to add div or section 

3- if you need to add a new component, you can do it in the "~/components" folder, and then import it in the page you want to use it in

4- if you need to add a new page, you can do it in the "~/pages" folder

### resources: 
1- HTML & CSS (if needed): https://www.youtube.com/watch?v=hu-q2zYwEYs&list=PL4cUxeGkcC9ivBf_eKCPIAYXWzLlPAm6G

2- Tailwind : https://www.youtube.com/watch?v=bxmDnn7lrnk&list=PL4cUxeGkcC9gpXORlEHjc5bgnIi5HEGhw&index=1

3- tailwind cheatsheet: https://nerdcave.com/tailwind-cheat-sheet


### Be Aware
folders/files that you **SHOULD NOT** touch:
- "~/node-modules"
- "~/nuxt.config.ts"
- "~/package.json"
- "~/package-lock.json"
- "~/tsconfig.json"
- "~/middleware/ 
- "~/nuxt/"
- "~/plugins/"

============================================ 
# STEPS: 

## 1- How to manage git : 
- ```git checkout -b <your-branch-name>```
- when you finished one part, make a commimt to your local branch but do NOT publish it. 
- when you finished all the tasks: 
```
git switch main;
git pull;
git merge <your-branch-name>;
git push;
git branch -d <your-branch-name>;
```


## 2- To run the backend server 
cd to the root directory of the whole project, then:
- pipenv install --python 3.10 (or 3.8)
- *if it was successfull: * 
- pipenv shell
- python manage.py makemigrations
- python manage.py migrate 
- *delete the db.sqlite3 file from the root directory of the whole project, then download the correct one (shared on dis)
- to the same place*
- python manage.py runserver

*if errors:* send on discord with a screenshot 

## 3- To run the frontEnd server: 
cd to the BOOOKZ-NUXT project, then:

```bash

npm install

npm run dev

```

## 4- Then: you can sign in on the website using : 

|username | password|
|---|---|
|root | toor|
|dina | password!@#|
|yaroslav | password!@#|
|asser | password!@#|
|youssef | password!@#|
|andrii | password!@#|




#### and now you have data to work with like books in shelves and stuff 

GOOD LUCK 


