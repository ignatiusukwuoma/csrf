# Basic CSRF Protection

CSRF attacks are often used by an attacker to make a target web application carry out a state-changing function by sending a request via a target authenticated user's browser without the knowledge of the victim. 
If a request is sent via the form/link presented to the user on the application frontend, then we can assume that the user has knowledge of the request. In the code above, I have attempted to 
prevent the web application from responding to requests that were not made via a form/link presented to the user. This is achieved by including a random string in the user's session to act
as a CSRF token. The token is also included in the form presented on the frontend in a hidden field. If an attacker succeeds in sending a well-crafted state-changing request to the appropriate
route, although the request will be sent along with the victim's session details (if the user is authenticated), yet the request will not include the correct unique identifier which is only included 
in the form on the victim's browser. I have also included logging to get notifications when CSRF attacks are made, though logs are not sent to the application in this basic implementation.

I have used jinja to display this visually and as a basic implementation I have only one csrf_token, but when building a real product, I will generate a unique identifier for every form/link and keep a list a valid identifiers in the user's session as well as on the form/links
to be sent along with the request. 

