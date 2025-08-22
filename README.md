<h1 id="title" align="center">Stewart Calculus Solution Book</h1>

<div align="center">
<img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome Badge"/>
<img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99" alt="Star Badge"/>
<a href="https://discord.gg/XTW52Kt"><img src="https://img.shields.io/discord/733027681184251937.svg?style=flat&label=Join%20Community&color=7289DA" alt="Join Community Badge"/></a>
<a href="https://twitter.com/fisher" ><img src="https://img.shields.io/twitter/follow/fisheryv.svg?style=social" /> </a>
</div>

## 👏 Welcome

Welcome to the *Stewart Calculus Solution Book*. 

This collection of problem solutions is compiled from the exercises I completed while self-studying [Stewart Calculus](https://www.stewartcalculus.com/), based on the `Metric Version | 9th Edition | Early Transcendentals`.

<div align=center><img src="_media/cover.jpg" width=200/></div>

Although an official solutions manual is available, I think it has the following shortcomings:

- **Incomplete** – Only provides solutions to odd-numbered exercises

- **Inadequate** – Many solutions lack detailed derivations

- **Inconvenient** – Both printed books and PDF documents are difficult to search and navigate

Therefore, with the encouragement of teachers, I decided to maintain a community version of the solution book based on my own answers. The goal is to help calculus learners better understand knowledge points, while also pushing myself to complete all exercise solutions. This aligns with the Feynman Learning Method I enjoy – learning by teaching.

> ⚠️**Warning:** 
>
> Please use this solution book responsibly and DO NOT plagiarize the answers to complete your assignments! Academic integrity is of utmost importance, and we must all adhere to it.


<h2 id="getting-started"> 🚀 Getting Started </h2>

### Online

The latest version is deployed on Github Pages. Open [https://fisheryv.github.io/stewart-calculus-solution-book/](https://fisheryv.github.io/stewart-calculus-solution-book/) in browser to access.

### Local

1. **Set up environment**

    This project is maintained using [docsify](https://docsify.js.org/). To contribute code or run it locally, first install `node.js` and `docsify-cli`: 

    1.1. Installing [Node.js](https://nodejs.org/)

    Please follow the instructions at [https://nodejs.org/en/download](https://nodejs.org/en/download) to install `Node.js` on your local device.

    1.2. Installing [docsify](https://docsify.js.org/)

    Install `docsify` via the following command:
    ```bash
    npm i docsify-cli -g
    ```
    For more information about docsify, please refer to the [docsify official website](https://docsify.js.org/).

2. **Install git**

    Please follow the instructions at [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install `git`.

3. **Clone this repository**

    Download this repository to your local device using 
    ```bash
    git clone https://github.com/fisheryv/stewart-calculus-solution-book.git
    cd stewart-calculus-solution-book
    ```
    This command will create a directory named `stewart-calculus-solution-book` containing the sources for the current releases.

4. **Run locally**

    Execute the following command in the project directory:
    ```bash
    docsify serve ./
    ```
    to preview contents. You will see the following output:
    ```bash
    Serving ./stewart-calculus-solution-book now.
    Listening at http://localhost:3000
    ```
    Open http://localhost:3000 in your browser to view the content.

## ⌛️ Progress

```txt
⏳ Completion Progress  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  3.80 %
```

## ✨ Contribution

This project is actively maintained, and contributions of any kind are welcome, including but not limited to:

- Fixing typos and errors
- Adding alternative solutions
- Answering open questions


### How to Contribute

Assuming you have completed the setup of the local environment. If not, please refer to the [Getting Started](#getting-started) section.

1. **Fork the Repository**

    Click the `Fork` button to create a copy of the this [original repository](https://github.com/fisheryv/stewart-calculus-solution-book.git) in your GitHub account.

2. **Clone the Fork**

    Download the forked repository to your local machine using 
    ```bash
    git clone https://github.com/[your_account_name]/stewart-calculus-solution-book.git
    cd stewart-calculus-solution-book
    ```
    This command will create a directory named `stewart-calculus-solution-book` containing the sources for the current releases.

    All exercise solution files are located in the `docs/` directory, structured as follows:
    ```
    docs/
    ├── ch[*]/
        ├── section[*]/
            ├── Problem[*].md
    ```  
    `ch[*]/` represents chapter directories, `section[*]/` represents section directories. Solution files for each exercise (or exercise set) are stored under section directories, with one markdown file per exercise. Each section directory also contains an `_media/` subdirectory for storing image resources required by the exercises in that section.

3. **Make Changes**

    Modify the code and commit the changes using `git add` and `git commit`.

4. **Push Changes**

    Push the branch to your forked repository using `git push`.

5. **Submit a Pull Request**
    
    Navigate to your forked repository on GitHub and click "Compare & pull request" to propose your changes.

### File Template

To maintain consistency in visual presentation, please write questions and solutions according to the following template:

- **Question Part**
```html
<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem No.</h4>

Here is the question...

</div>
```

- **Solution Part**
```html
<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

Here is the solution...

</div>
```

This project has integrated `katex`, `mermaid`, and `bootstrap`. If additional docsify plugins are needed, please refer to the [docsify plugin list](https://docsify.js.org/#/awesome?id=plugins).


## ©️ License

This work is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1">