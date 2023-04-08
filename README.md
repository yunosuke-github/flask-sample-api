# flask-sample-api

Flaskで実装されてREST API

GitHub Actionを使ってCI/CDを体験する用のリポジトリ

## GitHub Action

### pytest.yml
mainブランチとmainブランチに対してプルリクエストを作成すると自動でテストが実行される

### image-build.yml
mainブランチに対してpushされ、pytestのワークフローが正常に終了するとdocker buildを実行してDockerHubにimageをpushする

#### 注意点

下記設定をしておかないと、Jobがエラーとなる。
- ワークフローの中でgit tagをpushしているため、Settings > Actions > General > Workflow permissionsをRead and writeにする必要がある
- DockerHubにimageをpushするため、Settings > Secrets and Variables > Actionsに下記Secretを登録する必要がある
  - DOCKER_USERNAME: DockerHubのユーザー名
  - DOCKER_PASSWORD: DockerHubのログインパスワード

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