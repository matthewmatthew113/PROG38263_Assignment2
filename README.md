Secure Software Assignment 2
-----------------------------
Matthew Souter & Manraj Kang


Account credential Information
Admin account
username: admin
Password: testing321

User account
username: newuser
Password:testing321

username: newuser2
Password:testing321

commands to ensure our project works properly:
pip install django-crispy-forms
Pip install pillow
pip install django-bootstrap-static
Pip install django-sslserver

Administrator:
Our project includes 3 tiers of users, Administrators, Users, and visitors. All of the users can list and view public posts. Admins can list, create, edit, update and delete users. The admin interface is not accessible by the user and visitors tiers. Admins can log in from an admin portal by accessing the “/admins” page in the url link. Admins can also view and list all of the posts on the site, however they are not able to edit or modify any of the posts at all. Admins also do have an option to logout when they are done using the system.

Users:
Users have access to list, create, edit, update as well as delete their own posts. We could not get private posts working with our site. Users are able to log out when they are done interacting with the system. Users also have the option to edit their usernames as well as reset their passwords (using a valid email address). We were unable to get the “watch words” configured on our site.

Visitors:
Visitors can create a new user account. They can also log in once they made their new user account. Finally the new user is able to perform a password reset if they require to do so.

Posts:
Posts can have titles and content uploaded with them. The home page displays the most recent posts. Users are able to type posts in and upload them. The posts will include the user that posted them and the date and time they were uploaded, the title of the post as well as the content of the post.

Security:
The entire application is secured using HTTPS (the certificate is not valid because we were not paying a 3rd party to make it legitimate.) We included a CSRF token to enable the user to always have a secure connection to our site when performing requests. Our SQL server is also secured to prevent injection attacks. Our application features a secure authentication and authorization scheme provided to us by the Django framework.

Other requirements:
We include the different versions that we created throughout this assignment. This can be found on our public Github repository. The link for this is: https://github.com/matthewmatthew113/PROG38263_Assignment2.git
Our code includes documentation/comments where necessary.
We have the ability to revert changes by accessing the older version on Github.

We had some difficulties with some of the functionality aspects of this assignment however we did implement a good chunk.
Thank you for using our application. We hope you enjoy.
