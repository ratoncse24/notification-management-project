## [Notification Management Project](https://github.com/ratoncse24/notification-management-project) setup guidelines

#### Prerequisites:
* Must be installed [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) in your local machine

### Follow the steps one by one
1. git clone `https://github.com/ratoncse24/notification-management-project`
2. cd `notification-management-project`
3. `docker-compose -p=nms up`
4. after successfully running docker container, follow the next steps
5. setup notifications for the website
    * go to: `http://localhost:8001/admin`
    * enter username: `admin`
    * enter password: `admin`
    * click on login button you will be redirected to dashboard area. Click on notification menu to management website notification.
6. e-commerce website view with notification 
    * go to: `http://localhost:8001`
    * if you visit first time then you will get the notification that you set on admin panel for first time visitor.
    * if you refresh the url then you will get the notification for second time visitor

### Run unit test
1. Unit test backend application 
    * open terminal inside backend project
    * create a [virtual environment](https://pypi.org/project/virtualenv/) and activate it to the terminal
    * run: `pip3 install -r requirements.txt`
    * run: `pytest`
    
2. Unit test front-end application 
    * open terminal inside front-end project
    * run: `npm install`
    * run: `npm run test:unit`
    

### Other information
1. Backend Application 
    * backend API application  url: `http://localhost:8000`
    * backend API docs url: `http://localhost:8000/docs`
    

### FAQ
1. Can't see notification ?
    * login to admin panel and set the notification poperly
    * go to this url: `http://localhost:8001`
    * clear cookie 
    * visit again to this url: `http://localhost:8001`
    
