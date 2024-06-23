# Flask Weather App
From https://github.com/jkaethee/Flask-Weather-App

This is a sample solution for Week 9 of BYU-Idaho / Ensign Pathways IT 360.

The assignment was to deploy an application on Kubernetes and publish it to Github.

For grading, I'm looking for three distinct components:

1) Develop an application into a container. 

Some students are using a sample container with zero modifications. 
This doesn't achieve the expectations of the class in that the labs are to stand as an example, and students are meant to extrapolate from that example and build their own application. 
Part of the course is to show that you can create an application, dockerize it, and then host it with Kubernetes. Developing something is the first step.
I used a sample application, but made a few modifications: 

* I registered for my own API key and included it in my solution
* I pre-loaded cities of interest into the sqllite database packaged in my container
* I created a docker file that is loaded with tools I use to troubleshoot from within the container (This would not be the case for a production container, you'd want to reduce the software footprint as much as possible, but the point is to showcase it is your own.)
* Just for fun if you visit http://<GOOGLE_LOADBALANCER_IP>/server it'll tell you the weather in the vicinity of the server by looking up the IP in a city database

Students should either write their own application using a sample application as a model, or make their own modifications to a sample application and repackage it to their own artifact registry.
 
2) Expose that application to the Internet with Kubernetes.

Yes, I've seen some students apply orchestrations to Kubernetes, but did not expose the port to the Internet. Because the lab didn't. 
We've learned how to do this! You should be doing it!

3) Push app, container code, and Kubernetes orchestrations to Github 

Just as you see here. Providing documentation in a README.md is a best practice for development projects such as this. 
You should include one.

```
docker pull us-central1-docker.pkg.dev/ensign-421602/ensign-public/weather:v1
```

```
docker run -p 5555:5555 us-central1-docker.pkg.dev/ensign-421602/ensign-public/weather:v1
```

Docker will host my container on your machine here: http://localhost:5555/

