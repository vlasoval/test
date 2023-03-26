## Description
The test project for IT Bootcamp implementing the requirements from https://docs.google.com/forms/d/e/1FAIpQLSdv_AzaXuggJZhlYKd2IOMBrYjc1P0o9f-iHGjIJ_Y5WhiVGg/viewform
The project is implemented using Django Rest Framework and have the following API:
- /api/book/
    - GET
    - POST
    - PUT
    - DELETE
- /api/author/
    - GET
    - POST
    - PUT
    - DELETE


### Pre-requirements
- Python >= 3.9
- pip  

### How to get the project ready to run?
- Clone the project from Github `git clone https://github.com/vlasoval/test.git`
- Go to the project folder
- Install python Virtual Environment library (if not yet) `pip install virtualenv`
- Create Virtual Environment `virtualenv env`
- Activate the environment `source env/bin/activate`
- Install python libraries needed to run the project `pip install -r requirements.txt`

### How to run the project?
- Go to the project folder + `src`
- Execute command `python manage.py runserver`
- Go to the `http://127.0.0.1:8000/api` to see the the API

## Note
- To see the response in JSON format append to the url the follow query param `?format=json`