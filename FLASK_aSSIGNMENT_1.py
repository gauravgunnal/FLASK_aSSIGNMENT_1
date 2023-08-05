'''Q1'''
'''Flask is a micro web framework for Python. It is designed to be simple, lightweight, and flexible, allowing 
developers to build web applications quickly and efficiently. Flask provides the essentials needed to get a web 
application up and running, while also allowing developers to choose and integrate additional tools and libraries as 
needed.
Advantages of Flask Framework:

1. **Simplicity and Minimalism:** Flask follows a "micro" philosophy, providing only the core features needed for web 
development. This simplicity makes it easy to learn, understand, and use, especially for beginners.

2. **Flexibility:** Flask gives developers the freedom to choose the components and tools they want to use, rather 
than imposing a rigid structure. This flexibility allows you to customize your application to your specific needs.

3. **Modularity and Extensibility:** Flask is built around the concept of extensions, which are third-party packages 
that add extra functionalities to your application. This modular architecture makes it easy to integrate features like 
databases, authentication, and more.

4. **Werkzeug and Jinja2 Integration:** Flask is built on top of the Werkzeug WSGI toolkit and the Jinja2 template 
engine. Werkzeug provides low-level utilities for handling HTTP requests and responses, while Jinja2 allows you to create 
dynamic templates. These components provide a solid foundation for building web applications.

5. **Routing and URL Mapping:** Flask uses a simple routing system that allows you to map URLs to specific functions, 
making it easy to define different routes for your application.

6. **Pythonic Coding:** Flask leverages Python's syntax and idioms, making it familiar and comfortable for Python 
developers. Writing Flask applications feels like writing regular Python code.

7. **Active Community:** Flask has a large and active community of developers, which means you can find plenty of 
resources, tutorials, and extensions to help you with your projects.

8. **Well-Documented:** Flask has excellent documentation that covers all aspects of the framework, making it easy to 
get started and solve problems along the way.

9. **Testing and Debugging:** Flask provides built-in support for testing and debugging, allowing you to write unit 
tests and identify and fix issues efficiently.

10. **Scalability:** While Flask is lightweight, it can still handle a range of applications, from small projects to 
more complex ones. With proper design and architecture, Flask applications can be scaled effectively.

In summary, Flask's simplicity, flexibility, and modular design make it an excellent choice for building web applications 
of various sizes and complexities. Whether you're a beginner looking to learn web development or an experienced 
developer who wants a lightweight and customizable framework, Flask provides the tools you need to get the job done.'''

'''Q2'''
from flask import Flask

'''importing request module to insert value in the web API'''
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>HELLO WORLD</h1>"


if __name__=="__main__":
    app.run(host="0.0.0.0")
'''link for referce "https://orange-actor-gtlop.pwskills.app:5000/"'''

'''Q3'''
'''App routing in Flask refers to the process of defining URL routes for different parts of your web application and associating them with specific view functions. These view functions are responsible for handling the logic and generating the responses when a user accesses a specific URL. In other words, app routing determines how your Flask application responds to different HTTP requests at different URLs.

In Flask, app routing is achieved using the `@app.route` decorator. This decorator is used to bind a function to a URL route, allowing you to specify what should happen when a user visits that URL.

Here's an example of how app routing works in Flask:'''

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'You can contact us here.'

if __name__ == '__main__':
    app.run()
```

'''In this example, three routes (`/`, `/about`, and `/contact`) are defined using the `@app.route` decorator. Each route is associated with a view function (`home`, `about`, and `contact`). When a user accesses the respective URLs in a web browser, Flask invokes the corresponding view function, and the function returns the specified response.

**Why Use App Routes:**

App routes serve several important purposes in Flask and web development in general:

1. **URL Structure:** App routes define the structure of your web application's URLs. They provide a clean and organized way to navigate through different sections of your site.

2. **Modularity:** By associating specific routes with specific view functions, Flask encourages modular and organized code. Each route's logic is contained within its own view function, making the application easier to understand and maintain.

3. **Code Separation:** App routes help separate concerns in your application. Different routes can handle different aspects of your application, such as rendering HTML templates, processing form data, or interacting with a database.

4. **User Experience:** App routes contribute to a positive user experience by enabling users to access different functionalities of your application through intuitive URLs.

5. **API Endpoints:** App routes are essential for creating API endpoints in your application, allowing you to expose specific functionalities for consumption by other applications.

6. **Dynamic Content:** App routes, along with URL parameters, allow you to create dynamic content by generating responses based on user input or database queries.

In summary, app routing is a fundamental concept in Flask that allows you to define how your application responds to different URLs. It helps structure your application, separate concerns, and create a clear and intuitive user experience.'''


'''Q5'''
'''In Flask, the `url_for()` function is used for URL building. It generates a URL for a given view function, allowing you to create URLs dynamically without hardcoding them in your templates or code. This is particularly useful when you have defined routes using the `@app.route` decorator and want to generate URLs based on those routes.

Here's an example of how to use the `url_for()` function in Flask:'''

```python
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'You can contact us here.'

if __name__ == '__main__':
    app.run()
```

'''Now, let's create another route that generates URLs using the `url_for()` function:'''

```python
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'You can contact us here.'

@app.route('/generate_url')
def generate_url():
    # Using url_for() to generate URLs for the home, about, and contact routes
    home_url = url_for('home')
    about_url = url_for('about')
    contact_url = url_for('contact')

    return f'Generated URLs: <br> Home: {home_url} <br> About: {about_url} <br> Contact: {contact_url}'

if __name__ == '__main__':
    app.run()
```

'''In this example, we've added a new route `/generate_url` that uses the `url_for()` function to generate URLs for the `home`, `about`, and `contact` routes. When you access the `/generate_url` URL in your web browser, the `generate_url()` view function will be invoked, and it will generate and display the URLs for the other routes.

Remember that the `url_for()` function allows you to dynamically generate URLs based on the route names (function names) you've defined in your application. This makes your code more maintainable and adaptable as you can change route URLs without updating every reference to them.'''

'''Q4'''
from flask import Flask

'''importing request module to insert value in the web API'''
from flask import request
app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_details():
    return '''Company Name: ABC Corporation
Location: India
Contact Detail: 999-999-9999'''

if __name__=="__main__":
    app.run(host="0.0.0.0")
