# Red Kubes Technical Assignment

## Docker steps

1. Pull the Docker image from Docker Hub:
```
docker pull adnansh92/red-kubes:latest
```

2. Run the Docker imag passing your AWS credentials:
```
docker run -d -e AWS_ACCESS_KEY_ID="your-access-key" -e AWS_SECRET_ACCESS_KEY="your-secret-access-key" -p 5050:5050 adnansh92/red-kubes:latest
```

3. Navigate to `localhost:5050/files` to view a list of the objects you have in your S3 bucket

## Helm steps

1. Make sure you are connected to a Kubernetes cluster locally by running:
```
kubectl config get-contexts
```
If no context has been selected, run the following:
```
kubectl config use-context <your-kubernetes-cluster>
```

2. In the root of the repo run the `helm install` command to deploy the application:
```
helm install red-kubes-helm red-kubes-helm --set AWS_ACCESS_KEY_ID="your-access-key" --set AWS_SECRET_ACCESS_KEY="your-secret-access-key"
```

3. To navigate to the browser and list the S3 objects, you need to grab the pod name with this command:
```
kubectl get pods --namespace default -l "app.kubernetes.io/name=red-kubes-helm,app.kubernetes.io/instance=red-kubes-helm" -o jsonpath="{.items[0].metadata.name}"
```
After that run:
```
kubectl --namespace default port-forward $POD_NAME 5050:5050
```
You can now navigate to your browser and go to `localhost:5050/files` to view a list of the objects you have in your S3 bucket.

## Minikube steps
1. Start Minikube by running:
```
minikube start
```
2. Configure kubectl to use the Minikube cluster by running:
```
kubectl config use-context minikube
```
3. Install the Helm chart of the application by running:
```
helm install red-kubes-helm red-kubes-helm --set AWS_ACCESS_KEY_ID="your-access-key" --set AWS_SECRET_ACCESS_KEY="your-secret-access-key"
```
4. Get the URL of the service by running:
```
minikube service red-kubes-helm --url
```
5. You can now navigate to the browser by clicking on the URL
### Cleanup
1. To delete the deployment:
```
helm delete red-kubes-helm
```
2. To stop Minikube:
```
minikube stop
```

## Drone execution

When you submit the service creation required, a Drone pipeline is triggered by a change committed to Gitea from the console change you made. This pipeline applies the changes in the service in order to deploy it. In the case of creating a service, the resources responsible for exposing the service is through Istio that is tied to the namespace of your team.