# B-Onion-TopicDemo

## Instructions to Follow Demo
**NOTE:** all of the files I will be making for the demo will be held in */basic_demo* 

## Setup work

If you haven't downloaded gcloud and authenticated use:
  - [Install GCloud CLI](https://cloud.google.com/sdk/docs/install)
  - [link to authenticate docker](https://cloud.google.com/container-registry/docs/advanced-authentication#linux)

### You can follow these steps to get this setup

**First, go to google's platform and search, container registry API. Once there enable the API**

~~~
  sudo apt-get install apt-transport-https ca-certificates gnupg
~~~
Add the gcloud CLI distribution URI as a package source.
~~~
  echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
~~~
Import the Google Cloud public key.
~~~
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
~~~
Install the CLI 
~~~
sudo apt-get update && sudo apt-get install google-cloud-cli
~~~

#### Authenticate Docker
~~~
gcloud auth login
~~~
~~~
gcloud auth configure-docker
~~~

### Make Basic Flask App

### Google Container Registry
1. Find hostname for repo, should be gcr.io given our location.

1. Choose target image name, this can be different to an images local name

1. Combine into format *Hostname*/*Project_ID*/*target_img* you will use this when tagging your local image using the format 

~~~
docker build -t HOSTNAME/PROJECT-ID/TARGET-IMAGE:TAG .
~~~

- **HOSTNAME** is the registry host you chose in step 2.
- **PROJECT** is the Google Cloud project ID.
- **TARGET-IMAGE** is the name for the image when it's stored in Container Registry.
- **TAG** is the tag you want to associate with this image version.


4. Ensure that you have authentication to push your container and a repository to push to. 

5. Push the tagged image using 
~~~
docker push HOSTNAME/PROJECT-ID/IMAGE:TAG
~~~

### Getting Cloud Run set up
1. go to google cloud console cloud run

2. Create a service, make sure to 
  - select the image url you just pushed
  - set the port to the port which you defined in the app (8000)

