# Hello World Docker Compose
This is a sample application shows how to run a hello world application and expose it through Nginx using a simple docker-compose file.

## Pre-requesties
- add the record ``127.0.0.1 helloworld.com`` to `/etc/hosts` file on your system.
- Port `80` and `3030` should not be allocated to any application.
- `Docker` and `Docker-compose` should be installed on the system.

## How to run the Application
Clone the git repository  
```
git clone https://github.com/mohamedfazrin/helloworld.git/
```  

Get in to the directory  
```
cd helloworld
```

Run the application  
```
docker-compose up -d
```  
>**Note**
> `-d` is used to run the application in background  <br/>  
<br/>


To check the containers running  
```
docker-compose ps
```

Access the application using:  
http://helloworld.com  
<br/>
To stop the application  
```
docker-compose down
```  
