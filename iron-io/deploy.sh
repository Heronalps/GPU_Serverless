# create func.yaml file, replace $USERNAME with your Docker Hub username.
fn init heronalps/hello
# build the function
fn build
# test it - you can pass data into it too by piping it in, eg: `cat hello.payload.json | fn run`
fn run
# Once it's ready, build and push it to Docker Hub
fn build && fn push
# create an app - you only do this once per app
fn apps create myapp
# create a route that maps /hello to your new function
fn routes create myapp /hello