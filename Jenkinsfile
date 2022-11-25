pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/MaNaN-3/Jenkins_Project.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x prog1.py"
                sh "./prog1.py"
            }
        }
    stage(' Passed Test Code') {
            steps {
                sh "chmod u+x test1.py"
                sh "./test1.py"
            }
        }
    stage(' Failed Test Code') {
            steps {
                sh "chmod u+x test2.py"
                sh "./test2.py"
            }
        }
    } 
}