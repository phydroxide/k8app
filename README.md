# Ensign 9.2 Develop and Deply a Web App


I used my cli toolkit container instead of GCloud Web Console

```
docker run -it --privileged \
  -v /Users/phydroxide/cloudsdk:/home/cloudsdk \
  -v /var/run/docker.sock:/var/run/docker.sock \
  us-central1-docker.pkg.dev/ensign-421602/ensign-public/ensign-cli:smaller \
  /bin/bash
``` 

## GCP Setup for Kubernetes Cluster

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
gcloud projects create ensign --name ensign 
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
gcloud container clusters create mycluster \
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
gcloud container clusters get-credentials mycluster 
```

This will use the Google credentials to get the kubernetes credential and save to ~/.kube/config

Once again, you can verify you're connected and authorized by requesting cluster-info
```
kubectl cluster-info
```

## Deploy Orchestrations to Kubernetes

Login to Google Cloud

```
gcloud auth login
```

Set project and zone

```
gcloud set project ensign
```

```
gcloud set compute/zone us-central1-a
```

Get Kubernetes Cluster credentials from gcloud cli

```
gcloud container clusters get-credentials mycluster
```

Apply Orchestrations

```
kubectl apply -f weather-deployment.yaml
```

```
kubectl apply -f weather-service.yaml
```

Find site URL to visit by waiting for IP to provision

```
kubectl get services
``` 

weather-service   LoadBalancer   34.118.237.37   <pending>     80:32469/TCP   27s
