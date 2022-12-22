# Progress:

## BackEnd: 
1. added endpoints for all wanted and giveaway shelves 
2. endpoint for all existing users 
3. deleting a user is now doable from the admin panel (and endpoint will be provided to the user later)
4. working on adding the region for each user 

## FrontEnd:

1. integrated tailwind css
2. integrated font-awesome 
3. added the wanted and giveaway shelves in the main page and fetching its data from the corresponding endpoint
4. added profile page and fetching data (for now) from all shelves 
5. register and login and log out are all working 
6. using PINIA for state management 
7. added seperate stores (models) for : User, all books, google API 
8. user store states are reset after logout 
9. profile tabs are fully reactive and lazy fetched
10. we have a separate page for each book 
11. route redirecting after login and logout 
12. website head throughout all the website (will be changed for some uri's later)
    

## Next Steps:
#### BackEnd endpoints: 
- [ ] single profile info. 
- [ ] comments on a book. 
- [ ] transaction endpoint.
- [ ] confirm the books recieved. 
- [ ] ratings endpoints. 
- [ ] deactivating profile. 
- [ ] transaction started notification: a field in the user Json is added, and when the recieving user opens his profile, frontend gets the json with that newly added field and displays a notification accordingly.

#### FrontEnd:
- [ ] data fetching and rendering of the rest of profile components 
- [ ] error messages on sign in and register 
- [ ] transactions page 
- [ ] settings page 
- [ ] route guarding 
