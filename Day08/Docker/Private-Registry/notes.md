# Private Docker Registry

## Overview

In this lab, I built a secure Private Docker Registry to centrally store and distribute Docker images. The registry was configured with HTTPS using a self-signed TLS certificate and protected with Basic Authentication via `htpasswd`.

## Objectives

* Build a Docker image for a Flask application.
* Deploy a Private Docker Registry.
* Enable HTTPS with a self-signed certificate.
* Configure Basic Authentication.
* Push and pull Docker images securely.
* Understand the complete Docker image distribution workflow.

## Implementation

The following tasks were completed:

* Built a Flask Docker image using a custom Dockerfile.
* Generated authentication credentials using `htpasswd`.
* Created a self-signed TLS certificate with OpenSSL.
* Started the Docker Registry container with:

  * HTTPS enabled
  * Basic Authentication enabled
  * Persistent storage using bind mounts
* Configured Docker to trust the local registry.
* Tagged the local image with the registry address.
* Logged into the registry and successfully pushed the image.
* Verified that the image could be pulled from the private registry.

## Key Commands

* `docker build`
* `docker tag`
* `docker login`
* `docker push`
* `docker pull`
* `docker inspect`
* `docker logs`

## Outcome

The private registry was successfully deployed and secured with TLS encryption and authentication. Docker images can now be stored, versioned, and shared through the local registry instead of relying on Docker Hub.
