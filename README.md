# competition-sager

<h1> This is registration django project </h1>
<p> Prerequists are: </p>
<ol>
 <li> Python 3.9.5 (Or install any version above 3.6)</li>
 <li> requiremets.txt, if not found you can see these packages to install inside your virtual environment:</li>
 <p> 
     django==3.2.4
  <br>
     djangorestframework==3.12.2
  <br>
     django-countries==7.2.1
  <br>
     Pillow==8.1.2 
  <br>

 <p>
</ol>

<p> After installing Python 3.9.2, and download the project </p>

<ol>
 <li> Go to the root directory and install venv on by using this command on Terminal of VScode or cmd 
  <br>
  <strong >   <br> python -m venv .    <br>    <br>
   <br> </strong> 
 </li>
 <li> If you work on Windows OS then run this code to activate venv on Termina of VScode or cmd on the root directory
  <br>
  <strong >   <br> scripts/activate   <br></strong> 
 </li>
  <li> After activation of the venv, using cmd or VScode Terminal change directory (cd) to 'competition' folder
  <br>
  <strong >   <br> cd competition   <br></strong> 
 </li>
   <li>(Optional) Be sure that you are in the folder that has these files (manage.py , requirements.txt) by using ls command inside Terminal VScode or cmd
  <br>
  <strong >   <br> ls   <br></strong> 
 </li>
    <li> install packages that are in requirements.txt file using this command in Terminal of VScode or cmd
  <br>
  <strong >  <br> pip install -r requirements.txt   <br></strong> 
 </li>
 
  <li> Wait until the required packages were installed, after they are installed run this command on Terminal of VScode or cmd, be sure you are in the same folder that has these files (manage.py, requirements.txt)
  <br>
  <strong >   <br> python manage.py runserver  <br></strong> 
 </li>
 
   <li> (Note) | (Optional) for the last point you can runserver on your local IP address with open port to open the website from mobile on the same network and here is an example:
  <br>
      <br>
  <strong >python manage.py runserver 192.168.1.<your_last_ip_number>:2020</strong>
    <strong>python manage.py runserver 192.168.1.71:2020</strong>
     <br>
 </li>

  <li> After run the runserver command, you will see this output on Terminal VScode or cmd, then copy the ip:port 127.0.0.1:8000 or combine ctrl + left click 
  <strong >
     <br>
           <br>
           System check identified no issues (0 silenced).
            <br>
           June 14, 2021 - 01:04:54
            <br>
           Django version 3.2.4, using settings 'competition.settings'
            <br>
           Starting development server at http://127.0.0.1:8000/
            <br>
           Quit the server with CTRL-BREAK.
     <br>
 </strong> 
 </li>
 </ol>
