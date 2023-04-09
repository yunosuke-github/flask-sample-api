# flask-sample-api

Flaskで実装されてREST API

GitHub Actionを使ってCI/CDを体験する用のリポジトリ

## GitHub Action

### pytest.yml
mainブランチとmainブランチに対してプルリクエストを作成すると自動でテストが実行される

### image-build.yml
mainブランチに対してpushされ、pytestのワークフローが正常に終了するとdocker buildを実行してAmazon ECRにimageをpushする

#### 注意点

下記設定をしておかないと、Jobがエラーとなる。
- ワークフローの中でgit tagをpushしているため、Settings > Actions > General > Workflow permissionsをRead and writeにする必要がある
- GitHub ActionからAWS Resourceを操作するためのIAMを作成する
  - AmazonEC2ContainerRegistryFullAccess
  - AWSCloudFormationFullAccess
- Amazon ECRにimageをpushするため、Settings > Secrets and Variables > ActionsにGitHub Action用に作成したIAMのアクセスキーを登録する
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY

## ローカルで実行

### Image Build

```
$ docker build . -t flask-sample-api
```

### API実行

```
$ docker run -it -d flask-sample-api
```

### APIリクエスト

```
$ curl http://127.0.0.1:5000/users
> '{"id": 1, "name": "SAMPLE_01"}'
```