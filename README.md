# fastapi-jwt-tester
This is a simple project to demonstrate how to test FastAPI endpoints that require JWT authentication.
In this project, singleton is used to store users data. You can use your own database.


## Installation
    
    ```shell
    $ git clone this response
    $ cd fastapi-jwt-tester
    $ pip install -r requirements.txt
    ```

## Pytest
    
    ```shell
    $ pytest
    ```

## Run the app
        
    ```shell
    $ uvicorn main:app --reload
    ```

### Ref
- https://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/
- https://www.dataquest.io/blog/unit-tests-python/
