GETTING STARTED
- cd into the \test_site\ directory of the project and ``` run pip install -r requirements.txt ```
- Run the server using  ```python manage.py runserver ```
- open http://127.0.0.1:8000/ in the browser to be redirected to the login page where a new user can be created.
- To view and delete bids, open http://127.0.0.1:8000/view-bids/
- To create bids, open http://127.0.0.1:8000/create-bid/

TESTING
- To run the tests use the command ``` python manage.py test bidding_app ``` from the \test-site\ directory
