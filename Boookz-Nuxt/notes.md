
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
## 2- To run the  server: 
cd to the BOOOKZ-NUXT project, then:

```bash

npm install

npm run dev

```
**Note: that's all you need, you don't care about the backend server now**
## 4- Then: you can sign in on the website using : 

|username | password|
|---|---|
|root | toor|
|dina | password!@#|
|yaroslav | password!@#|
|asser | password!@#|
|youssef | password!@#|
|andrii | password!@#|




