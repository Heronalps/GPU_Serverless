### Run GPU Serverless on Iron IO

1. Docker login

``` docker login ```

2. In another terminal (process) under iron-io directory, run Iron Function in single server mode. This command is hard to run as background process. (TODO)

``` sh server.sh ```

3. Create app and routes

``` fn apps create <app-name> ```
```  fn routes create <app-name> /<app-name> ```

4. Call the function

``` curl http://localhost:8080/r/myapp/hello ```

5. List images

```fn routes list <app-name>```
path	image	endpoint
/hello	iron/hello

6. Run function - this command will spawn a container and serve the request, not from the above singe-mode server.

```fn run <image-name>```
Hello World!

```fn run ```
Image name can be ignored if executing in function's directory. In this sense, ```fn run``` is essentially ```docker run --rm```

7. Put a Dockerfile in the directory of func.xx if it's required


gotchas:

- ```fn call myapp /hello```
unexpected error: Get https:///apps/myapp/routes/hello: http: no Host in request URL

- ``` fn images ```
No list
```fn routes list myapp```
path	image	endpoint
/hello	iron/hello

Iron function use ``` docker images ``` to build apps. The default image is ```iron/<path>```


- ``` fn init -f --runtime python heronalps/hello ```
runtime needs whole name (python, ruby, golang)

- ``` sh server.sh ```
You have to run ``` docker rm functions ``` every time restart a single mode server