---
title: Github主页配置
date: 2025-07-24 15:42:56
tags:
 - Github
 - WakaTime
categories:
 - 技术
---

仓库地址:
[metrics](https://github.com/lowlighter/metrics),[WakaTime配置](https://github.com/anmol098/waka-readme-stats)

关键词: Github自定义主页、waka-readme-stats

Readme配置:

```markdown
## Hi there 👋

<p align="left">
  <!--START_SECTION:waka-->
  <!--END_SECTION:waka-->
</p>

```

Workflows配置:

actions --> new workflow

```markdown
name: Metrics

on:
    workflow_dispatch:
    schedule:
        - cron: '0 0 * * *'

jobs:
    github-metrics:
        runs-on: ubuntu-latest
        environment:
            name: production
        permissions:
            contents: write
        steps:
            - name: Waka Readme
              uses: anmol098/waka-readme-stats@master
              with:
                  WAKATIME_API_KEY: ${{ secrets.WAKATIME_TOKEN }}
                  GH_TOKEN: ${{ secrets.METRICS_TOKEN }}
                  COMMIT_USERNAME: 'kaleus'
                  COMMIT_EMAIL: '84889222+Aspirai@users.noreply.github.com'
                  SHOW_UPDATED_DATE: 'True'
                  SHOW_PROFILE_VIEWS: 'False'
                  SHOW_COMMIT: 'False'
                  SHOW_DAYS_OF_WEEK: 'False'
                  SHOW_SHORT_INFO: 'False'
                  SHOW_LOC_CHART: 'False'
```

