# Bugman
Gamified Bug Reporting/Fixing

A way to gamify and make bug fixing & reporting interesting.

To run the project:

1. You'll need Python(2.x), Pip, git and git-flow.

    Git flow cheat-sheet: http://danielkummer.github.io/git-flow-cheatsheet/

2. Install virtualenv for isolated Python environment and Activate environment.
    
    (http://docs.python-guide.org/en/latest/dev/virtualenvs/)

3. Hit a "$pip install -r Requirements.txt" from respective folder, to install all dependencies.

4. From project folder:


                        python manage.py syncdb


                        python manage.py migrate


5. Run the development Python server: 


                        python manage.py runserver. 
