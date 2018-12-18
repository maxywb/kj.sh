# programs to install

## homebrew
homebrew is what's called a [package manager](https://en.wikipedia.org/wiki/Package_manager), a piece of software the manages the packages (i.e. software apps/programs) installed on your machine. part of what it does is manage [dependencies](https://help.ubuntu.com/community/InstallingSoftware#Package_Dependencies), the other apps/programs the app you want to install need to be installed in order to work.

for example: you're going to write a little program using `Python 3.7`, which means that `Python 3.7` is a **dependency** of your program. i.e. your program can't function in the absence of the `Python 3.7` software package.

[open a terminal](https://www.wikihow.com/Open-a-Terminal-Window-in-Mac) and execute the following:

```
# install homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# disable anonymous data collection
brew analytics off
```

## zsh
zsh is a [terminal emulator](https://en.wikipedia.org/wiki/Terminal_emulator), aka [CLI (command line interface)](https://en.wikipedia.org/wiki/Command-line_interface), that provides a rudimentary interface for using a computer.

### background

the first trick to using a terminal emulator is to remember that all of the files and folders on your computer are arranged in a [tree shape](https://en.wikipedia.org/wiki/Tree_(data_structure)). also note that **directory** is the technical name for a folder.

```
root
+-- dir1
+-- dir2
    +-- file1
+-- dir3
    +-- file2
    +-- file3
    +-- dir4
        +-- file4
+-- file5

```

in this diagram there are 5 directories: root, dir1, dir2, dir3, dir4. ["root directory" (or "root")](https://en.wikipedia.org/wiki/Root_directory) the technical term for the directory at the top of the tree.

### install zsh

execute the following:
```
brew install zsh
```
then do this to make zsh the default shell (every computer system has multiple flavors of terminal emulators installed, this command will instruct OSX to use zsh when you open the terminal).
```
sudo -s 'echo /usr/local/bin/zsh >> /etc/shells' && chsh -s /usr/local/bin/zsh
```

then do this to change to using zsh right now:
```
/usr/local/bin/zsh
```

#### power of sudo
[sudo](https://en.wikipedia.org/wiki/Sudo), aka "super user do", is a program that allows you to perform actions with administrative privileges. **this is the most dangerous command on your computer.** there are no guardrails with this command, there are a million ways you can use `sudo` do destroy your computer. until you are more adept at maintaining your computer i recommend you never use `sudo` for anything. 

## python

[python](https://en.wikipedia.org/wiki/Python_(programming_language)) is a programming language that is very popular in [web development](https://en.wikipedia.org/wiki/Web_development), [devops](https://en.wikipedia.org/wiki/DevOps), and [data science](https://en.wikipedia.org/wiki/Data_science).

execute the following
```
brew install python
echo "export PATH=/usr/local/share/python:$PATH" >> ~/.zshrc
```

then install helpful packages
```
pip install virtualenv
pip install virtualenvwrapper
pip install numpy
brew install gfortran
pip install scipy
brew install freetype
pip install matplotlib
pip install ipython[all]
```

## sublime
the most important tool for programming is a good [text editor](https://en.wikipedia.org/wiki/Text_editor). 

sublime is a very nice text editor with [tons of features](http://docs.sublimetext.info/en/latest/basic_concepts.html). 

```
brew cask install sublime-text
```
([if that doesn't work here are alternatives](https://stackoverflow.com/questions/27381531/how-to-install-sublime-text-3-using-homebrew))

make it easy to launch sublime from the terminal:
```
sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
echo "export EDITOR='subl -w'" >> ~/.zshrc
source ~/.zshrc
```

## rock 'n roll

in your shell make a directory for your intro program:
```
mkdir test-program
```

and navigate into the directory:
```
cd test-program
```

and then open up the test file:
```
subl computer_guess.py
```
