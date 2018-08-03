# A Peer to Peer Sports Betting System

## our initialized git repo

### For now, checkout your own branches and push whatever you want there. We'll decide what code we want to merge to the master branch once we like it
if you guys need help/advice on setting up or using github commands from the terminal, let me know 

click on the branch dropdown option above this and go to my branch and read the readme
  
Here's how to get started from the terminal.
cd in a new directory and type
```angular2html
✗ git clone git@github.com:collinol/Blockchain-Powered-Betting.git
```
and you should see 
```angular2html
Cloning into 'Blockchain-Powered-Betting'...
remote: Counting objects: 53, done.
remote: Compressing objects: 100% (43/43), done.
remote: Total 53 (delta 8), reused 40 (delta 2), pack-reused 0
Receiving objects: 100% (53/53), 21.01 KiB | 0 bytes/s, done.
Resolving deltas: 100% (8/8), done.
Checking connectivity... done.
```
Then
```angular2html
✗ cd Blockchain-Powered-Bettting
✗ git pull
Already up-to-date.
```
Now create your own branch to work on so you're not committing files to the master branch

```angular2html
✗ git checkout -b <your_name>_Branch
```
Now you can create whatever files you want. I would suggest copying your lab5 mining
assignment into this directory and uploading it.
```angular2html
✗ cp -r path_to_mpcswork56600/lab5/ .
```
Be sure to copy the directory recursively with the -r flag, otherwise 
bash will tell you "cp: omitting directory 'path/lab5'" and make you copy
all the files individually and that'll just be annoying to deal with.
  
Next, create a readme.md file and write in any ideas you have or stuff you
think we should start working on. You don't have to, but if you want to do fancy text stuff
> Like this
### or this
```angular2html
Or this
```
here are a few markdown syntaxes
```angular2html
# - used for titles (the second example above)
# is biggest
## is for a subsection
### is for a subsubsection

to make a note (first example)
> text goes here. One 'greater than' symbol for a note that's indented once
>> gets indented twice. See below
```
> One indent note
>> two indent note
```angular2html
Finally, use a pair of ``` (backticks) for block code like what I'm  
currently typing in. Use a pair of single backticks for one line code

```
`single backticks` 

Also pretty important, if you hit enter while typing in a readme, 
while the text will be written on the next line, it won't appear on the next
line in the readme. Use double spaces for that.
So like, everything I just wrote from "Also" to "for that" doesn't contain a double space,
so it's written to the end and wraps to the next line.  
However,  
If,  
I didn't want that.  
And wanted to break to a new line earlier  
End your sentence with double spaces.

Now commit your lab 5 and readme.md

```angular2html
git add README.md lab5/
git commit -m "hurr durr some dumb message"
git push -u origin <your_name>_Branch
```
