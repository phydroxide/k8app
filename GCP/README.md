# Jenkins on GCP

Based on https://www.cloudskillsboost.google/focuses/1776?parent=catalog




# Custom CLI Tools

For BYUI/Ensign Pathways IT 360 I created a docker container that could be used on a student's computer rather than having to rely on Cloud Run or any requirement to install a bunch of tools:

[Alternate CLI Container Image](https://github.com/phydroxide/ensign/tree/main/8_Lab9_Terraform#alternate-cli) 

```
docker run -it --privileged -v /Users/phydroxide/cloudsdk:/home/cloudsdk -v /var/run/docker.sock:/var/run/docker.sock mycli /bin/bash
```

## GCP Setup

First we need to do an initial setup of the GCP Project:

### Login
Login to GCP with gcloud's CLI

```
gcloud auth login
```
Then paste the authentication challenge in the cli. 


### Create GCP Project

I found it is easiest to support students by telling them to create a new project for the assignment, and if things go south, we can nuke it and try again.
```
gcloud projects create ensign-jenkins --name ensign-jenkins 
```

They'll need to enable the compute API. 
```
gcloud services enable compute.googleapis.com
```

Now you can set the compute region and zone
```
gcloud config set compute/region us-central1
```

```
gcloud config set compute/zone us-central1-a
```

### Create Kubernetes Cluster

First enable the container API 
```
gcloud services enable container.googleapis.com
```

Now Create the cluster
```
gcloud container clusters create jenkins-cd \
--num-nodes 2 \
--scopes "https://www.googleapis.com/auth/projecthosting,cloud-platform"
```

Verify Cluster is built:
```
gcloud container clusters list
```

gcloud's cli will automatically create the cluster and put credentials in ~/.kube/config. 
If the session expires, or you need to login from elsewhere to manage the cluster you'll need to generate credentials:

```
gcloud container clusters get-credentials jenkins-cd
```

This will use the Google credentials to get the kubernetes credential and save to ~/.kube/config

