### Run GPU Serverless on Iron IO

1. Docker login

``` docker login ```

2. Under iron-io directory, run Iron Function in single server mode. This command is hard to run as background process. (TODO)

``` sh function.sh ```

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



gotchas:

- ```fn call myapp /hello```
unexpected error: Get https:///apps/myapp/routes/hello: http: no Host in request URL

- ``` fn images ```
No list
```fn routes list myapp```
path	image	endpoint
/hello	iron/hello


