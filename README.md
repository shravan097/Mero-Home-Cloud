# Mero-Home-Cloud
A Personal Cloud Storage for home use.
Almost same to service of DropBox but it is your personal home cloud service.  Home members within same network can access files,photos and manymore either for themselves or for public.  Just type in the web address and thats it.

# Screenshots of Final Build:
Here are some screenshots of what it looks like:
**Homepage**
![](https://github.com/shravan097/Mero-Home-Cloud/blob/master/homepage.png?raw=true)
**Audio Player Page**
![](https://github.com/shravan097/Mero-Home-Cloud/blob/master/audio.png?raw=true)
**Upload File Page with Encryption System**
![](https://github.com/shravan097/Mero-Home-Cloud/blob/master/upload.png?raw=true)


## How to Run this Code:

**You must have Python 3 to run this code. Look [Here](https://www.python.org/downloads/)**

To check if you installed Python 3, run this on terminal `python3 --version`.

Next, you need to install, Django.

Run this on terminal `sudo pip3 install Django`

And just to check if you installed Django properlly. Run  `python3 -m django --version`

Now, go to the directory where you have cloned Mero-Home-Cloud. Then again go inside `homeserver`.

Then run this:

`python3 manage.py runserver`

Now go to your browser and type this on the URL: (http://127.0.0.1:8000/cloud/).

**The Audio Player calls DropBox API so you need to create access Token. It was required in order for chromecast to work without any fees.**

# DEV Info
Here is a login credintial to Django Admin Portal:
<br>
`user: admin`<br>
`pass: helloworld`

