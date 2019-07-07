8---
# DOCKER CONTAINER FOR FLASK APP
---

In a nutshell, docker container lets you run your app in any machine irrespective of it's OS or configuration and avoids independancy trap.

---
## STEPS:

In Docker Image:

    - Install python3
    - Install pip3
    - Copy Source code of FlaskApp
    - Install Python Modules
    - Expose Port
    - Make Container Executable

---
## 1. Create a new docker image

**Create 'Dockerfile' with the following code:**

```
from alpine:latest

RUN apk add --no-cache python3-dev \
   && pip3 install --upgrade pip
```

- **FROM** command is used to fetch base docker image
- **RUN** command runs a command inside image 
- **apk** is package manager for 'alpine' system


**In Terminal:**

```
docker build -t myapp:latest .
```

- Docker build -t <new-image-name>
- .(dot) notation will find Dockerfile in current folder
   
_(NOTE: After entering the above command all the contents fill be detched and installed)_

----
## 3. View created Docker Image

**In Terminal:**
```
docker images
```

- Above command will list all available images. In our case, the two images will be displayed:
      - myapp
      - alpine
      
---
## 4. Run the image and create container

**In Terminal:**

```
docker run -it flaskapp /bin/sh
```

- docker run -it <image-name> /bin/sh 
- By entering above command you will be taken into container there you can  execute 'python3' or 'pip' to get their info
- To exit the container, enter ```exit```
- you can see if the container running or not by entering ```docker ps``` in another tab
   
---
## 5. Copy source code of flask app

**Modify the Dockerfile**

```
from alpine:latest

RUN apk add --no-cache python3-dev \
   && pip3 install --upgrade pip

WORKDIR /workspace

COPY . /workspace

RUN pip3 --no--cache-dir install -r requirements.txt
```

- ```WORKDIR /workspace``` will create a directory named 'workspace' in container, where we will be working
- ```COPY . /workspace``` copys all files from current dir to workspace dir
- ```RUN pip3 --no--cache-dir install -r requirements.txt``` will install all modules specified in ```requirements.txt```

**In Terminal: (Create Docker Image Again)**

```
docker build -t flaskapp:latest .
```
[ IF YOU DIDNOTCHANGE THE PREVIOUS LINES IN ```Dockerfile```, THOSE LINES WILL NOT RUN!! ]4

- docker build -t <image-name:version> .
- As we had ```latest```tag, the previous image will be overwritten. You can verify this by ```docker images```

---
## 6. Expose the port

**Modify Dockerfile:**
```
from alpine:latest

RUN apk add --no-cache python3-dev \
   && pip3 install --upgrade pip

WORKDIR /workspace

COPY . /workspace

RUN pip3 --no--cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ['python3']
CMD ['app.py']

```

- Port 5000 will be exposed to localhost
- **ENTRYPOINT** Makes the container executable.
      - ENTRYPOINT ['<what-we-want-to-run>']
      - CMD ['arg1-for-what-we-want-to-run'. 'arg2-for-what-we-want-to-run', ...]

**Build the image**

```
docker build -t flaskapp:latest .
```

- View the created images using ```docker images```

---
# 7. Create container from it: 

```docker run -it flaskapp```

- Add daemon port flags to expose the port

```docker run -it -d -p 5000:5000 flaskapp```

- docker run -it flaskapp -d -p <localhost-port>:<Dockerfile-port> flaskapp
   
---

# 8. Stop Docker container:

```docker stop <container-id>```

---
