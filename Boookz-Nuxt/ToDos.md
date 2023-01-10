# This is ALMOST everything that's missing from our final version 
if you work on one of them please let the others know so no 2 people work on the same thing

## Missing functionalities
- [x] 4.clear all notifications 
- [x] 1.show the total of notification, and profile tabs 
- [x] 3.filter home page books by region / pref
- [x] trade button in case of guest should not be there 
- [x] notification number should not be there if 0
- [x] limit number of rendered books in homepage 
- [ ] 2.in wanted books, the button trade should only appear if I have the book and then it shows me one of his giveaways
- [ ] check on each redirect if the token is still valid and update state 
- [ ] optimize bookshelves to be 1 item
- [ ] delete "remember me?"
- [ ] **add country to register (iso something)**
- [ ] **get category of books from google api as well**
- [ ] description in addbook form 

## In all forms:
- [x] 1. buttons styles
- [ ] 2. **toasts to inform the user what happened**
- [ ] 3. styles (we need same style for all forms)


## Settings form: 
- [ ] 1. split into 2 forms : 1 for info and the other for password
- [ ] 2. categories of books he likes
- [ ] 3. fetch data to be there automatically and he changes it
- [ ] 4. ability to change username (does it exist in BE?)
- [ ] 5. spoken languages field 
- [ ] 6. deactivate account ability 
- [ ] 
  
## Contact Support 
- [x] 1. form in separate page 
- [x] 2. link in footer 

## Search page
- [x] 1. new page "./searchresults"
- [x] 2. fetch data and render it 

## About page
- [ ] 2. nice styles (place to try whatever) **Asser**

## Styles: 
- [x] shelves books 
- [x] buttons in transactions and shelves and login/register and addbook 
- [x] footer hover 
- [x] book card responsiveness 
- [ ] ?? display the uploaded image in the addbook page

## Refractoring
- [ ] code cleanup and robstness and reusability
- [ ] merge giveaway & wanted in 1 component 
- [ ] mergeing bookcards 

## Bugs 
- [ ] 1. profile pic not loaded instantly after refresh
- [ ] homepage books layout after refresh and the "oops" message is repeated
- [ ] region filter is buggy (fix by loading data store again after login)
## enhancments : 
- [ ] 1. add a loading spinner when fetching data
- [ ] dark mode
- [ ] transitions and animation
- [ ] use <v-card> for bookcards