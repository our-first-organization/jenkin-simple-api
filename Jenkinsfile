pipeline{
    agent any

    environment{
        APP_NAME = "My Simple API"
        IMAGE_NAME = "ghcr.io/our-first-organization/simple-api-image:lastest"
        VENV_NAME = 'myenv'
		ROBOT_REPO = "https://github.com/our-first-organization/jenkin-simple-api-robot"
    }
    stages{
        stage("Setup Python Environment"){
            agent {
                label "vm2"
            }
            steps {
                sh "python3 -m venv ${VENV_NAME}"
                sh ". ${VENV_NAME}/bin/activate"
            }
        }

        stage("Install Python Dependencies for api"){
            agent {
                label "vm2"
            }
            steps {
                sh "${VENV_NAME}/bin/pip install -r req.txt"
            }
        }

        stage("Run Unit Test"){
            agent {
                label "vm2"
            }
            steps {
                sh ". ${VENV_NAME}/bin/activate && python3 -m unittest test.py"
            }
        }

        stage("Build Docker Image"){
            agent {
                label "vm2"
            }
            steps {
                sh "docker compose build"
                sh "docker ps"
            }
        }

        stage("Run Docker Container"){
            agent {
                label "vm2"
            }
            steps {
                sh "docker compose up -d"
            }
        }

        stage("Clone simple-api-robot repository"){
            agent {
                label "vm2"
            }
            steps {
                sh "rm -rf jenkin-simple-api-robot"
                sh "git clone ${ROBOT_REPO}"
            }
        }

        stage("Install Python Dependencies for robot"){
            agent {
                label "vm2"
            }
            steps {
                sh "${VENV_NAME}/bin/pip install -r jenkin-simple-api-robot/req.txt"
            }
        }

        stage("Run Robot Test"){
            agent {
                label "vm2"
            }
            steps {
                sh ". ${VENV_NAME}/bin/activate && robot jenkin-simple-api-robot/test.robot"
            }
        }

		stage("Push Docker Image") {
			agent {
				label "vm2"
			}
			steps {
				withCredentials([string(credentialsId: "GITHUB_PAT", variable: "GITHUB_TOKEN")]) {
					sh "echo ${GITHUB_TOKEN} | docker login ghcr.io -u USERNAME --password-stdin"
					sh "docker push ${IMAGE_NAME}"
					sh "docker rmi -f ${IMAGE_NAME}"
				}
			}
		}

        stage("Stop Docker Container"){
            agent {
                label "vm2"
            }
            steps {
                sh "docker compose down"
            }
        }

		stage("PreProd - Pull Image") {
			agent {
				label "vm3"
			}
			steps {
				withCredentials([string(credentialsId: "GITHUB_PAT", variable: "GITHUB_TOKEN")]) {
					sh "echo ${GITHUB_TOKEN} | docker login ghcr.io -u USERNAME --password-stdin"
					sh "docker pull ${IMAGE_NAME}"
				}
			}
		}

        stage("PreProd - Run Container from Image"){
            agent {
                label "vm3"
            }
            steps {
                sh "docker compose up -d"
            }
        }
    }

    post {
        always {
            // Clean up the virtual environment
            sh "rm -rf ${VENV_NAME}"
        }
    }
}
