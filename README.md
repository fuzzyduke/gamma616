# Itheum GitHub Action to store output in a AWS S3 bucket

## Abstract

Data Providers are one of the most important stakeholders when it comes to the Data NFT ecosystem. The objective of this template is to help data providers run their data gathering scripts automatically and save their results in a "set it and forget it" way.

## Description

This project template aims to help data providers run automated scripts that updates datasets daily under the same URL.

This is done by using a GitHub Action that runs the Data Provider's Python script periodically and uploads the output to a AWS S3 bucket.

## Pre-requisites

- A GitHub account; you can create one [here](https://github.com/signup)

- Available GitHub Actions usage minutes; in public repositories, you have unlimited minutes by default, but if you use a private repository, you have 2000 minutes for free; (if your script takes 1 minute to run, you can run it 2000 times per month; if your script takes less than 1 minute to run, the usage time will be rounded to 1 minute); if you need more minutes you can set up a custom billing plan, but if you run your scripts once a day it's hard to get there (note: GitHub action minutes are cumulative per account, so if you have multiple repositories, the minutes will be shared between them)

- An AWS account; you can create one [here](https://portal.aws.amazon.com/billing/signup#/start)

- Git installed locally; you can get it [here](https://git-scm.com/downloads)

- GitHub CLI installed locally; you can get it [here](https://cli.github.com/)

- A Python script that outputs its results to a file (or multiple ones)

## How to use

### A. Initial Git setup & Logging in to git with yout GitHub account locally

Note: You can jump over this step if you have installed and used git before on your local machine.
Open a terminal (command line interface). Use this series of commands:

```
    git config --global user.name "Your name here"
```

```
    git config --global user.email "Your mail here"
```

```
    gh auth login
```

After this third command, follow the steps to login to your GitHub account.

### B. Creating an AWS S3 bucket

Note: You can jump over this step if you already have an AWS S3 bucket.

1. Go to [AWS S3](https://aws.amazon.com/) and click on "Sign in to the Console" on the top right corner of the page. If you are not logged in, you will be asked to log in with your AWS account.

2. Once logged in to the AWS Console, use the search bar to search for "S3" and click on the first result. Once on the S3 page, click on "Create bucket".

3. Select a name for your bucket and choose a preffered region for its hosting. For the "Object ownership" option choose ACLs enabled. For "Block Public Access settings for this bucket" make sure all the checkboxes are UNchecked (except for the one asking you to acknowledge that these settings might result in this bucket becoming public). You can let the other options as default. Click on "Create bucket". Note: AWS S3 is (at the time of writing this guide) offering a free tier that allows you to store up to 5GB of data for free for 12 months. If you need more storage, you can set up a custom billing plan. You can find out more about AWS Free Tier [here](https://aws.amazon.com/free/) and about AWS pricing [here](https://aws.amazon.com/s3/pricing/).

4. In your bucket's menu, go to permissions and scroll down until you see "Cross-origin resource sharing (CORS)". Click on "Edit" and paste the following text there:
```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [
            "Access-Control-Allow-Origin"
        ]
    }
]
```

### C. Creating a GitHub repository & preparing it for usage

1. Go on GitHub and create a new repository under your desired account using this template (click on the green "Use this template" button on the top right corner of [this page](https://github.com/Itheum/auto-data-generation-action)). Select a name for your repository, decide whether you want your repository to be public or private and click on "Create repository from template". Wait a few seconds for your repository to be generated

2. Once your repository is generated, click on the green "Code" button and copy the HTTPS link that appears. Open a terminal on your local machine and run the following command:

```
    git clone YOUR_REPOSITORY_URL
```

This will clone the repository to your local machine.

3. Go back to your repository page on GitHub. Click on "Settings". Then, under the "Security" section, click on "Secrets and variables" and then on "Actions".

4. We will have to create three secrets that will be used inside of our GitHub Action. We are using them as secrets instead of directly in the code in order to keep these variables private from the public. Click on "New repository secret" and create the following secrets:

- Name: S3_BUCKET_NAME, Secret: the name of the AWS S3 bucket you created in the previous step (if you don't remember it, you can find it by going to your account's AWS S3 page)
- Name: S3_KEY_ID, Secret: the AWS Access Key ID of your AWS account. You can generate one by clicking on your account name on the right top corner in AWS and then clicking on security credentials. Then, go to access keys and click "Create access key". After accepting the prompt and click again on "Create access key", your key will be created. The characters under "Access key" is your key ID. You have a button that you can use to copy it. Don't close this page after that, we will also need the secret access key for the next secret.
- Name: S3_ACCESS_KEY, Secret: the Secret access key coresponding to your AWS Access Key ID. You can find it in the same page as the previous secret.

### D. Adjusting your script to the template & getting it to GitHub

1. You can now go open the repository you clone on your local machine. For this template to work flawslessly it is important to adapt your script by following the following standards:

- The main file that is triggered via the command line should be named "main.py". Feel free to delete the current main.py file and replace it with your own. You can have more files in your repository, but make sure that the main file is named "main.py" and that it is in the root of the repository.

- Make sure that all the files that you want to get into your AWS S3 bucket are saved by the script in the "output" folder. Feel free to delete the mock "data.json" file that is currently there.

- Make sure that all the packages that are not included by default in Python are listed in the "requirements.txt" file, one per line. Feel free to delete the current requirements that are listed there as an example for now.

2. Once you are done with this, your script is ready to go into GitHub. Go back to your terminal and run the following commands:

```
    git add .
```

```
    git commit -m "YOUR_COMMIT_MESSAGE_HERE"
```

```
    git push
```

3. Congrats! Now everything is ready and the script will run daily at 23:30 UTC or whenever you push new code to your repository. Whenever you make a change to your code locally, you can use the three commands above to push the changes to GitHub and the script will run again. You can also check the logs of the script by going to your repository page on GitHub, clicking on "Actions" and then on the latest workflow run. You can also check the output of the script by going to your AWS S3 bucket and checking the files in the "output" folder.

### If the workflow run was successful you can now go to your AWS S3 and click on your bucket. You should be able to see your objects there. Clicking on your object will allow you to see a link that can be used to access that object (file). You can now use that link to create a Data NFT!

## Customization

You can customize by changing the update-data.yaml file inside of the .github/workflows folder. If you don't see the .github folder, make sure you enabled seeing hidden files inside your explorer. More about GitHub Actions [here](https://docs.github.com/en/actions)

## Contributing

Feel free the contact the development team if you wish to contribute or if you have any questions. If you find any issues, please report them in the Issues sections of the repository. You can also create your own pull requests which will be analyzed by the team.

## Disclaimer

This open-source SOFTWARE PRODUCT is provided by THE PROVIDER "as is" and "with all faults." THE PROVIDER makes no representations or warranties of any kind concerning the safety, suitability, lack of viruses, inaccuracies, typographical errors, or other harmful components of this SOFTWARE PRODUCT. There are inherent dangers in the use of any software, and you are solely responsible for determining whether this SOFTWARE PRODUCT is compatible for your needs. You are also solely responsible for the protection of your equipment, your private credentials (e.g AWS account Key and Secret, GitHub access credentials etc.) and backup of your data, and THE PROVIDER will not be liable for any damages you may suffer in connection with using, modifying, or distributing this SOFTWARE PRODUCT.
