Django documentation 
https://docs.djangoproject.com/en/4.1/intro/tutorial01/

Basic info:
	pip - python packet manager, must be installed manually
		Macos: brew install python; brew unlink python && brew link python
		Windows: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; python get-pip.py. 


# Django

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

# VirtualEnvironment

1) ALWAYS use virtual environemt!!!!!

	- Why?

		Makes sure that everyone works with the same dependencies and also simplifies A LOT mounting the django on server.
    
    - To create virtual environement https://docs.python.org/3/library/venv.html:
   
		`python3 -m venv /path/to/new/virtual/environment`

		e.g. `python3 -m venv .env`

	- Afterwards, always when working with django you must use virtual environment:

		`source <environment>/bin/activate`

		e.g. env/bin/activate

	- To deactivate virtual environemt:

		`deactivate`

    - When you install/update some dependencies ALWAYS renew requirements.txt file

		`pip freeze > requirements.txt`

		--- `pip freeze` - shows all dependencies in the current environement

		-- ">" the outout of the command to a file "requirements.txt", Note the file is being overwritten

	- To install dependencies defined in requirements.txt:

		`pip3 install -r requirements.txt`



2) ALWAYS keep convention of virtual environement name because of .gitignore, don't git push your virtual environment folder

------------------

# Django usage

	django-admin startproject <project_name>

	python manage.py startapp <package_name>


## Django Database

### When changes to database model are done must use "migrate" to apply:

	python manager.py makemigrations (creates a migration file that contains all updates)

	python manager.py migrate        (applies the changes)

### To access django shell (for debugging purpose):
	
	python manage.py shell

	you must import all needed files, e.g. models, views



#SE bookexchanger development guide:



# Docker

14min Docker main idea explained https://www.youtube.com/watch?v=rOTqprHv1YE&t=438s&ab_channel=Simplilearn

2min Docker really briefly the idea https://www.youtube.com/watch?v=Gjnup-PuquQ&ab_channel=Fireship

Files used:

##DockerFile - an instruction file that tells how to build docker image
f.e.

```
		FROM python:3.9.6-alpine    | based on which image to build our custom image
 
		WORKDIR .                   | working directory inside out image
		
		# set environment variables 
		ENV PYTHONDONTWRITEBYTECODE 1   | 2 environment variables prevents python from writing to console and buffering
		ENV PYTHONUNBUFFERED 1
		
		RUN apk update \
	    	&& apk add postgresql-dev gcc python3-dev musl-dev      | update apk (file manager) inside our image
		
		COPY . .        | COPY <path_to_file/dir_you_want_to_copy_from_local_machine> <path_inside_image>
		                | ". ." means that all files in current local machine directory where Dockerfile is to working director
		
		# install dependencies
		RUN pip install --upgrade pip   | running shell command which is "pip install --upgrade pip"
		RUN pip install -r requirements.txt
		
		# make entrypoint.sh executable
		RUN chmod +x ./entrypoint.sh   | adding possibility to execute shell script entrypoint.sh (copied by "COPY . ." )
		RUN sed -i 's/\r$//g' ./entrypoint.sh | sed command to remove trash character at the end of lines
		
		ENTRYPOINT ["./entrypoint.sh"]   | use our entrypoint.sh as entrypoint (first executable shell)
```
		
##docker-compose.yml - file that simplifies the run of containers, basically each element can be substitute with "docker run" command
IMPORTANT in yml extension spaces make difference, be careful
f.e.
```	  
	  db:
	    image: postgres:13.0-alpine                 | based on which image instatiate the container
	    volumes:
	      - postgres_data:/var/lib/postgresql/data  | <custom_name_of_volume>:<path_inside_postgres_container_where_volume_is_mounted>
	    environment:								| Declaration of required environment variables
	      - POSTGRES_USER=hello_django
	      - POSTGRES_PASSWORD=hello_django
	      - POSTGRES_DB=hello_django_dev
	    ports:
	      - "5432:5432"                             | port expose <transfer_to>:<postgres_port>
```
##entrypoint.sh - a script created by me to make sure that db run as expected

## AWS

Cloud where our server will be running


#The flow

1) You must pull from master branch on github https://github.com/AsserElfeki/Instant_Book_exchange
2) Set environment, `python -m venv .env; source .env/bin/activate`
3) install requirements to virtual environment `pip install -r requirements.txt`
4) Make changes where you want to make them
5) Test them on your local machine by running it inside docker container as follows
   ```
   docker-compose -f docker-compose-local.yml pull # to update the image that might be create on your local machine
   docker-compose -f docker-compose-local.yml up -d # "-d" is used to run in detached mode (background)
   ```
   go to 0.0.0.0:80 and check what you want to check
6) Don't forget to push your changes to github master
7) Since I am still lazy to create webhook to github you should manually push changed image to dockerhub
   ```
   docker-compose -f docker-compose-local.yml push
   ```
   Note: there might be additional step be needed if there are problem with architectures. Might be not, dunno
8) Now me or you should apply changes at the server in aws.
9) Finally you and even people on the moon must be able to see changes on the server 






