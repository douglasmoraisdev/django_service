node {

        def projectImage

        stage('Checkout') {

                checkout scm
               
                def nameRegex = scm.userRemoteConfigs.url[0] =~ /^(https|git)(:\/\/|@)([^\/:]+)[\/:]([^\/:]+)\/(.+).git$/;
                NAME = nameRegex[0][5]
        }

        stage('Configure') {

            sh "echo branch name: ${env.BRANCH_NAME}"

            // build prod stage if is git TAG 
            if (env.TAG_NAME){
                BUILD_ENV = 'prod'
            }else{
                BUILD_ENV = env.BRANCH_NAME
            }

            SERVICE_NAME = "$NAME"
            DOCKER_REPO = "${env.AWS_ACCOUNT_ID}.dkr.ecr.${env.AWS_DEFAULT_REGION}.amazonaws.com"
            LAMBDA_FUNCTION = "$SERVICE_NAME"+"_function"
            DOCKER_ECR_LOGIN = sh(returnStdout: true, script: "aws ecr get-login-password --region ${env.AWS_DEFAULT_REGION}").trim()
            
            configFileProvider(
                [configFile(fileId: "$BUILD_ENV"+"_envfile", variable: 'JSON_FILE')]) {
                    
                    def jsonObj = readJSON file: "$JSON_FILE"
                    
                    STAGE = "${jsonObj.STAGE}"
                    CLUSTER_URL = "${jsonObj.CLUSTER_URL}"
                    DATABASE_URL = "${jsonObj.DATABASE_URL}"

                    BUILD_ID = "${env.BUILD_ID}"
                    LAMBDA_TASK_ROOT = "$BUILD_ENV"

            }

        }

        stage('Pre Build') {
                
            projectImage = docker.build("$SERVICE_NAME:${env.BUILD_ID}", 
                                        "--build-arg STAGE=$STAGE \
                                         --build-arg CLUSTER_URL=$CLUSTER_URL \
                                         --build-arg BUILD_ID=$BUILD_ID \
                                         --build-arg DATABASE_URL=$DATABASE_URL \
                                         --build-arg LAMBDA_TASK_ROOT=$LAMBDA_TASK_ROOT .")

        }

        /*
        stage('Test') {

            projectImage.inside {
                sh 'pytest'
            }

        }
        */

        stage('Publish'){

            sh "docker login --username AWS --password $DOCKER_ECR_LOGIN $DOCKER_REPO"

            sh "docker tag $SERVICE_NAME:${env.BUILD_ID} $SERVICE_NAME:latest"

            sh "docker tag $SERVICE_NAME:latest $DOCKER_REPO/$SERVICE_NAME:latest"
            sh "docker push $DOCKER_REPO/$SERVICE_NAME:latest"

        }

        stage('Update Lambda'){

            sh "echo publishing on $BUILD_ENV"

            //Update $LATEST lambda version
            sh "aws --region=${env.AWS_DEFAULT_REGION} lambda update-function-code --function-name $LAMBDA_FUNCTION --image-uri $DOCKER_REPO/$SERVICE_NAME:latest"

            sh "aws --region=${env.AWS_DEFAULT_REGION} lambda wait function-updated --function-name $LAMBDA_FUNCTION"

            def lambda_return = sh(returnStdout: true, script: "aws lambda publish-version --function-name $LAMBDA_FUNCTION --description build_${env.BUILD_ID}_$BUILD_ENV").trim()

            def lambdaJson = readJSON text: lambda_return

            def newVersion = lambdaJson.Version

            sh "aws --region=${env.AWS_DEFAULT_REGION} lambda update-alias --function-name $LAMBDA_FUNCTION --name $BUILD_ENV --function-version "+newVersion

        }

        stage('Clear'){
            sh "docker rmi $SERVICE_NAME:${env.BUILD_ID}"
            sh "docker rmi $DOCKER_REPO/$SERVICE_NAME:latest"

        }

        stage('Heath Check'){

            sh "curl -sf '$CLUSTER_URL/$STAGE/$SERVICE_NAME/health' >/dev/null"

        }



}
