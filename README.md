Here I am adding Python programming for Beginner Level code

To save work and save it into git files in local directory, make a directory first(if want to create a new one)

pwd
mkdir Directory_Name // any directory name
type ls to check it is created or not
type cd Directory_Name to move inside the directory.
Git workflow for beginners
To access git into local created directory, type command in local pc's terminal and copy the url from the git website: git clone url

Note: It could be chnage from time to time (Talking about command)
or push an existing repository from the command line
git init
git add .
git status
git commit -m "First Commit"
git remote add origin https://github.com/SKShorna/Python-Basic-Beginner.git
git push -u origin master
Can have a look on this video: https://www.youtube.com/watch?v=xLbmcMVtfKE (For Push Code (remote) to Github using Command Line (Terminal))




For Access token-

Visit github-> click-> settings-> developer settings -> personal access token --> (click) --> generate new token

Note-: All-access-pass
No expiration
Check mark all access to everything/every options-> then click generate token button

take the token which will be used for chnages to push in github

Come back to the terminal (local pc) 

type--- git push origin 

1st time it may not work but it will ask for 2nd time then type username(SKShorna) and access token
