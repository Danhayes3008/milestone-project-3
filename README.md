Project Status: <strong> In Progress</strong>

<strong>Milestone Project 3</strong>
-

The purpose of this project is to create a public database full of recipes that everyone can freely use.
It is my hope that this site will provide all users with new recipes weekly depending on how often the
members add new content.

-----------------------------------------------------------

<strong>UX</strong>
-

To prevent inapropriate content being added to the site a custom made admin system is used to check
recipes being added before there able to be viewed publicly. If a user were to add content that should not be
on the site, the admin is able to delete the user. The site is a simple one in layout and looks but it 
meets the requirments of what i wanted it to do. people are able to create simple accounts that dont require
any personal information like e-mail addresses or other stuff so no encryption was needed (couldnt get the encrypt to work
hence why the user system is basic)

On Desktop view there is a bug within the category and subcategory selectors were it takes two attampts to
get it to show up. This flaw does not happen on mobile or tablet though. When viewing recipes i have gone for a
system were you need to select the category on the recipes page to be redirected to the page that shows
all the recipes in that category. It is my hope that the admin system, custom form for adding recipes
and category selection part of looking at recipes will help people overlook the basic look of my site.
I could have made more improvments on it if there was more time.

Unfortunately i did not have time to add a search bar system.



-----------------------------------------------------------

<strong>Wire Frames</strong>
-

I have included images into this project that contain the wire frames. I
attempted to stick to the design I made at first but complications made me slightly
change what the dashboard looks like. The current layout of the website is the
closest i could get to the wire frames i made, it is posible to have a site exactly how i wanted it to
look but i needed to get this project submitted so i made changes to get it up and running faster.

-----------------------------------------------------------

<strong>Preview</strong>
-

The following link sends you to the preview of this dashboard:<strong><a href="
https://my-milestone-3.herokuapp.com" target=
"_blank">
Milestone project 3</a></strong>



-----------------------------------------------------------

<strong>Technology’s:</strong>
-

<a href="https://en.wikipedia.org/wiki/HTML" target="_blank"><strong>HTML</strong></a> 
- 
This is the standard language for making websites.

<a href="https://en.wikipedia.org/wiki/Sass_(stylesheet_language)#SCSS" target="_blank"><strong>SCSS</strong></a>
- 
In combination with Bootstrap and Materialize I used my own SCSS files to give the website a personal touch.
This also allowed me to get the site to work properly on all devices, and a alright look that should pass.


<a href="https://en.wikipedia.org/wiki/JavaScript" target="_blank"><strong>JavaScript</strong></a>
-
JavaScript was used to add more instructions and ingredients buttons to work, make the slideshow in the index page
to work (it is a simple slideshow, would improve it if i had more time) and get the navbar to work correctly. All of these javascripts
are placed in the bottom of the base.html template.


<a href=”https://getbootstrap.com” target="_blank"><strong>Bootstrap</strong></a>
- 
I used Bootstrap to include icons for the social media at the bottom of every page.

<a href=”https://materializecss.com/” target="_blank"><strong>Materialize</strong></a>
- 
I used materialize for the framework as it was used in the mini project, unfortunatly i found materialize dificult to work with so in future projects i might not use it.

-----------------------------------------------------------

<strong>Layout</strong>
-

The layout for this website is very basic due to time constraint, at first i tried to make the page that displays the recipes have a filter on the left
side of the screen with the recipes displayed on the right. Unfortunately i couldnt get this to work so i changed the layout to have a card for each category
that links to a specific page in which the user can view each recipe for that category. on the categorty pages i have placed the recipes inside a scroll function
so that the user does not have to got down a long page, this scroll system is also used on the admin page, userpage and each category page.

In the page that displays each recipe i have tried to keep it looking decent but that was tricky. in the instructions section there is a big gap between the last paragraph
and the bottom of the section. This could not be rectified in time for submitting. on the add recipe page i tried to keep the layout as simple as i could so that users find it easy to use.

The register and login pages are basicly the same layout, the only difference in them are that the login page has a link to the register page. Each page has a notification for if a user 
inputs an invalid username. When the correct username and password is entered the user gets redirected to the userpage, from here they can view all there contrabutions to the site and click
the add recipe button to add more recipes. If it is the admin who is logged in they can then click the Admin functions button to be directed to the admin page.

The admin system was not a needed part of this project, but was added to protect the site and myself from trouble. This is because there is no control on what people could enter into the form
so a system was developed to allow myself to control what is public and what is not in regards to recipes. To do this there is a section of the admin page were a list of recipes awaiting approval
(automaticly set and not approved when recipe is created). Next to this is a list of users inside a scroll function, this will allow me to delete users if needed.

-----------------------------------------------------------

<strong>Deployment:</strong>
-

As like my last two projects I have uploaded my project to Git-Hub for storage but the deployment
was done through Heroku this time. To upload to Git-Hub you first have to create 
a repository on Git-Hub then enter the following commands onto the command window on cloud 9:


- First i clicked on the project i wanted to have deployed.
- Then i selected settings and scrolled down to the GitHub Pages section in options.
- Here we must first select the source (the branch to be deployed).
- After selecting the source i selected a theme to be used.
- Next was to choose a domain. This however is not requierd for a course project.

To deploy through Heroku the following steps need to be followed:

- on the Heroku site after loggin in, head to the dashboard and click on the new dropdown menu and select the new app.
- set a app name that has not been used already and set a region then click create app.
- there are three ways form here to deploy to heroku, the one i chosen was connecting to github. in this method all you have to do is input the repository name form github in the repo-name section.
- After that is done go to settings adn click config vars. here you can add the port, id and MONGO_URI in the key/value sections.
- When all this is done all that is needed is to push to github as Heroku will automaticly update.

The website address is: <strong><a href="https://danhayes3008.github.io/Milestone-Project-2/" target="_blank">London dashboard</a></strong>

-----------------------------------------------------------

<strong>Bugs</strong>
-

there is a bug in the category and subcategory dropdown menu's on desktop, this has not been fixed yet but all that is needed to be done to select something is click on the
dropdown menu a few times (usualy just twice). another bug is were there is a big unused space at the bottom of the instructions section of each recipe. i have not figured out
how to fix this yet but it does not effect the site.


-----------------------------------------------------------

<strong>Testing:</strong>
-

The testing has been done manually again whilst developing the site. This has helped me solve some problems i have been having during development such as getting the session name to display on
the navbar, filtering the recipes (got around this problem with the use of pages designated for each category). adding more input fields into the add recipe form, setting author of the recipes,
a number of typo's, simple mistakes such as missing brackets and semicolins. Other problems that was discovered during development were due to attempting to get all pages layout to work on all screensizes.

All testing was done whilst working on each part so that i could fix problems as they came up. Another reason was because sometimes the site would go down if there was a problem due to it being run through a python files
that renders all the pages when in use.

-----------------------------------------------------------
<h3>Contrabutions</h3>
-

Shane Muirhead helped me get my logging system working correctly, i couldnt have gotten this done without his rewriting of my code
He has also helped me out on getting my recipespage.html working but helping me get the code right. the coding he helped me get right
was the part that selects what recipe the user wishes to see in the recipespage.html, the section at the bottom of this page were 
you can view other recipes. everytime i got help from shane, he has pointed out that my code was close and just needed adjusting to make
it work thus the code in my project is mine but rewritten by shane in some area's.

another part he helped me with was the session stuff, he helped me get my page to save the username from the login form as session name so that the site knows who is logged in.
this also lead to help getting the session name set as author name when a recipe is added to the site, in this part he explained it would be easier to write the 
dictionary for the form instead of having the route do it for me. this also allowed me to set approval to no when the form was pushed to mongodb. He also helped me sort out the logout part of the user
system.

The javascript that controls the add ingredient and add instruction buttons was found at <a href="https://stackoverflow.com/questions/42015443/new-input-on-button-click">This site</a>.
following what i found here i was able to make some changes to make it work for my site.

This site was built to be used in my course work, it is in now was a real site and all content within it has not been used for camertial use. The recipes added by the author Admin belongs to
the bbc good food website. The images used for the categories cards in the recipes.html page were found on google images, i found these by looking for images that shouldnt violate any copyrights.
To prevent any copyright violations a notification was added to the add recipe form asking for only images that dont violate any copyrights to be added.