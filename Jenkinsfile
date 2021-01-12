pipeline {
    environment {
   	 PROJECT = "spacex"
 	   APP_NAME = "spacexapi"
     BRANCH_NAME = "main"
   	 IMAGE_TAG = "janith/${PROJECT}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
                }
    agent any 
    options {
        skipStagesAfterUnstable()
            }
    stages {
	      stage('Building & Deploy Image') {
		         
              steps {
                  sh 'mkdir images'
                  sh 'cp Dockerfile images/'
                  sh 'cp manage.py images/'
                  sh 'cp requirements.txt images/'
                  sh 'cp -avr app/ images/'
                  sh 'cp .gitignore images/'
                  sh 'docker build -t ${APP_NAME} images/.'
                  sh 'docker tag ${APP_NAME} ${IMAGE_TAG}'
                  sh 'docker login -u janith -p Janith0771818404'
                  sh 'docker push ${IMAGE_TAG}'
                  sh 'docker image rm ${IMAGE_TAG}'
                  sh 'docker image rm ${APP_NAME}'
                  sh 'rm -rf images/'			
                    }
                                         }
        stage('Deploy cluster') {
              steps {
                  sh '''cat <<EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spacex-deploy
spec:
  selector:
    matchLabels:
      app: spacex-stage
      department: spacex-app
  replicas: 2
  template:
    metadata:
      labels:
        app: spacex-stage
        department: spacex-app
    spec:
      containers:
      - name: hello
        image: ${IMAGE_TAG}
        env:
        - name: "PORT"
          value: "5000"
EOF''' 
                  sh '''cat <<EOF > service.yaml 
apiVersion: v1
kind: Service
metadata:
  name: spacex-service
spec:
  type: LoadBalancer
  selector:
    app: spacex-stage
    department: spacex-app
  ports:
  - protocol: TCP
    port: 5000
    targetPort: 5000
EOF'''         
                  sh 'gcloud auth activate-service-account --key-file /var/lib/jenkins/.certificate/slwidgets-fd89f6333e67.json'
                  sh 'gcloud config set compute/zone asia-southeast1-b'
                  sh 'gcloud config set project slwidgets'
                  sh 'gcloud container clusters get-credentials standard-cluster-1 --zone asia-southeast1-b --project slwidgets'
                  sh 'export KUBECONFIG=$(pwd)/config'
                  sh 'kubectl get nodes'
                  // sh 'kubectl create ns production'
                  sh 'kubectl  apply -f deployment.yaml'
                  sh 'kubectl  apply -f service.yaml'
                    }
                                }

           }
           post {
              always {
                 mail to: 'janith2011@gmail.com',
                          subject: "Success Pipeline: ${currentBuild.fullDisplayName}",
                          body: "${PROJECT}/${APP_NAME}/${env.BRANCH_NAME}/${env.BUILD_NUMBER}"
                     }
              failure {
                    mail to: 'janith2011@gmail.com',
                          subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                          body: "Something is wrong with ${env.BUILD_URL}"
                      }
                }
        }