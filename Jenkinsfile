node {

        stage("Checkout repo"){
            git branch: 'master',
            credentialsId: '7957cba0-a39c-4aae-8619-26b66d94da30',
            url: 'https://github.com/juliia1988/Test.Automation'
        }

        stage("Install deps") {
            sh 'pipenv install'
        }

        stage('Test STAGE APIs') {
            sh 'pipenv run pytest STAGE_test_API -sv --alluredir=allure_results'
        }

        stage('Test STAGE ETL') {
            sh 'pipenv run pytest STAGE_test_ETL -sv --alluredir=allure_results'
        }

        stage('Test STAGE PJR') {
            sh 'pipenv run pytest STAGE_test_PJR -sv --alluredir=allure_results'
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
