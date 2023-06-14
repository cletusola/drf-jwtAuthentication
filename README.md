# Jwt Authentication 
<h3>user auth with django rest framework and react js using django rest_framework_simple_jwt.</h3>

<h4>DIRS:</h4>
<p>Contains "backend" and "frontend folder"</p>
<p>Backend folder contains the backend code</p>
<p>Frontend folder contains the frontend code</p>

<h4>Usage</h4>
<h5>Backend:</h5>
<p>clone: git clone drf-jwtAuthentication.git</p>
<p>create virtual env: i.e python3 -m venv env</p>
<p>Activate vitual env i.e source env/bin/activate </p>
<p>install required libraries: pip intall -r requirements.txt (requirements.txt file contains the required libraries for backend only)</p>

<h5>Frontend:</h5>
<p>After cloning the repository, you change dir to "frontend/auth", then install the required packages with "npm install"</p>

<h4>Note:</h4>
<p>This project is focused on just jwt authentication with django_rest_framework and react js and nothing more</p>

<h4>How it works</h4>
<p> username will be included in the tokens generated by simplejwt, this is to make it easier to get the user's username in frontend after the token is being decoded</p>
<p> tokens are stored in local storage after signing in via the fronend interface, and they are deleted after signing out</p>

