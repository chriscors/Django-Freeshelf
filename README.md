# Freeshelf

This week, you are building a Django application to collect an index of free programming resources (books, articles, blogs, zines, and podcasts) online. You'll work on this application for the entire week. The end goal is an application that allows users to see a list of all the resources, register and log in, and favorite resources.

## Requirements and goals

### Overall requirements

- You will work on this assignment in pairs, using [VS Code Liveshare](https://code.visualstudio.com/learn/collaboration/live-share), and both partners will be typing in the same repository. You will not be using git branches yet, that's coming in phase 3.
- Your application should be styled. It should be usable and aesthetically neutral, at a minimum. There is a sample mockup of the index page in [mockup/index.html](mockup/index.html). You do not have to follow this mockup -- it's just a place to start if you don't have your own ideas. You can write your own css and/or incorporate libraries like Bulma or Tachyons that have styled components.
- When you are not sure about whether a feature is needed, use your knowledge of similar sites and your good sense. Ask yourself 
the question, "would I as a user want the site to have this feature?"
- Remember that a client would rather see one working feature than 10 partially complete features that don't work. Please focus on making sure you have successfully reached one goal before moving on. This will require good communication with your partner.

### Goal 1: User model, registration and login

Your first goal is adding a `User` model using one of the four stratgeies from the [Simple is Better Than Complex article](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html) and adding registration and login to your application using `django-registration-redux`. *Remember to do this first before running any migrations*.

If a user is not logged in, they should see the log in page (a form to log in).

The user should be able to click on links to log in or register, and to log out if they are logged in.

### Goal 2: resources

Your next goal should be creating a Resource model and showing an index of all resources on the homepage. It will be helpful to sketch out this model before creating it. Some details:

- Resources have, at a minimum, a title, author, description, URL, and date added to the database (`created_at`).
- Resource URLs (the URL field in the database) should be unique.
- Admins can add, edit, and delete resources.
- You should have initial data for resources (a CSV is provided, but you can edit it to fit your data).
- Resources should be displayed in order with the most recently added at the top.
- Users should be logged in to be able to see the list of resources on the homepage. That can be accomplished using the `@login_required` decorator explained in this [article](https://realpython.com/django-view-authorization/#restricting-views-to-logged-in-users).

#### Initial Data

To load some initial resources into your database, you can [create a data migration](https://docs.djangoproject.com/en/4.0/topics/migrations/#data-migrations). Read the data from the CSV file and use your model to save data to the database. ([Another good resource on data migrations.](https://simpleisbetterthancomplex.com/tutorial/2017/09/26/how-to-create-django-data-migrations.html))

You can also create resources in the database using the Django admin.

#### Stretch for Goal 2

- Add an optional image url for resources.
- Allow users to change the sorting order of resources, ordering by title or by reverse order of being added.

### Goal 3: associated categories

Your next goal should be adding categories for resources. Each resource should be associated with a category.

- Categories have a title and a [slug](https://docs.djangoproject.com/en/4.0/ref/models/fields/#slugfield).
- Each category should have a URL that shows resource just for that category. For example: `resources/python` or `resources/javascript`.

#### Stretch for Goal 3

- Allow resources to be in more than one category. This will require using a [Many to Many](https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/) relationship.

### Goal 4: user favorites

Once you have registration and login, users should be able to mark resources as their favorites. Every user should be able to go to a URL, `/favorites/`, to see their favorite resources. The resources should be in order with the most recently favorited ones on top. The user can "un-favorite" a currently favorited resource. This will most likely require a new model to represent the relationship between a user and a resource, a `Favorite` model.

#### Stretch for Goal 4

- Show the number of times a resource has been favorited on its entry .


### 🌶 Spicy Features

If you reach the four goals above, challenge yourself to implement these additional features.
#### 🌶 Spicy Goal 1: Add user comments

Users should be able to comment on resources. Each resource will need to have its own unique URL where you can see comments on the resource. Comments should be in order from the oldest to the newest. On resource listing pages (the main page and the category pages), the number of comments should be listed with the resource.

##### Stretch for 🌶 Goal 1

- Make user names on comments links to a user profile page. This page should show all the comments the user has made on all resources.

#### 🌶 Spicy Goal 2: Users can suggest resources

Users should be able to suggest new resources for Freeshelf. You can do this with a separate Suggestion model or by using the Resource model with a new boolean indicating whether the suggestion has been accepted or not. Either way, a new page, `/suggestions/`, should be available to admins, showing them all the current suggestions and allowing them to accept or decline the suggestion.

## Project Setup

### Steps after cloning this project repo

```sh
$ pipenv install django
$ pipenv shell
```
- Start on Goal 1 and build the `User` model before you run `makemigrations` or `migrate`.

## Resources

- [Free Programming Books GitHub Repo](https://github.com/EbookFoundation/free-programming-books)
