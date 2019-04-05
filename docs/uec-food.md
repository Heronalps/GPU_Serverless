### On Iron Functions

1. Build

``` cd iron-io/uec_food_func ```
``` fn build <Docker_Username>/<Image_name>:<Version> ```

2. Run blur filter function

``` fn run ```

3. Push image to Docker Hub

```docker login```
```fn push```

- docker test command:

``` docker run --rm --runtime=nvidia -it -v "$PWD":/img-filter -w /img-filter izone/pycuda /bin/bash ```


### On Nautilus (kubeless)

