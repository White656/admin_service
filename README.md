### How to run project?

```shell
$ docker-compose -f docker-compose.dev.yml up -d --build
```

Before running project open [localhost](http://localhost/admin) admin panel from checking service.

If you have empty database running:

```shell
$ docker-compose -f docker-compose.database_script.yml up -d
```

This script upload in database random 100M values in all tables.

|       release       | v1  | v2  | v3  |
|:-------------------:|:---:|:---:|:---:|
|        nginx        |  ❌  |  ❌  |  ❔  |
| optimized db query  |  ❌  |  ✅  |  ✅  |
|     admin panel     |  ✅  |  ✅  |  ✅  |
| sqlite to pg loader |  ❌  |  ❌  |  ❔  |
|  random db loader   |  ❌  |  ✅  |  ✅  |
|   docker-compose    |  ❌  |  ✅  |  ✅  |
|     write tests     |  ❌  |  ❌  |  ❔  |

### Team:

[White656](https://github.com/White656) - Developer