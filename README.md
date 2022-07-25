This is https://github.com/bomonike/fullest-stack - 

This monorepo is called "fullest-stack" because we want to go beyond what the mythical "full stack" software engineer can create and manage.

It takes a team to have skill in all the tools needed to create a complete production system with these features and processes:

<a target="_blank" href="https://res.cloudinary.com/dcajqrroq/image/upload/v1658717953/fullest-stack-flow-3138x1166_fdihf8.jpg"><img width="650" alt="fullest-stack-flow" src="https://res.cloudinary.com/dcajqrroq/image/upload/v1658717953/fullest-stack-flow-3138x1166_fdihf8.jpg"></a>

We begin with the simplest set and gradually grow to that complete production-grade entity that in today's hostile internet.

1. The initial capability is a public static site generated from <strong>GitHub Markdown</strong> by Jekyll running within GitHub, based on a template.

1. The next level is using <strong>Python progams</strong> to generate GitHub Markdown code.
   The caiq-html-gen.py program generates Markeown based on a csv file in the same folder.

1. More sophisticated is Python code generating Markdown from <strong>Excel</strong> spreadsheets.

1. Data maintenance utilities written in <strong>Bash</strong> are used to maintain secrets (using <strong>Vault</strong>), to clean and to reorganize data.

1. Programs here are processed using CI/CD such as <strong>GitHub Actions</strong> (or CircleCI) processing <strong>Terraform</strong> to create resources in clouds, plus <strong>Ansible</strong> within servers.

1. When static pages need authentication and authroization to accept payment of other user-specific interaction, an app is built using <strong>React.js</strong> to provide a UI front-end (web and mobile) with a <strong>back-end</strong> providing APIs.

1. The API exposes makes use of a data store (database) to hold data specific to each user.

1. An app data cache is used to handle more scale by minimizing rewriting of data.

1. Apache Airflow for extracting and process data from databases.

1. That database needs <strong>backups</strong> to ensure quick recovery from outages and complete disasters.

1. That database stores data to be extracted and shared as csv files.

1. Logs and metrics are extracted for accumulation in <strong>Time Series</strong> and master reference databases, which <strong>Power BI</strong> displays as analytics.

1. Open-sourced <strong>Grafana</strong> is commonly used to display dashboards.

1. Violations of rules defined in the Rego language are identified by the <strong>OPA</strong> (Open Policy Agent).

1. ML (Machine Language) is used to infer actions based on data accumulated over time.
