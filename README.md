# Wiki

This  is a simple Wikipedia like encyclopedia website which allows users to search, edit and create new entries.  

## Features 

- Visiting **/wiki/TITLE**, where **TITLE** is the title of an encyclopedia entry, renders a page that displays the contents of that encyclopedia entry. If the entry requested does not exist, user is presented with an Page Not Found error. 

- **Search box** where user can write the query they are looking for. And if no such query exists they are represented with a list of other entries that include the query as a substring in their name.
- **Create New Page** where users can create their own entries using Markdown.
- **Edit Page** where users are presented with the existing Markdown content which they can edit and save.  
- **Random Page** takes the user to a random encyclopedia entry.

## Screenshots and Demo
  
![Screenshot from 2021-03-14 00-13-33](https://user-images.githubusercontent.com/56313500/111044590-851b1600-845a-11eb-98f1-0e5ed41a9940.png)

---
![Screenshot from 2021-03-14 00-13-39](https://user-images.githubusercontent.com/56313500/111044596-89473380-845a-11eb-9e5c-757b6f12bc63.png)

---
![Screenshot from 2021-03-14 00-15-09](https://user-images.githubusercontent.com/56313500/111044603-8fd5ab00-845a-11eb-9662-e7a6e6f7718f.png)

[Youtube Demo Link](https://youtu.be/AJEdW9yDGYk)

## Run Search locally

### Step 1: Clone project
```
 git clone https://github.com/damlayildiz/Wiki.git
 cd Wiki 
 ```
 ### Step 2: Install markdown
```
 pip install "Markdown==3.2.1"
 ```
### Step 3: Run the project
```
 python manage.py runserver
 ```
