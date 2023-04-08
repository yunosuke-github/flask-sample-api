# flask-sample-api

Flaskで実装されてREST API

GitHub Actionを使ってCI/CDを体験する用のリポジトリ

## GitHub Action

下記ymlファイルにより、mainブランチとmainブランチに対してプルリクエストを作成すると自動でテストが実行される

```
.github/workflows/pytest.yml
```

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