pipeline {
    environment {
   	 PROJECT = "spacex"
 	   APP_NAME = "spacexapi"
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
                  sh 'sudo docker build -t ${APP_NAME} images/.'
                  sh 'sudo docker tag ${APP_NAME} ${IMAGE_TAG}'
                  sh 'sudo docker login -u janith -p Janith0771818404'
                  sh 'sudo docker push ${IMAGE_TAG}'
                  sh 'sudo docker image rm ${IMAGE_TAG}'
                  sh 'sudo docker image rm ${APP_NAME}'
                  sh 'rm -rf images/'			
                    }
                                         }
        stage('Deploy cluster') {
              steps {
                  sh '''cat <<EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-deploy
spec:
  selector:
    matchLabels:
      app: python-stage
      department: python-app
  replicas: 2
  template:
    metadata:
      labels:
        app: python-stage
        department: python-app
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
  name: data-m-catalogue-mongo-service
spec:
  type: LoadBalancer
  selector:
    app: python-stage
    department: python-app
  ports:
  - protocol: TCP
    port: 5000
    targetPort: 5000
EOF'''         
                  sh 'gcloud auth activate-service-account --key-file /root/.m2/dmpipelinedevelopment-f9412485c45a.json'
                  sh 'gcloud config set compute/zone asia-southeast1-c'
                  sh 'gcloud config set project dmpipelinedevelopment'
                  sh 'gcloud container clusters get-credentials standard-cluster-1 --zone asia-southeast1-c --project dmpipelinedevelopment'
                  sh 'export KUBECONFIG=$(pwd)/config'
                  sh 'kubectl get nodes'
                  // sh 'kubectl create ns production'
                  sh 'kubectl  apply -f deployment.yaml'
                  sh 'kubectl  apply -f service.yaml'
                  sh 'kubectl  get service data-m-catalogue-mongo-service'
                    }
                                }

           }
           post {
              always {
                 mail to: 'janith.algewatta@inovaitsys.com',
                          subject: "Success Pipeline: ${currentBuild.fullDisplayName}",
                          body: "${PROJECT}/${APP_NAME}/${env.BRANCH_NAME}/${env.BUILD_NUMBER}"
                     }
              failure {
                    mail to: 'ravi.aluthge@inovaitsys.com',
                          subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                          body: "Something is wrong with ${env.BUILD_URL}"
                      }
                }
        }