Django documentation 
https://docs.djangoproject.com/en/4.1/intro/tutorial01/

Basic info:
	pip - python packet manager, must be installed manually
		Macos: brew install python; brew unlink python && brew link python
		Windows: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; python get-pip.py. 


### Django

	-----MVC-----

	Django has its own name convension, wellknown to us MVC is actually MTV:
	
	     MVC   |  MTV
	---------------------
	model      -  model (database)
	view       -  template (html)  
	controller -  view 


	Django - BIG framework that is used for creating web applciation.
	
	Django REST - an additional framework that we are going to use. Simplifies work with database by improving native Django views (functions) and introducing better serializers. Also improves the roles of users and the way the users are treated. Mainly needed for serializers.

	Postgresql - the most used and powerful opensource object-relation database that we are going to use. Similar to sql but has some nice features

### VirtualEnvironment

1) ALWAYS use virtual environemt!!!!!

	- Why?

		Makes sure that everyone works with the same dependencies and also simplifies A LOT mounting the django on server.
    
    - To create virtual environement https://docs.python.org/3/library/venv.html:
   
		python3 -m venv /path/to/new/virtual/environment

		e.g. python3 -m venv env

	- Afterwards, always when working with django you must use virtual environment:

		source <environment>/bin/activate

		e.g. env/bin/activate

	- To deactivate virtual environemt:

		deactivate

    - When you install/update some dependencies ALWAYS renew requirements.txt file

		pip freeze > requirements.txt

		--- pip freeze - shows all dependencies in the current environement

		-- ">" the outout of the command to a file "requirements.txt", Note the file is being overwritten

	- To install dependencies defined in requirements.txt:

		pip3 install -r requirements.txt



2) ALWAYS keep convention of virtual environement name because of .gitignore, don't git push your virtual environment folder

------------------

### Django usage

	django-admin startproject <project_name>

	python manage.py startapp <package_name>


## Django Database

# When changes to database model are done must use "migrate" to apply:

	python manager.py makemigrations (creates a migration file that contains all updates)

	python manager.py migrate        (applies the changes)

# To access django shell (for debugging purpose):
	
	python manage.py shell

	you must import all needed files, e.g. models, views




