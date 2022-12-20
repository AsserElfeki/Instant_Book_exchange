#### how to run this shit 

1. pipenv --python 3.10 
2. pipenv sync   
3. pipenv shell
4. delete files in the migrations folder but not "init" (authentication & booksdata )
5. delete db.sql 
6. python manage.py makemigrations 
7. python manage.py migrate
8. python manage.py createsuperuser  
9. python manage.py runserver 