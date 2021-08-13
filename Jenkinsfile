node {

        stage("Checkout repo"){
            git branch: 'master',
            credentialsId: '7957cba0-a39c-4aae-8619-26b66d94da30',
            url: 'https://github.com/juliia1988/FracVault_autotests.git'
        }

        stage("Install deps") {
            sh 'pipenv install'
        }

        stage('Test APIs') {
            sh 'pipenv run pytest test_APIs -sv --alluredir=allure_results'
        }

        stage('Test ETL') {
            sh 'pipenv run pytest test_ETL -sv --alluredir=allure_results'
        }

        stage("Report"){
            script {
                allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure_results']]
                ])
                }
            }
}
