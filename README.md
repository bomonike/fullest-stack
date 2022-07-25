This is https://github.com/bomonike/fullest-stack - 

This monorepo is called "fullest-stack" because we want to go beyond what the mythical "full stack" software engineer can create and manage.

It takes a team to have skill in all the tools needed to create a complete production system with these features and processes:

<a target="_blank" href="https://res.cloudinary.com/dcajqrroq/image/upload/v1658751641/fullest-stack-flow-3084x1158_c69cqu.jpg"><img width="650" alt="fullest-stack" src="https://res.cloudinary.com/dcajqrroq/image/upload/v1658751641/fullest-stack-flow-3084x1158_c69cqu.jpg"></a>

We begin with the simplest capability set and gradually mature to that full production-grade system needed in today's hostile internet.
<strong>Join us!</strong>

1. The initial capability is a website of <strong>static pages</strong> hosted on github.io

1. A CDN (Content Distribution Network) is used to host binary images and other binary files. <strong>Cloudinary</strong> also provides automated resizing needed for different size screens.

1. The static HTML is created from text coded in Markdown format by Jekyll running within GitHub, based on its template CSS and JavaScript.

   (Next.js does the same for sites coded in React.js.)

1. The next level is using <strong>Python programs</strong> to generate GitHub Markdown code from "flat" (csv text) files containing data.

   The caiq-html-gen.py program generates Markeown based on a csv file in the same folder.

1. More sophisticated is Python code generating Markdown from <strong>Excel</strong> spreadsheets which can be structured as an Excel form for data entry.

1. Data maintenance in the <strong>(Azure) cloud</strong> is done by shell script (written in <strong>Bash</strong>, Python, Go) invoking Terraform to establish <strong>Vault</strong> for maintaining secrets.

   Bash is run on Windows through WSL (Windows System for Linux).

1. Processing is made repeatable by automation using CI/CD (<strong>GitHub Actions</strong> or CircleCI) processing <strong>Terraform</strong> to create resources in clouds, plus <strong>Ansible</strong> within servers.

1. When static pages need user-specific interaction such as authentication and authorization to accept payments, an app is built using <strong>React.js</strong> to provide a UI front-end (web and mobile) with a <strong>back-end</strong> providing APIs.

1. To persist data, a data store (database). A graph database provides more flexibility.

1. That database needs <strong>backups</strong> to ensure quick recovery from outages and complete disasters.

1. A <strong>data cache</strong> is used to handle more scale by minimizing transfer of the same data.

1. Logs and Metrics are collected for troubleshooting and security forensics.

1. Logs and metrics are accumulated in <strong>Time Series</strong> and master reference databases by <strong>Prometheus</strong>.

   There is also open-source Prometheus on Linux.


1. A utility (<strong>Apache Airflow</strong>) for extracting and process data from databases.

1. That database stores data to be extracted and shared as csv files.

1. Open-sourced <strong>PowerBI</strong> is commonly used to display dashboards. <a target="_blank" href="https://www.youtube.com/watch?v=dTc4OGbt80w">VID</a>

   There is also open-source Grafana on Linux.

1. Violations of <strong>rules</strong> defined in the Rego language are identified by the <strong>OPA</strong> (Open Policy Agent).

1. ML (Machine Language) is used to infer actions and rules based on data accumulated over time to generate alerts and answers into databases, saving users time.

1. NLP (Natural Language Processing) generates text, speech, images, and videos.

   OpenCV is the AI working on images.