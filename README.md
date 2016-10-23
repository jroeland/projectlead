# Teapot

Teapot is a python-django based application wrapped in
docke-compose which calculates discounts for orders.

## Features
- A simple REST-API which can be easely used in class based views
- Unit-tests
- Admin interface

## How to get Teapot

    git clone https://github.com/jroeland/teapot.git

## Install instructions - Fast (Tested only in linux-debian based distributions)
Requirements:
- pip

It is possible to runproject without having to use docker-compose.
Simply edit the following file:

    /project/web/app/website/settings.py

Change the following variable to True:

    TEST = False
    
Run the following file, which will install the requirements using pip, run
the migrations and load the initial data.
Note: Its recommended to run this command in a virttual env, although
it will still work if ran globally:

    cd project/
    . /easy_build.sh

Now start the django's development server with the following command:

    cd project/web/app/
    python manage.py runserver localhost:8080
    
To run the tests, run the following command:

    cd project/web/app/
    python manage.py runserver localhost:8080

## Install instructions - docker-compose
The service will be running in port 8000.
To change this, edit the file project/docker-compose.yml

To build the project as a micro-service, run the following command:

    cd project/
    . build.sh

If you have made some changes to the docker file and you wish to re-build the service:

    cd project/
    . rebuildAll.sh

### Some extra management commands when using the service:
To stop the service:

    cd project/
    . stop.sh

To start / restart the service:

    cd project/
    . start.sh

To run the tests:

    cd project/
    . runTests.sh

## End-points
The end-points for customers:

    /api/customers/ accepts GET, POST requests
    /api/customers/\<id\>/ accepts GET, PUT and DELETE requests

The end-points for products:

    /api/products/ accepts GET, POST requests
    /api/products/\<id\>/ accepts GET, PUT and DELETE requests

The end-points for product categories:

    /api/products/categories/ accepts GET, POST requests
    /api/products/categories/\<id\>/ accepts GET, PUT and DELETE requests
    
The end-points for free product discounts:

    /api/discounts/freeproducts/ accepts GET, POST requests
    /api/discounts/freeproducts/\<id\>/ accepts GET, PUT and DELETE requests

The end-points for category discounts:

    /api/discounts/categories/ accepts GET, POST requests
    /api/discounts/categories/\<id\>/ accepts GET, PUT and DELETE requests

The end-points for cutomer loyalty discounts:

    /api/discounts/loyalty/ accepts GET, POST requests
    /api/discounts/loyalty/\<id\>/ accepts GET, PUT and DELETE requests
    
The end-points to calculate discounts for an order:

    /api/discounts/calculate/ accepts POST requests

## Admin Interface
To facitilate operations, the admin site is available.
To login to the admin interface, go to /admin/
- Username: admin
- Password: teapotapi

## API request Examples
### GET
Get all customers:

    curl -X GET  http://localhost:8000/api/customers/
    [{
        "model":"customers.customer",
        "pk":1,
        "fields":{
            "uid":"1",
            "name":"Coca Cola",
            "since":"2014-06-28",
            "revenue":"492.12"
        }
    },...]

To get one specific customer, pass the customer id in the url:

    curl -X GET  http://localhost:8000/api/customers/1/
    [{
        "model":"customers.customer",
        "pk":1,
        "fields":{
            "uid":"1",
            "name":"Coca Cola",
            "since":"2014-06-28",
            "revenue":"492.12"
        }
    }]

### POST
To post a Product with a new category:
First create a new category, or the post for the product will be refused:

    curl -H "Content-Type: application/json" -X POST -d @web/app/examples/resources/newcategory.json http://localhost:8000/api/products/categories/
    [{
        "model":"products.productcategory",
        "pk":3,
        "fields":{
            "uid":"3",
            "description":"Garden"
        }
    }]
    
Now we can post a new product:
    
    curl -H "Content-Type: application/json" -X POST -d @web/app/examples/resources/newproduct.json http://localhost:8000/api/products/
    [{
        "model":"products.product",
        "pk":6,
        "fields":{
            "uid":"C101",
            "description":"Switch with motion detector",
            "category":"3",
            "price":"12.95"
        }
    }]

To calculate discounts for orders:

    curl -H "Content-Type: application/json" -X POST -d @web/app/examples/resources/orders/order1.json http://localhost:8000/api/discounts/calculate/
    {"total":"49.90",
    "new_total":49.9,
    "items":[
        {
            "unit-price":4.99,
            "category":"2",
            "product-id":"B102",
            "free_products":{
                "quantity_required":5,
                "product_id":"B102",
                "to_receive":2
            },
            "total":49.9,
            "quantity":10
        }
    ],
    "customer-id":"1",
    "loyalty_discount_details":null,
    "id":"1",
    "category_discounts":[
        {
            "category_id":"2",
            "new_total":49.9,
            "cheapest_product_discount":0.0,
            "cheapest_product_discount_details":null,
            "total":49.9,
            "cheapest_product_price":4.99,
            "quantity":10
        }
    ]}


### PUT
To update an existing entry in the database, we need to pass the entry's id in the url:

    curl -H "Content-Type: application/json" -X PUT -d @web/app/examples/resources/editproduct.json http://localhost:8000/api/products/C101/
    [{
        "model":"products.product",
        "pk":6,
        "fields":{
            "uid":"C101",
            "description":"A tea pot!",
            "category":"3",
            "price":"0.01"
        }
    }]
    
### DELETE
To delete an entry from the database, we need to pass the entry's id in the url:

    curl -H "Content-Type: application/json" -X DELETE -d @web/app/examples/resources/editproduct.json http://localhost:8000/api/products/C101/ -i
    HTTP/1.1 204 No Content
    Server: nginx/1.4.6 (Ubuntu)
    Date: Sun, 23 Oct 2016 16:30:48 GMT
    Content-Type: text/html; charset=utf-8
    Connection: keep-alive
    X-Frame-Options: SAMEORIGIN

## The Author
Teapot was designed and developed by Jaime Roeland in 2016.
jaime.roeland@gmail.com
