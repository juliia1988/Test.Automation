node {

    stage("Checkout repo"){
        git branch: 'master',
        credentialsId: '428de68c-b0a5-460b-a6e2-90468ccfe967',
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