This is https://github.com/bomonike/fullest-stack - 

This monorepo is called "fullest-stack" because we want to go beyond what the mythical "full stack" software engineer can create and manage.

It takes a team to have skill in all the tools needed to create a complete production system with these features and processes:

<a target="_blank" href="https://res.cloudinary.com/dcajqrroq/image/upload/v1658950646/fullest-stack-flow-1692x621_mj7lax.jpg"><img width="750" alt="fullest-stack" src="https://res.cloudinary.com/dcajqrroq/image/upload/v1658950646/fullest-stack-flow-1692x621_mj7lax.jpg"></a>

We begin with the <strong>simplest</strong> capability set and gradually mature over time to that full production-grade system we call "Fullest-stack" needed today.
<strong>Join us!</strong>

1. The initial capability uses a <strong>site generator</strong>. There are many available, but <strong>Jekyll</strong> that runs in GitHub.com. It works by taking applying its template CSS and JavaScript to 

1. Text files writtin in <strong>GitHub Markdown</strong> format and transforms them to 

1. <strong>static web pages</strong> hosted on a subdomain of github.io managed by GitHub.

1. Binary image files and other binary files are uploaded to a <strong>CDN</strong> (Content Distribution Network) for distribution around the world. Each cloud vendor has one, but <strong>Cloudinary</strong> also provides automated resizing needed for different size screens.


1. The next level of automation is generation of GitHub Markdown code from "flat" (<strong>csv</strong> text) files containing data. That's done by <strong>Python programs</strong>.

   The caiq-yamll-gen.py program generates Markeown based on a csv file in the same folder.

1. There are code libraries for Python programs to extract and update <strong>Excel</strong> spreadsheets which can be structured as an Excel form for data entry.


1. Sooner than later, developers find they need to keep files in a cloud such as AWS, <strong>Azure</strong>, etc. where a variety of <strong>Data maintenance</strong> tools are available for use. 

1. Each cloud vendor have a different way to write <strong>CLI Bash</strong> programs that invoke <strong>Terraform</strong> to establish a <strong>Vault</strong> system needed to maintain secrets for the whole system.

1. Processing is made repeatable by automation using CI/CD (<strong>GitHub Actions</strong> or CircleCI) which create resources in clouds, plus <strong>Ansible</strong> to configure programs running on each server.


1. When static pages need user-specific interaction such as authentication and authorization to accept payments, an app is built using the popular <strong>React.js</strong> to provide a UI front-end (web and mobile) with a <strong>back-end</strong> providing APIs.

1. To persist data, a data store (database). A graph database such as <strong>Neo4j</strong> provides more flexibility.

1. When there is enough traffic, a <strong>data cache</strong> is commonly added to handle more work by minimizing transfer of the same data.

1. To ensure quick recovery from outages and complete disasters, databases need <strong>backups</strong>.

1. Interactions with individual users means that authentication and authorization is needed before sending <strong>email, SMS</strong> to each users.

1. <strong>Event Logs and server metrics</strong> are collected for troubleshooting and security forensics.

1. Such data are accumulated in a <strong>Time Series</strong> database. <a target="_blank" href="https://www.youtube.com/watch?v=dTc4OGbt80w">VID</a>

1. Trends are illustrated in a <strong>dashboard</strong> application. <strong>Power BI</strong> has been rated as a top tool for that. It's from Microsoft, so its users tend to also use  

1. <strong>analytics</strong> databases and tools in Microsoft's Azure cloud.

1. The decision regarding which cloud to standarize on relates to a choice of and other services. Azure has 

1. Users of the highly-rated <strong>Power BI dashboard</strong> tool tend to also use the <strong>Synapse</strong> database also from Microsoft. 

   There is also open-source Grafana on Linux.

1. To integrate data among various clouds, the utility <strong>Apache Airflow</strong> is increasingly used for sophisticated extracting and importing of data.

1. To reducing processing time, many organizations are replacing time-consuming and error-prone manual approval steps with an Open Policy Agent (<strong>OPA</strong> which automates decisions based on <strong>rules</strong> that leverage various databases.

1. Rules can then be dynamically generated based on <strong>ML</strong> (Machine Language) that leverage existing data to infer <strong>actions</strong>, send <strong>alerts</strong> as soon as appropriate, and <strong>answer</strong> questions. 

   NLP (Natural Language Processing) utilities are getting increasingly mature at generating text, speech, images, and videos. And they are getting easier and easier to adopt.

For your domain to keep up with competitors, consider how quickly you can adopt the progression of technologies.

<a target="_blank" href="https://res.cloudinary.com/dcajqrroq/image/upload/v1658950646/fullest-stack-flow-1692x621_mj7lax.jpg"><img width="750" alt="fullest-stack" src="https://res.cloudinary.com/dcajqrroq/image/upload/v1658950646/fullest-stack-flow-1692x621_mj7lax.jpg"></a>

