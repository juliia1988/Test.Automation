node {

    stage("Checkout repo"){
        git branch: 'master',
        credentialsId: '11f47eab-3ab5-418b-bf2e-a8c9c6669374git',
        url: 'https://github.com/juliia1988/FracVault_autotests.git'
    }

    stage("Install deps") {
        sh 'pipenv install'
    }

    stage("Test"){
        sh 'pipenv run pytest test -sv --alluredir=allure_results'
    }

    stage("Report"){
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