# smoothie_p3_app

View here: 

## Description

The Smoothie Share Recipe app is a web application where users can create, share, and find smoothie recipes. It is user friendly, and its easy navigation means users can easily sign up or login. When logged in users can add new smoothies Users can only add, edit and delete their own recipes when logged in. They can not change other users recipes. Smoothie ingredients are shown for logged in users. Non-logged in users will see a prompt to log in. This will encourage people to sign up.

## Project requirments

The project requirements are to create and deploy a data centric web application using Django. Users must be able to log in and perform CRUD operations, Create, Read, Update and Delete. The site should be user friendly and responsive. It must be deployed on Heroku.

## User stories

## Features

## Future Features

## Design

### Database Schema

### Colour scheme

### Typography

### Wireframe

## Technologies used

## Tools used

## Deployment

## Testing

## Lighthouse reports: 

## W3C Markup Validation

## W3C CSS Validator

**Manual testing:**

**Features:**

## Bugs and Fixes

| Bug | Cause | Solution | Result |
|-----|-------|---------|--------|
| CSS test page (/css_test/) returned 404 and CSS did not load. | URL path mismatch in Django routing (css_test/ vs /css-test/). | Fixed smoothies/urls.py to use path(css_test/, views.css_test, name=css_test); ensured base.html loads static CSS and style.css exists in static/css/. | Page loads successfully and CSS background-color is applied. |
|  |  |  | |
| Server failed to start when loading smoothie views. | SmoothieForm was imported in views.py before forms.py existed in the smoothies app. | Created forms.py in the correct app directory and defined SmoothieForm. | Server starts successfully and smoothie views loads correctly. |
|  |  |  | |
| Footer was in the middle of the page. | Page layout did not push footer to the bottom of the page.  | Added flex layout to body and main in CSS. | Footer stays at the bottom of the page. |
|  |  |  | |
| Testing add smoothie while not logged in caused 404. | LOGIN_URL not set in settings.py.  | Added LOGIN_URL = '/login/' in settings.py. | Non logged in users are now redirected to the login page. |
|  |  |  | |
| Navbar and footer disappeared when preparing for deployment. | STATICFILES_FILES pointed to the wrong static directory.  | Updated STATICFILES_DIRS to reference the root static folder. | CSS loads correctly and navbar and footer display as expected. |





## Credits

**Youtube tutorial Django Recipe Sharing Tutorial by Dom Vacchiano. I used this video as a guide along with my own code, some python conventions and patterns used are 
  similar.**

[See video here](https://www.youtube.com/watch?v=w7EJu9Gd5Ns&list=PLQbt1tI_yQHg5HYpdUqit1wkc4BOPTkpx&index=1)

---

**Youtube tutorial Django Recipe Sharing Tutorial by Dee Mc. I used as a guide with my own code, some python conventions and patterns used are similar.**

[See video here](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)

---

**Google Fonts:**

**Canva:**

**Favicon:**

**Font Awsome:**
