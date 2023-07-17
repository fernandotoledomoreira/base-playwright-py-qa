pipeline {
  agent {
    docker {
      image "${params.playwright_py_docker_image}"
      args '-v /var/jenkins_home:/var/jenkins_home -v /var/lib/jenkins:/var/lib/jenkins'
    }
  }
  parameters {
    string(
      name: 'playwright_py_docker_image',
      defaultValue:'758526784474.dkr.ecr.us-east-1.amazonaws.com/base-playwright-py-qa:develop',
      description: 'The cucumber docker image'
    )
    string(
      name: 'config_vars',
      defaultValue:'cdt_dev',
      description: 'Where you set config vars'
    )
    string(
      name: 'command_run',
      defaultValue:'pytest -n auto',
      description: 'Where you set cucumber tag'
    )
    string(
      name: 'env',
      defaultValue:'dev',
      description: 'Where you set environment (dev|hml|prd|dr)'
    )
    string(
      name: 'file_var',
      defaultValue:'qa',
      description: 'Where you set file to read environment'
    )
  }
    stages {
      stage('CLEANING WORKDIR') {
         steps {
             deleteDir()
         }
      }
      stage('RUNNING PLAYWRIGHT TESTS') {
        steps {
          catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
            slackSend(channel: "#reports-cucumber-tests", color: '#FFFF00', message: "Tests Started \n Command Run: ${params.command_run} \n Image: ${params.playwright_py_docker_image} \n Build Number: ${BUILD_NUMBER} \n Pipeline: ${JOB_NAME} \n Build Console: ${BUILD_URL}console")
            configFileProvider([configFile(fileId: "${params.file_var}", variable:"${params.file_var}")]) {
              wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'xterm']) {
                sh "cd /base-playwright-py-qa && . \$${params.file_var} >> /dev/null && ${params.command_run}"
              }
            }
          }
        }
      }
    }
    post {
      always{
      echo "TESTS FINISHED"
        sh 'cd /base-playwright-py-qa/reports && zip allure-results allure-results/*'
        sh 'cp /base-playwright-py-qa/reports/allure-results.zip ${WORKSPACE}/'
        sh 'cd /base-playwright-py-qa/reports && rm -R allure-results.zip'
        sh 'cd ${WORKSPACE} && unzip allure-results.zip'
        sh 'cd ${WORKSPACE} && rm -R allure-results.zip'
         allure([
          includeProperties: true,
          jdk: '',
          reportBuildPolicy: 'ALWAYS',
          results: [[path: 'allure-results']]
        ])
        sh 'mkdir allure-report-${JOB_NAME}-${BUILD_NUMBER}'
        sh 'cp ../../jobs/${JOB_NAME}/builds/${BUILD_NUMBER}/archive/allure-report.zip allure-report-${JOB_NAME}-${BUILD_NUMBER}'
        sh 'cd allure-report-${JOB_NAME}-${BUILD_NUMBER} && unzip allure-report.zip'
        sh "aws s3 cp allure-report-${JOB_NAME}-${BUILD_NUMBER}/allure-report s3://report-tests/${JOB_NAME}/${params.env}/${BUILD_NUMBER} --recursive"
        script {
          if ("${currentBuild.result}" == "SUCCESS") {
             sh 'cd /base-playwright-py-qa && python3 slack/slack_finish_testes_notify.py'
             slackSend(channel: "#reports-cucumber-tests", color: "#00FF00", message: "Tests Finished \n Command Run: ${params.command_run} \n Build Number: ${BUILD_NUMBER} \n Pipeline: ${JOB_NAME} \n Report Link: https://report-tests.devtools.caradhras.io/${JOB_NAME}/${params.env}/${BUILD_NUMBER}/index.html \n Pipeline Results: ${currentBuild.result}")
        } else if ("${currentBuild.result}" == "UNSTABLE") {
             sh 'cd /base-playwright-py-qa && python3 slack/slack_finish_testes_notify.py'
            slackSend(channel: "#reports-cucumber-tests", color: "#FF0000", message: "Tests Finished \n Command Run: ${params.command_run} \n Build Number: ${BUILD_NUMBER} \n Pipeline: ${JOB_NAME} \n Report Link: https://report-tests.devtools.caradhras.io/${JOB_NAME}/${params.env}/${BUILD_NUMBER}/index.html \n Pipeline Results: ${currentBuild.result}")
        } else {
             sh 'cd /base-playwright-py-qa && python3 slack/slack_finish_testes_notify.py'
            slackSend(channel: "#reports-cucumber-tests", color: "", message: "Problem Tests \n Command Run: ${params.command_run} \n Build Number: ${BUILD_NUMBER} \n Pipeline: ${JOB_NAME} \n Report Link: https://report-tests.devtools.caradhras.io/${JOB_NAME}/${params.env}/${BUILD_NUMBER}/index.html \n Pipeline Results: ${currentBuild.result}")
        }
        }
      }
    }
  }