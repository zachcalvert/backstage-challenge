# backstage-challenge

### Local setup
1. `git clone git@github.com:zachcalvert/backstage-challenge.git`
2. `cd backstage-challenge`
3. `python3 -m venv venv`
4. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `./manage.py migrate`
5. `./manage.py runserver`

The difference endpoint will then be available at: http://localhost:8000/api/difference?number=10

### Running the tests
1. `./manage.py test`
